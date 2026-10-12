import os
#x : create
#a : append:
#w : write
#r : read
with open(".\\apple.txt","r") as f:
  print(f.read())

#delete a file
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#delete folder
os.rmdir("myfolder")  