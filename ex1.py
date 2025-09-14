#creating a new file
import os

if not os.path.exists("names.txt"):
    f = open("names.txt","w")
    f.write("Alice\nBob\nCharlie\n")
    f.close()

#reading a file 
f = open("names.txt","r")
content = f.read()
f.close()

#modifying the contents of the file
f = open("names.txt","w")
f.write(content.upper())
f.close()
