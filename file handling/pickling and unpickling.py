# pickeling is used for to convert class in to binary file or to store a data from class
# pickling means storing object in the file
# unpickling is opposite pickling its convert from files to class
# unpickling means reading object from the file


import pickle
class Student:
    def __init__(self,name,roll_no,address):
        self.name = name
        self.roll_no = roll_no
        self.address = address

    def disp(self):
        print(f'name:{self.name} roll_no:{self.roll_no} address:{self.address}')
n = int(input('enter the number of student:-'))
with open('sai.dat','wb') as f:
    for i in range (n):
        name = input('enter student name:-')
        roll_no = int(input('enter student roll no:-'))
        address = input('enter student address:-')
        stu = Student(name,roll_no,address)
        pickle.dump(stu,f)
print('pickling done')

with open('sai.dat','rb') as f:
    while True:
        try:
            obj = pickle.load(f)
            obj.disp()
            print('unpickling done')

        except EOFError:
            print('done')
            break