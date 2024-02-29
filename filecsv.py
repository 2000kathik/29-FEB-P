with open ("file.csv") as file:
# Iterate over each line in the file
    for line in file:
 # Remove trailing newline characters and split the line into fields using a comma as the delimiter
        row = line . rstrip().split(",")
# Print information based on the first and second elements of the row
        print(f"{row[0]} is in {row[1]}")
        # name, space, house=line.rstrip().split(",")
        # print (f"{name} is in {house} is in {space}")