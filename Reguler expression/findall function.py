# the findall function returns a list containing all matches

import re
a = "The rain in spain"
x = re.findall(r"ai",a)
print(x)

# the list contains the matches in the order they are found
# if no matches are found an empty list is returned

#example
import re
a = "The rain in spain"
x = re.findall(r"portugal",a)
print(x)