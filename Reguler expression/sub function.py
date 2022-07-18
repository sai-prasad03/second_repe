# the sub function replace the matches with the text of your choice
# example
# replace every white space character with number 9

import re
a = "The rain in spain"
x = re.sub(r"\s","9",a)
print(x)

# NOTE = you can control the no.of replacement by specifying the count parameter
# replace the first 2 occurrance

a = "The rain in spain"
x = re.sub(r"\s","9",a,2)
print(x)
