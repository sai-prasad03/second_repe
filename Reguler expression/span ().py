# print the position (start and end position) of the first match occurrence
# the reguler expression looks for any words that start with upper case S

import re
a = "The rain in Spain"
x = re.search(r"\bS\w+",a)
print(x.span())

