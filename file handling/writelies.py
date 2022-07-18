# this method is used for to store a multiple string e.g list,tuple,set etc

f = open('rudra1.txt','w')
list = ['sai ','rudra ','samarth ','siddharth ']
f.writelines(list)
f.close()
print("file create successfully")