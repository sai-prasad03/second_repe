# print the string passed in to the function
import re
a = "The rain in Spain"
x = re.search(r"\bS\w+",a)
print(x.string)