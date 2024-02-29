# Create an empty list to store names
names=[]
# Use a loop to get names from the user and append them to the list
for _ in range(3):
    names.append(input("your name plz :"))
# Use the sorted() function to sort the names alphabetically
# Iterate over the sorted names and print a greeting for each name
for name in sorted(names):
    print(f"hello,{name}")