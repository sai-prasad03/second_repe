# print the part of the string where there was a match
#Que:- The reguler expression looks for any words that starts with an upper case 'S'

import re

a = "The rain in Spain"
x = re.search(r"\bS\w+",a)
print(x.group())