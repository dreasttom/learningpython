# This is VERY rudimentary. Not even a fully working program. Rather just
# examples of how regular expressions are used.

import re

# Sample text
text = "My phone number is 123-456-7890 and my email is chuck@chuckeasttom.com"

# Find phone number using regular expression
phone_pattern = r"\d{3}-\d{3}-\d{4}"
phone_number = re.findall(phone_pattern, text)

# Find email address using regular expression
email_pattern = r"\S+@\S+"
email_address = re.findall(email_pattern, text)


print("Phone number:", phone_number)
print("Email address:", email_address)
