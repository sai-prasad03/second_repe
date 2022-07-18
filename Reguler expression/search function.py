import re
a = "The rain in Spain"
x = re.search("\s",a)
print("the first white space character is located in position",x.start())

# note = if no matches are found the value none is returned