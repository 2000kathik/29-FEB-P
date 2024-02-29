# Create an empty list to store lines from the file
file3=[]
# Open the file named "file1.txt" using a context manager
with open("file1.txt") as file:
# Iterate over each line in the file
    for line in file:
 # Remove trailing newline characters and append the line to the 'file3' list
        file3.append(line.rstrip())
# Sort the list of lines in ascending order
for file in sorted(file3):
# Print a greeting message for each line
    print(f"hello,{file}")
#     for line in sorted(file):
#         print("hello ," ,line.rstrip())