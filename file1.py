#user for their name
name=input("your name please :")
with open("file1.txt","a") as file:
# Append the entered name followed by a newline to the file
    file.write(f"{name}\n")
#file.close()
 