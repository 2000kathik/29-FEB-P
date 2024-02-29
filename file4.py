# Create an empty list to store lines from the file
file4=[]
# Open the file named "file1.txt" using a context manager
with open ("file1.txt") as file:
# Iterate over each line in the file
    for line in file:
    # Remove trailing newline characters and append the line to the 'file4' list
        file4.append(line.rstrip())
# Sort the list of lines in reverse order
for file in sorted(file4, reverse=True):
    # Print a greeting message for each line
    print(f"hello,{file}")