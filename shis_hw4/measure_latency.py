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
import numpy

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
    retry = DEFAULT_RETRY if (args.retry is None) or (args.retry <= 0) else args.retry


    t_directs = []
    t_tors = []
    diffs = []
    diffs_abs = []
    for i in range(0,retry):
        direct = direct_response_time(url)
        tor = tor_response_time(url)
        diff = tor - direct
        diffs.append(diff)
        diffs_abs.append(abs(diff))
        t_directs.append(direct)
        t_tors.append(tor)
        print("Attempt %d - tor: %0.2f, direct: %0.2f, diff: %0.2f, abs diff: %0.2f" % \
             (i + 1, tor, direct, diff, abs(diff)))
    

    arr_direct = numpy.array(t_directs)
    arr_tor = numpy.array(t_tors)

    print("************** Finished *************")
    print("Test URL: %s" % (url))
    print("Max - direct: %0.2f, tor: %0.2f" % (sorted(t_directs)[-1], sorted(t_tors)[-1]))
    print("Min - direct: %0.2f, tor: %0.2f" % (sorted(t_directs)[0], sorted(t_tors)[0]))
    print("Average - direct: %0.2f, tor: %0.2f" % (sum(t_directs)/retry, sum(t_tors)/retry))
    print("Median - direct: %0.2f, tor: %0.2f" % (numpy.median(arr_direct), numpy.median(arr_tor)))
    print("Standard Diviation - direct: %0.2f, tor: %0.2f" % (numpy.std(arr_direct), numpy.std(arr_tor)))
