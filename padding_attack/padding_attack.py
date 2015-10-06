#!/usr/bin/env python

#
# Create by: Shi Su, AndrewId:shis
# 10/06/2015

import httplib
import argparse

# ORACLE_HOST = "127.0.0.1"
# QUERY_PATH = "/oracle.php?ticket="
ORACLE_HOST = "stackoverflow.com"
QUERY_PATH = "/search?q="
# cipher text intercepted
ENCRYPT_TICKET = "0c80353a2c634be44096f9d7977bad4d60dcd000224743105c8eacc3f872e37a2e6c8afdaecba65e8d94754e15a587ea1620cf6b6bc59a0fe5d74400a7cabebbe9fa63236a1a6c90"

""" 
    ask oracle if the decrypted ticket has valid padding
    by making HEAD request as we only need the status code
    Return True if status code is 200, otherwise return False
"""
def hasValidPadding(query):
    conn = httplib.HTTPConnection(ORACLE_HOST)
    conn.request("GET", QUERY_PATH + query)

    # return conn.getresponse().read();    
    status = conn.getresponse().status;

    print status

    if status == 200:
        return True
    else:
        return False


def padding_attack():

    # if no other cipher text provided, decrypt the one provided in HW1
    if args.ciphertext is None:
        ciphertext = ENCRYPT_TICKET
    else:
        ciphertext = args.ciphertext
    
    print hasValidPadding(ciphertext)

    return


# padding_attack()

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description='Use padding attack to decrypt a DES encrypted ticket')
   parser.add_argument('-c','--ciphertext', help='ciphertext')
   args = parser.parse_args()
   padding_attack()