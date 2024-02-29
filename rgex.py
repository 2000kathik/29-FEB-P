#few important symbols:
# . = any character except a newline
# * = 0 or more repetitions
# + = 1 or more repetitions
# ? = 0 or 1 repetitions
# {m} = m repetitions
# {m,n} = m-n repetitions

import re

email = input("what's your email? ").strip()

if re.search(r".+@.+\.com", email):
    print("valid")
else:
    print("Inavlid")