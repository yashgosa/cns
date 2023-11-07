import random
import math

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True

def genrate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime): 
        prime = random.randint(min_value, max_value)
    return prime

def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e)% phi == 1:
            return d
    raise ValueError('mod inverse dosent exist')

p, q = genrate_prime(1000, 5000), genrate_prime(1000, 5000)

while p == q: q = genrate_prime(1000, 5000)

n = p * q
phi_n = (p - 1) * (q - 1)

e = random.randint(3, phi_n - 1)
while math.gcd(e, phi_n) != 1: e = random.randint(3, phi_n - 1)

while True:
    try:
        d = mod_inverse(e, phi_n)
    except ValueError:
        continue
    break;

print("Public_key", e)
print("Private key", d)
print("n", n)
print("Phi of n", phi_n)
print("q", q)
print("p", p)

message = "Yash Gosavi"

message_encoded = [ord(c) for c in message]
# (m ^ public_key) mod n = c
cipher = [pow(c, e, n) for c in message_encoded]
decrypt = ''.join([chr(pow(c, d, n)) for c in cipher])

print(''.join([str(c) + ' ' for c in cipher]))
print(decrypt)