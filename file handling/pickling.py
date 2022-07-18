import pickle
class Teacher:

	def __init__(self,name,roll_no,address):
		self.name = name
		self.roll_no = roll_no
		self.address = address

	def disp(self):
		print(f'name:{self.name} roll_no:{self.roll_no} address:{self.address}')

n = int(input('enter the number of teacher:-'))
with open('rudra.dat','wb') as f:
	for i in range(n):
		name = input('enter the name of teaher:-')
		roll_no = int(input('enter the roll no:-'))
		address = input('enter the address:-')
		tea = Teacher(name,roll_no,address)
		pickle.dump(tea,f)

print('pickling done')

with open('rudra.dat','rb') as f:
	while True:
		try:
			obj = pickle.load(f)
			obj.disp()
			print('unpickling done')

		except EOFError:
			print('done')
			break

