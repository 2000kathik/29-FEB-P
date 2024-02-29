# import re
# url = input("URL: ").strip()

# matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
# if matches:
#     print(f"username:", matches.group())
    
import re

url = input("URL: ").strip()  # Prompt the user to input a URL and remove leading/trailing whitespaces

matches = re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
# The regular expression pattern: ^https?://(?:www\.)?twitter\.com/(.+)$
# - ^https?://: Start of the string, followed by "http://" or "https://"
# - (?:www\.)?: Optional non-capturing group for "www."
# - twitter\.com/: Literal "twitter.com/"
# - (.+)$: Capturing group for the username, followed by the end of the string

if matches:
    print(f"username:", matches.group(1))