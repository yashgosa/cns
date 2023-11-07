# pow(g, something, p)

def is_prime(p):
    if p <= 1: return False
    else:
        if p == 2: return True
        for i in range(2, p):
            if p % i == 0:
                return False
        return True
    
def is_primitive(g, p, L):
    for i in range(1, p):
        L.append(pow(g, i, p))
    for i in range(1, p):
        if L.count(i) > 1:
            L.clear()
            return False
        return True
    

while True:
    l = []
    p = int(input("Enter P:"))
    if not is_prime(p): 
        print("Enter a prime number: ")
        continue
    
    g = int(input(f"Enter primitive root of {p}: "))
    if not is_primitive(p, g, l):
        print(f"{g} is not primitive root of {p}")
        continue
    
    x1 = int(input("Private key of User 1: "))
    x2 = int(input("Private key of User 2: "))
    if x1 >= p or x2 >= p:
        print("Private key must be less than p")
        continue

    y1, y2 = pow(g, x1, p), pow(g, x2, p)
    k1, k2 = pow(y2, x1, p), pow(y1, x2, p) # k1, k2 => g-> y2, y1

    if k1 == k2: 
        print("OK")
        break
    else: print("No success")