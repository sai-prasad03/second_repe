#this is used in jpg,jpeg format files
# by using this method we can access binary files
# if the file is not present in same directory then we can enter the file path
#python 3.0 not support the uniindeant for that purpose we have to give double backslash \\

f= open("C:\\Users\\SAIRAJ\\Desktop\\download.jpg",'wb')
print("file open successfully")
f.close()