#!/usr/bin/env python

# Use timing attack to generate a valid MAC without secret key
#
# Author: Shi Su, AndrewId:shis
# 12/01/2015

from stem import CircStatus
from stem.control import Controller

CONTROL_PORT = 9151

with Controller.from_port(port = CONTROL_PORT) as controller:
    controller.authenticate()

    for circ in sorted(controller.get_circuits()):
        if circ.status != CircStatus.BUILT:
            continue

        print("")
        print("Circuit %s (%s)" % (circ.id, circ.purpose))
        print(" |- Nickname: IP, country, bandwidth")
        print(" |----------- fingerprint")

        for i, entry in enumerate(circ.path):
            div = '+' if (i == len(circ.path) - 1) else '|'
            fingerprint, nickname = entry

            desc = controller.get_network_status(fingerprint, None)
            address = desc.address if desc else 'unknown'
            bandwidth = desc.bandwidth if desc else 'unknown'
            print(" |- %s: %s, %s" % (nickname, address, bandwidth))
            print(" %s----------- %s" % (div, fingerprint))

# import stem
# import argparse
# import sys

# from stem.connection import connect

# if __name__ == '__main__':
#   controller = connect(('127.0.0.1', 9151))

#   if not controller:
#     sys.exit(1)  # unable to get a connection

#   print 'Tor is running version %s' % controller.get_version()
#   controller.close()

