"""
1. Assign a number to each character of the plain-text and the key according to alphabetical order. 
2. Bitwise XOR both the number (Corresponding plain-text character number and Key character number). 
3. Subtract the number from 26 if the resulting number is greater than or equal to 26, if it isn’t then leave it.
"""

import random

def generate_key(plaintext_length):
    key = ''.join(random.choice('QWERTYUIOPLKJHGFDSAZXCVBNM') for _ in range(plaintext_length))
    return key

def encrypt(plaintext, key):
    cipertext = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, key))
    return cipertext

def decrypt(cipertext, key):
    return encrypt(cipertext, key)

plaintext = "Yash"
key = generate_key(len(plaintext))
print(f"encryption of {plaintext} is {encrypt(plaintext, key)}")
print(f"decryption of it is {encrypt(encrypt(plaintext, key), key)}")