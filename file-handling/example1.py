f = open("names.pdf","r")
data = f.read()
print(data)
f.close()

f = open("input.txt","a")
f.write("\njohn kiamunyu")
f.close()

f = open("input.txt","r")
data = f.read()
print(data)
f.close()

#counting the number of words in the file
f = open("input.txt","r")

words = f.read().split()
print(words)
f.close()
print("the numbers of words in the file are:", len(words))
f.close()

#converting all the text to uppercase in reading
f = open("input.txt","r")
data = f.read().upper()
print("the newly changed data is:", data)
f.close()

f = open("input.txt","a")
f.write(data)
f.close()

names = ["john", "jane", "doe"]
f = open("names.pdf","w")
for name in names:
    name = name.upper()
    f.write(f"{name}\n")
f.close()

f = open("names.pdf","r")
data = f.read()
print("the data in the file is:", data)
f.close()

#trying to convert the text to uppercase
f = open("names.pdf","r")
data = f.read().lower()
f.close()

f = open("names.pdf","w")
f.write(data)
f.close()