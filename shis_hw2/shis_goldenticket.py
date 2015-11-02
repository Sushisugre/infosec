#!/usr/bin/env python

# Use timing attack to generate a valid MAC without secret key
#
# Create by: Shi Su, AndrewId:shis
# 11/01/2015

import nanotime
import httplib
import argparse
import binascii
import operator

ORACLE_HOST = "127.0.0.1"
QUERY_PATH = "/auth.php?"
RETRY = 3

# generate ticket according to command line argument
def generate_ticket():
    if (args.username is None):
        username = "guest" #shis
    else:
        username = args.username

    if (args.is_admin is None):
        is_admin = "false" #true
    else:
        is_admin = args.is_admin

    if (args.expiration is None):
        expiration = "2000-01-31" #2022-01-31
    else:
        expiration = args.expiration

    return "{\"username\":\""+ username +"\",\"is_admin\":\""+ is_admin +"\",\"expired\":\""+expiration+"\"}"

# convert int array to hex string
def to_hex_string(array):
    str=""
    for i in range (0, 32):
        str = str + hex(array[i]).replace("0x","")
    return str


""" 
    Ask oracle if the ticket has valid MAC
    by making HEAD request as we only need the status code
    Return True if status code is 200, otherwise return False
    Query: ticket=xxx&mac=yyy
"""
def validate_MAC(query):
    conn = httplib.HTTPConnection(ORACLE_HOST)
    conn.request("GET", QUERY_PATH + query)
    resp = conn.getresponse()
    # content = resp.read()

    # if content is not "INVALID MAC":
    #     return True
    # else:
    #     return False


def timming_attack():

    ticket = generate_ticket()
    print ticket

    MAC = ""
    # initialize array
    MAC_array = bytearray([0] * 32)
    dict_freq = {}
        #     0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0,
        # 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0

    # compute a baseline 
    MAC = to_hex_string(MAC_array)
    query = "ticket=" + ticket + "&mac=" + MAC
    print "mac: " + MAC
    before = nanotime.now()
    # call oracle
    validate_MAC(query)
    after = nanotime.now()
    max_interval = int(after - before)
    print "interval: " + str(max_interval)

    for i in range (0, 32):
        # One time result maybe unreliable, 
        for k in range (0, RETRY):
            max_interval = 0
            candidate = 0
            for j in range (0, 16):
                # from left to right, test the value of one byte
                MAC_array[i] = j
                print str(i)+",("+str(k+1)+"/"+str(RETRY)+"),"+str(j)
                MAC = to_hex_string(MAC_array)
                query = "ticket=" + ticket + "&mac=" + MAC
                print "mac: " + MAC
                before = nanotime.now()
                # call oracle
                validate_MAC(query)
                after = nanotime.now()
                interval = int(after - before)
                print "interval: " + str(interval)

                # if interval become larger, we got another byte correct
                if interval > max_interval:
                    max_interval = interval
                    candidate = j
            # increase the frequency of candidate
            if not candidate in dict_freq:
                dict_freq[candidate] = 1
            else:
                dict_freq[candidate] += 1
        MAC_array[i] = max(dict_freq.iteritems(), key=operator.itemgetter(1))[0]





if __name__ == "__main__":
   parser = argparse.ArgumentParser(description='Encrypted a ticket with given information')
   parser.add_argument('-u','--username', help='Username')
   parser.add_argument('-a','--is_admin', help='Is the user admin, true/false')
   parser.add_argument('-e','--expiration', help='Expiration date of the ticket, e.g. 2015-10-07')
   args = parser.parse_args()
   timming_attack()
