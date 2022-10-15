from collections import defaultdict
from unittest import result

sourece = "execute"
a = ""
b = ""


dest =""

    
while sourece != "" :     
    for i in sourece :
        if i in a :
            b= b+i
        else :
            a= a+i
    sourece = b
    dest =dest + "".join(sorted(a))
    a =""
    b =""            
        

        
print(dest)            