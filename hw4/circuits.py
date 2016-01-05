#!/usr/bin/env python

# List the Tor circuits used by this machine
#
# Author: Shi Su, AndrewId:shis
# 12/01/2015

from stem import CircStatus
from stem.control import Controller

CONTROL_PORT = 9151

with Controller.from_port(port = CONTROL_PORT) as controller:
    controller.authenticate()
    
    # interate through all the available circuit
    for circ in sorted(controller.get_circuits()):
        if circ.status != CircStatus.BUILT:
            continue

        print("")
        print("Circuit %s (%s)" % (circ.id, circ.purpose))
        print(" |- Nickname: IP, country, bandwidth")
        print(" |----------- fingerprint")

        # interate through the entries in a circuit
        for i, entry in enumerate(circ.path):
            div = '+' if (i == len(circ.path) - 1) else '|'
            fingerprint, nickname = entry

            desc = controller.get_network_status(fingerprint, None)
            address = desc.address if desc else 'unknown'
            bandwidth = desc.bandwidth if desc else 'unknown'
            country = controller.get_info("ip-to-country/%s" % address, 'unknown')
            
            print(" |- %s: %s, %s, %s" % (nickname, address, country, bandwidth))
            print(" %s----------- %s" % (div, fingerprint))


