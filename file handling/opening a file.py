f = open("student.txt","r")
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
