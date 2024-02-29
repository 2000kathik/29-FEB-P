# Create an empty list to store dictionaries containing 'name' and 'home' information
import csv
# Open the CSV file using a context manager
files=[]
with open("file.csv") as file:
# Create a CSV reader object
    reader=csv.reader(file)
# Iterate over each row in the CSV file
    for name, home in reader:
# Append a dictionary to the 'files' list containing 'name' and 'home' information
        files.append({"name":name ,"home":home})
# Sort the list of dictionaries based on the 'name' field
# The lambda function specifies the key for sorting
for file in sorted(files, key=lambda file:file["name"]):
# Print information for each file (name and home)
    print(f"{file['name']} is in {file['home']}")