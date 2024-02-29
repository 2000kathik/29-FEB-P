# [] => set of characters
# [^] => complementing the set
# \d => decimal digit
# \D => not a decimal digit 
# \s => whitespace character
# \S => not awhitespace character
# \w => word character............ as well as numbers and the underscore
# \W => not a word character

import re

email = input("what's your email? ").strip()
if re.search(r"^\w+@\w+\.edu$", email):
    print("valid")
else:
    print("Inavlid")