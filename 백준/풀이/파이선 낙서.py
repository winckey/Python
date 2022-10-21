# raw = "Doctor Zhivago"
# arranged = sorted(raw)
# print(arranged)

# a = [7, 2, 3]
# b = [4, 5, 6]
# print(min(a, b))   # 반환 : [1,2,3]

g = [[1,-1,123123],[2,3],[3,4],[5,6],[7,8],[9,11]]

print(min(g , key=lambda x : x[1]))


dicts = {"a":5, "b":2, "c":3} 

print(sum(dicts.values()))

# print((max(dicts, key=dicts.get))) #a
# print((min(dicts, key=dicts.get))) #c

# print("dicts의 최소 값 구하기: {}".format(min(dicts))) 

# print("dicts의 최소 값 구하기: {}".format(min(dicts.values()))) 
 

# print("dits의 최소 값을 가지는 key 구하기: {}".format(min(dicts, key=dicts.get)))