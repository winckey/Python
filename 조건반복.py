from pickle import FALSE, TRUE

money = 1
#  = TRUE // 0 = FALSE
if money > 1:
    print(">1")
elif money< 0 :
    print("< 0" )
else :
    print("xxxx")
    
    
money = 0
# 1 = TRUE // 0 = FALSE
if money :
    print("t")

else :
    print("f")
    
    
        
    
money = [1, 2, 3]
# 1 = TRUE // 0 = FALSE
if money.count(4) :
    print("t")
    print(money.count(1))

else :
    print("f")
    
money = [1, 2, 3]
# 1 = TRUE // 0 = FALSE
if 5 in money :
    print("money in")

else :
    print("money f")