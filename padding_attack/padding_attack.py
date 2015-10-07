#!/usr/bin/env python

# Use padding oracle to decrypt DEC encrypted message
#
# Create by: Shi Su, AndrewId:shis
# 10/06/2015

import httplib
import argparse
import binascii

# ORACLE_HOST = "127.0.0.1"
# QUERY_PATH = "/oracle.php?ticket="
ORACLE_HOST = "stackoverflow.com"
QUERY_PATH = "/search?q="
# cipher text in HW1
ENCRYPT_TICKET = "0c80353a2c634be44096f9d7977bad4d60dcd000224743105c8eacc3f872e37a2e6c8afdaecba65e8d94754e15a587ea1620cf6b6bc59a0fe5d74400a7cabebbe9fa63236a1a6c90"
BLOCK_SIZE = 8

""" 
    Ask oracle if the decrypted ticket has valid padding
    by making HEAD request as we only need the status code
    Return True if status code is 200, otherwise return False
"""
def hasValidPadding(query):
    conn = httplib.HTTPConnection(ORACLE_HOST)
    conn.request("HEAD", QUERY_PATH + query)

    # return conn.getresponse().read();    
    status = conn.getresponse().status;

 #   print status

    if status == 200:
        return True
    else:
        return False

"""
    Divide the long ciphertext into 16 hex string blocks
"""
def chuck(string):
    return [ int(string[i:i + BLOCK_SIZE * 2], 16) for i in range(0, len(string), BLOCK_SIZE * 2) ]

"""
    Transfer the block back to hex representation string
    To form the query string for oracle
"""
def int_to_hex_str(block):
    hex_string = hex(block)
    # use replace with 0x because strip removes ending 0s
    return hex_string.replace("0x","").strip('L').zfill(BLOCK_SIZE * 2) 

"""
    Generate the mask for updating the test byte of Ci-1
"""
def get_mask(learned_byte, num):
    return num << 8 * learned_byte

"""
    When creating valid padding for the first time in a block
    Get the actual numbers of padding byte
"""
def get_padding_num(test_block, target_block):
    # random number for a byte
    mask = 0x3200000000000000

    for i in range(0, BLOCK_SIZE):

        # int is immutable, the change here won't affect outside
        test_block = test_block^mask
        mask = mask >> 8
        query = int_to_hex_str(test_block) + int_to_hex_str(target_block)
        if not hasValidPadding(query):
            break

    return BLOCK_SIZE - i

"""
    Get actual padding when knowning the number of padding
"""
def get_padding(padding_num):
    padding = 0
    for i in range(0, padding_num):
        padding = (padding << 8) + padding_num

    return padding




def padding_attack():

    # if no other cipher text provided, decrypt the one provided in HW1
    if args.ciphertext is None:
        ciphertext = ENCRYPT_TICKET
    else:
        ciphertext = args.ciphertext

    # 2 hex character represent 1 byte, remove IV block
    length = (len(ciphertext) >> 1) - BLOCK_SIZE
    # number of block = length/8
    block_num = length >> 3
    # create a bytearray with all 0 to store decrypted text
    plaintext = bytearray([15]*length)

    print hex(get_mask(5,9));
    
    blocks = chuck(ciphertext)

    reconstruct = ""
    for block in blocks:
        print int_to_hex_str(block)
        reconstruct = reconstruct + int_to_hex_str(block)

    print reconstruct
    print hasValidPadding(ciphertext)

    print get_padding_num(blocks[0],blocks[1])

    print hex(get_padding(3))

    print binascii.hexlify(plaintext)

    return



if __name__ == "__main__":
   parser = argparse.ArgumentParser(description='Use padding attack to decrypt a DES encrypted ticket')
   parser.add_argument('-c','--ciphertext', help='DES ciphertext to be decrypted')
   args = parser.parse_args()
   padding_attack()