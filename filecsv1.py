# Create an empty list to store dictionaries containing 'name' and 'house' information
file1=[]
# Open the CSV file using a context manager
with open("file.csv") as file:
 # Iterate over each line in the file
    for line in file:
# Remove trailing newline characters and split the line into 'name' and 'house' using comma as a delimiter
        name, house=line.rstrip().split(",")
    # Create a dictionary with 'name' and 'house' information and append it to the 'file1' list
        files={"name":name, "house":house}
        file1.append(files)
# def get_name(files):
#     return files["name"]
#for files in sorted(file1, key=get_name , reverse=get_name):
# Sort the list of dictionaries based on the 'name' field
# The lambda function specifies the key for sorting
for files in sorted(file1, key=lambda files:files["name"]):
# Print information for each file (name and house)
    print(f"{files['name']} is in {files['house']}")