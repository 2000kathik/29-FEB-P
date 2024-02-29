# name=input("your name please :")
with open("file1.txt","r") as file:
    # file.write(f"{name}\n")
# This block reads lines from the file and prints a greeting message for each line
    for line in file:
        print("hello," , line.rstrip())