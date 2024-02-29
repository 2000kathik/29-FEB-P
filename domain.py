# email = input("what's your email? ").strip()
# username,domain=email.split("@")
# if username and domain.endswith(".com"):
#     print("valid")
# else:
#     print("Invalid")
# Prompt the user to enter their em
email = input("what's your email? ").strip()
 # Check if the email contains "@" and at least one dot "."
if "@" in email and "." in email:
    print("valid")
else:
# Print "Invalid" if the email is missing "@" or a dot "."
    print("Invalid")