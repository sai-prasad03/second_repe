# the split function returns a list where the string has been split at each match
#example
#split at each white space character

import re
a = "The rain in spain"
x = re.split(r"\s",a)
print(x)

#NOTE = you can control the no.occurrance by specifying the using maxsplit parameter
import re
a = "The rain in spain"
x = re.split(r"\s",a,1)
print(x)

