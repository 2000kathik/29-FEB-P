# a|b => either A or B
# *(...) => a group
# (?:...) => non-capturing version
# using "?"
# REGULAR LIBRARY;
#  re.IGNORECASE
#  re.MULTILINE
#  re.DOTALL

# there will be getting small wrong output below program

import re

name =input("what's your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")