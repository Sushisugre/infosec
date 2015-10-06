#!/usr/bin/env python

# Call oracle to


import httplib

# ORACLE_HOST = "127.0.0.1"
# QUERY_PATH = "/oracle.php?ticket="
ORACLE_HOST = "stackoverflow.com"
QUERY_PATH = "/search?q="

""" 
    ask oracle if the decrypted ticket has valid padding
    by making HEAD request as we only need the status code
    Return True if status code is 200, otherwise return False
"""
def hasValidPadding(query):
    conn = httplib.HTTPConnection(ORACLE_HOST)
    conn.request("HEAD", QUERY_PATH + query)

    status = conn.getresponse().status;

    print status

    if status == 200:
        return True
    else:
        return False





def padding_attack():
    print hasValidPadding("ticket") 
    return


padding_attack()