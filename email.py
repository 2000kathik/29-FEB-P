import re import search

email = input("what's your email? ").strip()

if re.search(".+@.+", email):
    print("valid")
else:
    print("Inavlid")