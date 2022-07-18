# this method is used for weather the file is present or not
# for that purpose we have to import os
#to check the file by using isfile() statement
#example show in below


import os
if os.path.isfile('rudra.txt'):
    print("file opened")

else:
    print("file Not Found")