from collections import defaultdict
from unittest import result

sourece = "execute"
a = ""
b = ""

result =""


    
while sourece != "" :     
    for i in sourece :
        if i in a :
            b = b+i
        else :
            a = a+ i
            
    source = b
    result =result+a
    a= ""
    b= ""
  
        
print(result)            