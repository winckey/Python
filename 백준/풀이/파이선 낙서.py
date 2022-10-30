# raw = "Doctor Zhivago"
# arranged = sorted(raw)
# print(arranged)

# a = [7, 2, 3]
# b = [4, 5, 6]
# print(min(a, b))   # 반환 : [1,2,3]

# g = [[1,-1,123123],[99,3],[99,1],[5,6],[7,8],[9,11]]

# print(sorted(g))
# dicts = {"a":5, "b":2, "c":3} 
# print(sorted(dicts.values()))

# # print(min(g , key=lambda x : x[1]))

# dic = {'pop': 3100, 'classic': 1450, 'trot':620}

# # key 값을 기준으로 오름차순 정렬하여 리스트 출력
# print(sorted(dic))
# # key 값을 기준으로 내림차순 정렬한 리스트 출력 
# print(sorted(dic, reverse=True))

# print(sorted(dic.items()))

# # key 값을 기준을 정렬된 딕셔너리 생성 
# dic = dict(sorted(dic.items()))
# print(dic)

# print(sorted(dic.items(), key=lambda x:x[1]))
# # 위 값을 딕셔너리로 변환
# print(dict(sorted(dic.items(), key=lambda x:x[1])))
# # value 값을 기준으로 오름차순 정렬
# print(sorted(dic,key=lambda x:dic[x]))

# a = [(1, -1), (1, 2), (2, 2), (3, 3), (0, 4)]

# print(sorted(a , key = lambda x : (x[1] , -x[0]) ))


a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
if ('name','pey') in a.items():
    print('포함')
else:
    print('미포함')



# data ={'pop': 3100, 'classic': 1450, 'trot':620}
# result = list(permutations(data.values(), 2)) # 데이터중 3개를 뽑아 나열(순열)
# print(result) 

# => [('A', 'B' ,'C'),('A', 'C', 'B'), ,,,,,,,, , ('C', 'B', 'A')]

# print(sum(dicts.values()))

# print((max(dicts, key=dicts.get))) #a
# print((min(dicts, key=dicts.get))) #c

# print("dicts의 최소 값 구하기: {}".format(min(dicts))) 

# print("dicts의 최소 값 구하기: {}".format(min(dicts.values()))) 
 

# print("dits의 최소 값을 가지는 key 구하기: {}".format(min(dicts, key=dicts.get)))