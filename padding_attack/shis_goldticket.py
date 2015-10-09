#!/usr/bin/env python

import argparse
import binascii

# Use padding oracle to decrypt DEC encrypted message
# If no cipher is specified through -c, decrypted the ticket provided in the homework
#
# Create by: Shi Su, AndrewId:shis
# 10/08/2015

BLOCK_SIZE = 8
# the Dec(C) got from decticket.py

DEC_C = "77a24049491125852df3dbedb51cd82813a8f22c002e304f3deac1aa9650d958480de68ecbe98a7ce8ec052767c0e3c82c02fd5b5bf5b73fd4fa773185b7bcb9"
#DEC_C_LAST = "d4fa773185b7bcb9"
#CIPHER_LAST = "e9fa63236a1a6c90"

# IV (C0) from the intercepted cipher
IV = "0c80353a2c634be4"

def generate_ticket():
    if (args.username is None):
        username = "shis"
    else:
        username = args.username

    if (args.is_admin is None):
        is_admin = "true"
    else:
        is_admin = args.is_admin

    if (args.expiration is None):
        expiration = "3000-01-31"
    else:
        expiration = args.expiration

    return "{\"username\":\""+ username +"\",\"is_admin\":\""+ is_admin +"\",\"expired\":\""+expiration+"\"}"

def chunck(string):
    return [ int(string[i:i + BLOCK_SIZE * 2],16) for i in range(0, len(string), BLOCK_SIZE * 2) ]

"""
    Transfer the block back to hex representation string
    To form the query string for oracle
"""
def int_to_hex_str(block):
    hex_string = hex(block)
    # use replace with 0x because strip removes ending 0s
    return hex_string.replace("0x","").strip('L').zfill(BLOCK_SIZE * 2) 

def encrypt_ticket():

    # use the Dec(C) string from decrypted ticket if no new one provided
    if (args.dec_string is None):
        dec_string = DEC_C
    else:
        dec_string = args.dec_string

    ticket = generate_ticket()
    print ticket
    hex_ticket = ticket.encode("hex")

    # add padding
    padding_num = BLOCK_SIZE - (len(ticket) % 8)
    if padding_num == 0:
        padding_num = 8
    for i in range (0, padding_num):
        hex_ticket = hex_ticket + "0" + str(padding_num)

    # generate blocks
    p_blocks = chunck(hex_ticket)
    dec_blocks = chunck(dec_string)

    encrypted = ""
    for i in range(0, len(dec_blocks)):
        print "C" + str(i)
        print "P" + str(i+1)
        print "Dec" + str(i+1)
        encrypted_block = p_blocks[i] ^ dec_blocks[i]
        encrypted =  int_to_hex_str(encrypted_block) ＋ encrypted
        print encrypted

    print encrypted




if __name__ == "__main__":
   parser = argparse.ArgumentParser(description='Encrypted a ticket with given information')
   parser.add_argument('-u','--username', help='Username')
   parser.add_argument('-a','--is_admin', help='Is the user admin, true/false')
   parser.add_argument('-e','--expiration', help='Expiration date of the ticket, e.g. 2015-10-07')
   parser.add_argument('-d','--dec_string', help='Dec(C) string used for encrypting the ticket')
   args = parser.parse_args()
   encrypt_ticket()
