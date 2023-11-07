import hashlib

#md5
result = hashlib.md5('Yash Gosavi'.encode())
print(result.digest())
print(result.hexdigest())

#sha
print(hashlib.algorithms_guaranteed)  
print ("\r") 

#'sha1', 'sha384', 'sha256', 'sha512', 'sha224'
text = "Yash Gosavi".encode()
sha1 = hashlib.sha1(text)
print(sha1.digest())
print(sha1.hexdigest())
print ("\r") 

sha384 = hashlib.sha1(text)
print(sha384.digest())
print(sha384.hexdigest())  
print ("\r") 

sha256 = hashlib.sha1(text)
print(sha256.digest())
print(sha256.hexdigest())  
print ("\r") 

sha512 = hashlib.sha1(text)
print(sha512.digest())
print(sha512.hexdigest())  
print ("\r") 

sha224 = hashlib.sha1(text)
print(sha224.digest())
print(sha224.hexdigest())  
print ("\r") 
