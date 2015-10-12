#!/usr/bin/env python

import argparse
import binascii
from shis_decticket import get_padding_num, hasValidPadding

# Use padding oracle to encrypt message
#
# Create by: Shi Su, AndrewId:shis
# 10/08/2015

BLOCK_SIZE = 8

# the Dec(C) got from decticket.py
DEC_C_LAST = "d4fa773185b7bcb9"
CIPHER_LAST = "e9fa63236a1a6c90"


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
        expiration = "2022-01-31"
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

# this is so ugly, but I don't have time to clean up
def encrypt_ticket():

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

    # Use the last block of Dec(C) as last block of new Dec(C)
    if (args.dec_c_last is None):
        block_dec = DEC_C_LAST
    else:
        block_dec = args.dec_c_last

    # Use the last block of cipher as last block of new cipher
    if (args.cipher_last is None):
        block_cipher = CIPHER_LAST
    else:
        block_cipher = args.cipher_last

    # start from last block
    encrypted = block_cipher
    # count down from last block
    for i in range(len(p_blocks) - 1, -1, -1):
        print "----------------------------------------"
        print "testing cipher block " + str(i)+ " :" + block_cipher
        print "plain text:" + int_to_hex_str(p_blocks[i])

        # get Dec(C) of this block
        if not i == len(p_blocks) - 1:
            decrypted_byte = 0
            padding_num = 0
            padding = 0
            test_block = bytearray(BLOCK_SIZE)
            # previous VI being hack as a cipher
            target_block = bytearray.fromhex(block_cipher)
            dec_target = bytearray(BLOCK_SIZE)

            while decrypted_byte < BLOCK_SIZE:
                print "--------------------"
                print " encrypted_bytes: " + str(decrypted_byte)
                # the byte is changing to produce a valid padding
                test_byte = BLOCK_SIZE - decrypted_byte - 1
            
                # change 1 byte in testblock, try to generate Px with valid padding
                for x in range(0,256):
                    test_block[test_byte] = x
                    # send the 2 byte to oracle
                    query = binascii.hexlify(test_block) + binascii.hexlify(target_block)
                    if hasValidPadding(query):
                        break

                if decrypted_byte == 0:
                    padding_num = get_padding_num(test_block, target_block)
                    # The last few byte got decrypted
                    # Dec(Ctarget) = Ptest(with padding) ^ Ctest
                    for y in range( BLOCK_SIZE - padding_num, BLOCK_SIZE):
                        dec_target[y] = test_block[y] ^ padding_num

                    decrypted_byte = padding_num
                else:
                    padding_num = decrypted_byte + 1
                    # only the last few bytes are useful
                    # Dec(Ctarget) = Ptest(with padding) ^ Ctest
                    dec_target[test_byte] = test_block[test_byte] ^ padding_num

                    
                    decrypted_byte += 1

                print "dec_target: " + binascii.hexlify(dec_target)

                for z in range (0, BLOCK_SIZE):
                    test_block[z] = dec_target[z] ^ (padding_num + 1)

            block_dec = binascii.hexlify(dec_target)
       
        # Ci-1 = Pi ^ DEC(Ci)    
        block_cipher = int_to_hex_str(p_blocks[i] ^ int(block_dec, 16))
        encrypted = block_cipher + encrypted
        print "Encrypted: " + encrypted    

    print "----------------------------------------"
    print "Cipher Text: " + encrypted




if __name__ == "__main__":
   parser = argparse.ArgumentParser(description='Encrypted a ticket with given information')
   parser.add_argument('-u','--username', help='Username')
   parser.add_argument('-a','--is_admin', help='Is the user admin, true/false')
   parser.add_argument('-e','--expiration', help='Expiration date of the ticket, e.g. 2015-10-07')
   parser.add_argument('-d','--dec_c_last', help='Last block of Dec(C) text used for encrypting the ticket')
   parser.add_argument('-c','--cipher_last', help='Last block of the cipher text')
   args = parser.parse_args()
   encrypt_ticket()
