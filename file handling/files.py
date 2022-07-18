f = open("student.txt","w")
f. write("hello\n")
f.write("saiprasad\n")
f.write("how are you")
f.close()
print("writting success")

f = open("student.txt","r")
data =f.read()
print(data)
f.close()

f = open("student.txt","rb")
data = f.read()
print(data)
f.close