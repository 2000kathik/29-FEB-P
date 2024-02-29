#the user for their name
name=input("your name please :")
#file=open("file.txt","w")
# Open the file named "file.txt" in append mode using a context manager
file=open("file.txt","a")
#file.write(name)
# Write the user's name followed by a newline character to the file
file.write(f"{name}\n")
# The file is automatically closed when the block is exited
file.close()
 