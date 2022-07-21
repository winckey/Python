

s = "one4seveneight"
dict ={}
en = ['zero' , 'one' , 'two' , 'three' , 'four' ,  'five' , 'six' , 'seven' , 'eight' , 'nine']
    
for i in range(10):
    dict[en[i]] = i

result =""
eng=''
for i,  sp in enumerate(s):
    if sp.isdigit():
        result= result+sp
    elif sp.isalpha():
        eng = eng+sp;
        if(eng in dict):
            result = result+str(dict.get(eng,""))
            eng = ""
            
            
print (result)