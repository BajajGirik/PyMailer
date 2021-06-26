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
def find_files(filename, startPath = os.path.abspath(os.sep)):
   res = []

   # walking top-down from the startPath  
   for root, dirs, files in os.walk(startPath):

      # this is for not entering mac's read-only folder 
      dirs[:] = [d for d in dirs if d not in "System"]
      if filename in files:
         res.append(os.path.join(root, filename))

   return res