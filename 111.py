import re
line=open(r'"C:\Users\Nicks901\PycharmProjects\untitled4\mmmm"r')

mat = re.search(r'(.*) are (.*) is (.*) .*', line, re.M|re.I)

if mat:
   print("matchObj.group() : ", mat.group())

   
else:
   print("No match!!")



