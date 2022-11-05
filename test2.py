import re


set_value = "2 * 2 +"
last_digits = re.search(r'\d+$', set_value)

print()