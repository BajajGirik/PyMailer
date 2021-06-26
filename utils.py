import os
import re

# function to check for valid mail 
def checkEmail(Receiver_email):
    Emailregex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    Receiver_email.lower()
    if re.search(Emailregex, Receiver_email):
        return True
    return False

# function to find file paths 
def findFiles(filename, startPath = os.path.abspath(os.sep)):
   res = []
   if not filename:
       return False

   # walking top-down from the startPath  
   for root, dirs, files in os.walk(startPath):

      # this is for not entering mac's read-only folder 
      dirs[:] = [d for d in dirs if d not in "System"]
      if filename in files:
         res.append(os.path.join(root, filename))

   index = selectFiles(res)
   if index < 0:
       return False

   fileDetails = readFile(res[index])
   return fileDetails

def selectFiles(res):
    length = len(res)
    flag = 0

    if length == 0:
        print("No file found")
        flag = -1

    elif length == 1:
        print("File Found")
    else:
        print("Multiple Files found")
        flag = 1

    for i in range(1,length+1):
        print(f"{i}) {res[i-1]}")

    if flag == 1:
        flag = int(input("Enter the file number you want to select: "))
        flag -= 1

    return flag


def readFile(file):
    f = open(file, 'rb')
    f_data = f.read()
    f_subtype = fileSubType(f.name)
    f_maintype = fileMainType(f_subtype)
    arr = [f_data, f_maintype, f_subtype]
    return arr
    
def fileSubType(name):
    i = -1
    s=''
    while name[i] != '.':
        s += name[i]
        i -= 1

    s.lower()
    return s[::-1]

def fileMainType(subtype):
    txt = ['txt','html']
    img = ['jpeg','jpg','png']
    vid = ['mp4','mkv']

    if subtype in img:
        return 'image'

    if subtype in vid:
        return'video' 

    if subtype in txt:
        return 'text'

    return 'application'    