#tell = in that tell() we get the pointer position of cursel, default it is zero unless and until we change that
# i.e we change the position of pointer by using seek() method
# by using seek() method we can change the position of pointer
# example shown in below



f = open('rudra1.txt','r')
print(f.tell())
f.seek(6)
print(f.tell())
f.seek(2)
print(f.tell())
print(f.read())
f.close()