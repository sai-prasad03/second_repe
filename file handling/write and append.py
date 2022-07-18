# in write mode file will be created and we can write in file
#but when next time when we open file and write something the data will be overwtie
#when we use append mode file also created but data will not be overwrite


f = open('rudra.txt','a')
n = f.write('\nhello')
print(n)
f.close()