import os
import binascii

rand = os.urandom(32)
strand = binascii.hexlify(rand).decode()
print(strand)
