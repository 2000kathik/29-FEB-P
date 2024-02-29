import csv
name=input("what is your name : ")
home=input("what is your home : ")
# Open the CSV file in append mode using a context manager
with open("file.csv","a") as file:
    # writer=csv.writer(file)
    # writer.writerow([name,home])
# Create a DictWriter object specifying the fieldnames and the file
    Writer=csv.DictWriter(file,fieldnames=["name","home"])
 # Write a new row to the CSV file using the user input
    Writer.writerow({"name":name, "home":home})