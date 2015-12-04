#!/usr/bin/env python
#
# Measure the response time difference to a certain webserver
# between direction connection and Tor connection
#
# Author: Shi Su, AndrewId:shis
# 12/01/2015

import io
import pycurl
import stem.process
import datetime
from stem.control import Controller
from stem.util import term
from stem import Signal
import argparse

CONTROL_PORT = 9151
SOCKS_PORT = 9150
DEFAULT_URL = "http://dogo.ece.cmu.edu/tor-homework/secret/"
DEFAULT_RETRY = 5
COUNTRIES = [ 'US', 'GB', 'RU', 'DE', 'CA', 'NL', 'FR', 'AU', 'PL', 'CN', 
              'UA', 'IT', 'JP', 'IN', 'SE', 'ES', 'CH', 'RO', 'HK', 'AT', 
              'ID', 'CZ', 'SG', 'BE', 'NO', 'AR', 'DK', 'KR', 'FI', 'CL', 
              'TR', 'IR', 'NZ', 'BR', 'IE', 'ZA', 'BG', 'CO', 'PH', 'HU', 
              'MY', 'SI', 'TW', 'IL', 'TH', 'MX', 'BD', 'GR', 'PT', 'LV', 
              'SA', 'SK', 'NG', 'VN', 'PR', 'RS', 'PA', 'MD', 'LT', 'PK', 
              'VE', 'CR', 'HR', 'KZ', 'EC', 'LU', 'EE', 'HN', 'KE', 'MU', 
              'CY', 'EG', 'AE', 'PE', 'LB', 'BA', 'GT', 'GE', 'IQ', 'KW', 
              'KH', 'TZ', 'BY', 'AZ', 'AM', 'IS', 'PS', 'JO', 'GH', 'MT', 
              'SV', 'MK', 'AL', 'BO', 'DO', 'NI', 'NP', 'BB', 'AF', 'AO', 
              'AG', 'UZ', 'KG', 'MN', 'RE', 'SY', 'JM', 'BH', 'BZ', 'VG', 
              'PY', 'UG', 'MQ', 'LI', 'JE', 'LK', 'GP', 'ZM', 'MZ', 'DZ', 
              'SC', 'CW', 'CM', 'MA', 'VI', 'ZW', 'BM', 'UY', 'KN', 'TT', 
              'CD', 'ME', 'GA', 'OM', 'GU', 'BS', 'NA', 'QA', 'BW', 'NC', 
              'IM', 'PG', 'GF', 'VC', 'MW', 'LY', 'MO', 'GI', 'GD', 'GN', 
              'FJ', 'LC', 'KY', 'HT', 'DM', 'MG', 'SD', 'LS', 'CI', 'BN', 
              'LA', 'YE', 'TJ', 'MM', 'LR', 'VA', 'BJ', 'SZ', 'AW', 'CG', 
              'RW', 'BF', 'CU', 'MF', 'SO', 'MC', 'AI', 'BI', 'DJ', 'AS', 
              'VU', 'TN', 'SL', 'SN', 'NE', 'ML', 'WS', 'YT', 'SR', 'MR', 
              'MV', 'PF', 'SM', 'FO', 'GM', 'GY', 'TD', 'AX', 'SX', 'GG', 
              'BQ', 'BT', 'TC', 'SS', 'CV', 'MP', 'TL', 'TO', 'MS', 'SB', 
              'AD', 'GQ', 'CF', 'TM', 'BL', 'TG', 'NR', 'FM', 'GL', 'KP', 
              'MH', 'PM', 'GW', 'KM', 'FK', 'ET', 'PW', 'AQ', 'ST', 'XK', 
              'NF', 'WF', 'TV', 'KI', 'NU', 'TK', 'CC', 'CK', 'ER', 'TF', 
              'UM', 'IO', 'PN', 'SJ', 'GS', 'CX', 'SH']


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
    query.setopt(pycurl.CONNECTTIMEOUT, 30)

    try:
        query.perform()
        return query.getinfo(pycurl.HTTP_CODE)
    except pycurl.error as exc:
        return "Unable to reach %s (%s) through Tor" % (url, exc)

def reset_identity():
    with Controller.from_port(port = CONTROL_PORT) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

# Start an instance of Tor configured to only exit through Russia. This prints
# Tor's bootstrap information as it starts. Note that this likely will not
# work if you have another Tor instance running.

def print_bootstrap_lines(line):
  if "Bootstrapped " in line:
    print(term.format(line, term.Color.BLUE))


def launch_tor(country):
    print(term.format("Starting Tor with exit node in %s:" % (country), term.Attr.BOLD))
    try:
        tor_process = stem.process.launch_tor_with_config(
            config = {
                'SocksPort': str(SOCKS_PORT),
                'ControlPort': str(CONTROL_PORT),
                'ExitNodes': "{"+country+"}",
            },
            timeout = 40,
            # init_msg_handler = print_bootstrap_lines,
        )
    except OSError: 
        print("Timeout when trying to find relay....")
        return 0
    return tor_process



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Measure the latency w/ or w/o using Tor')
    parser.add_argument('-u','--url', help='Url for testing')
    parser.add_argument('-r','--retry', help='How much time do we retry')
    args = parser.parse_args()

    url = DEFAULT_URL if args.url is None else args.url
    retry = DEFAULT_RETRY if args.retry is None else int(args.retry)
    accessible = []

    for country in COUNTRIES:

        tor_process = launch_tor(country)
        # if not able to find relay in specified country
        if tor_process == 0:
            continue

        try:
            print(term.format("Connecting to server:", term.Attr.BOLD))
            # retry 5 times in each country
            for i in range(0, retry):
                status = tor_connection(url)
                print("Attempt %d: %s" % (i + 1, status))
                # if status == 403:
                #     break
                if status == 200:
                    # store to accessible list
                    print("Find %s returns 200, %s" %  
                        (country, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                    accessible.append(str("Find %s returns 200, %s" %  
                        (country, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))) 
                    break
        finally:
            if tor_process != 0:
                tor_process.kill()  # stops tor

    # print result
    print("Countries that are not blocked:")
    print(accessible)

    # tor_process.kill()  # stops tor

