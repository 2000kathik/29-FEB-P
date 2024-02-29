# ^ => matche the start of the string
# $ => matches the end of the string or just before the newline at the end of the string
# to remove "@" not repeating at the excuting time

import re

email = input("what's your email? ").strip()

if re.search(r"^.+@.+\.com$", email):
    print("valid")
else:
    print("Inavlid")