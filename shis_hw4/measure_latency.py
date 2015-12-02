#!/usr/bin/env python
#
# Measure the response time difference to a certain webserver
# between direction connection and Tor connection
#
# Author: Shi Su, AndrewId:shis
# 12/01/2015

import io
import time
import pycurl
from stem.control import Controller
from stem.util import term
from stem import Signal
import argparse

CONTROL_PORT = 9151
SOCKS_PORT = 9150
DEFAULT_URL = "https://stem.torproject.org/tutorials/to_russia_with_love.html"
DEFAULT_RETRY = 10

"""
    Connect to a url without going through Tor
"""
def direct_connection(url):
    output = io.BytesIO()
    query = pycurl.Curl()
    query.setopt(pycurl.URL, url)
    query.setopt(pycurl.WRITEFUNCTION, output.write)
    
    try:
        query.perform()
        return output.getvalue()
    except pycurl.error as exc:
        return "Unable to reach %s (%s) directly" % (url, exc)

"""
    Connect to a url through Tor
"""
def tor_connection(url):
    # reset tor identity before each request
    reset_identity()

    output = io.BytesIO()
    query = pycurl.Curl()
    query.setopt(pycurl.URL, url)
    query.setopt(pycurl.PROXY, 'localhost')
    query.setopt(pycurl.PROXYPORT, SOCKS_PORT)
    query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5_HOSTNAME)
    query.setopt(pycurl.WRITEFUNCTION, output.write)

    try:
        query.perform()
        return output.getvalue()
    except pycurl.error as exc:
        return "Unable to reach %s (%s) through Tor" % (url, exc)

"""
    Reset Tor identity before each request
"""
def reset_identity():
    with Controller.from_port(port = CONTROL_PORT) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

"""
    direct connection response time 
"""
def direct_response_time(url):
    start = time.time()
    direct_connection(url)
    end = time.time()
    return end - start

"""
    Tor connection response time 
"""
def tor_response_time(url):
    start = time.time()
    tor_connection(url)
    end = time.time()
    return end - start

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Measure the latency w/ or w/o using Tor')
    parser.add_argument('-u','--url', help='Url for testing')
    parser.add_argument('-r','--retry', help='How much time do we retry')
    args = parser.parse_args()

    url = DEFAULT_URL if args.url is None else args.url
    retry = DEFAULT_RETRY if args.retry is None else args.retry


    direct = 0
    tor = 0
    for i in range(0,retry):
        direct = direct + direct_response_time(url)
        tor = tor + tor_response_time(url)
    direct = direct / retry
    tor = tor / retry

    print("Test URL: %s" % (url))
    print("Average direct response time: %0.2fs" % (direct))
    print("Average Tor response time %0.2fs" % (tor))
