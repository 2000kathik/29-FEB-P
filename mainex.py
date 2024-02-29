import re
 # Replace this with the actual email address
email = input("URL: ").strip()

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
is_valid = re.match(pattern, email)

if is_valid:
    print("Valid email address")
else:
    print("Invalid email address")