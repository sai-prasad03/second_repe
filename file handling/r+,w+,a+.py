# r+ = in this mode first file will be read and then it writen

# f = open('student.txt','r+')
# data = f.read()
# print(f.tell())
# print(data)
# f.write('\n how are you')
# print(f.tell())
# f.close()

# w+ mode = in this mode first file will be writen and after that its available for reading mode
# in write mode the present data will be over ride

# f= open('student.txt','w+')
# f.write('welcome to python')
# f.seek(0)
# data = f.read()
#print(data)
#f.close()

# a+ mode = in this mode first file will be writen and then readable
# but in this data won't be over ride
# this is same as w+

f = open('student.txt','a+')
f.write('\ntrader')
f.seek(0)
data =f.read()
print(data)
f.close()
