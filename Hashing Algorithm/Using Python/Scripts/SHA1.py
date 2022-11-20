# Python program to find SHA1 hash value of a file
import hashlib
 
filename = input("Enter the file name: ")
with open(filename,"rb") as f:
    bytes = f.read() # read file as bytes
    readable_hash = hashlib.sha1(bytes).hexdigest();
    print(readable_hash)