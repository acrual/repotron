import hashlib

string = "Hello World"

stringhash = hashlib.sha256((string).encode()).hexdigest()
print("The hash of ",string," is ",stringhash)
