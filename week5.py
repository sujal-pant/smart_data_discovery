import os
# create a new folder by help of py
os.getcwd();
os.chdir('C:\\Users\Lenovo\Desktop')
a = input("enter foldername:")
os.mkdir(a)
# to open a folder
a="sujal"
flag=0
for b in os.listdir():
    if b==a:
        flag=1
        
if flag==1:
     os.startfile(a)
else:
   print("error")
# folder inside a folder
   os.makedirs
