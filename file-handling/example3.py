import os

if not os.path.exists("name_list.pdf"):
    f = open("name_list.pdf","x")
    f.close()

#deleting a file if the file does not exist
if os.path.exists("name_list.pdf"):
    os.remove("name_list.pdf")

else:
    print("the file you wish to delete has not been deleted successfully.")

#writing the content of another file into another file
with open("newfile.pdf","r") as s:
    content = s.read()

with open("input.txt","w") as f:
    f.write(content)


if not os.path.exists("name_list.pdf"):
    f = open("name_list.pdf","x")
    f.close()

f = open("name_list.pdf","w")
f.write(content)
f.close()

f = open("name_list.pdf","r")
update = f.read().upper()
f.close()

f = open("name_list.pdf","w")
f.write(update)
f.close()
