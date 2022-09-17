
from itertools import permutations

def solution(ability):
    answer = 0
    student_cnt = len(ability) # 학생 수
    event_cnt = len(ability[0]) # 종목 수

    students = [i for i in range(student_cnt)]
    for perm in list(permutations(students, event_cnt)):
        temp = 0
        for i, p in enumerate(perm):
            temp += ability[p][i]
        if temp > answer:
            answer = temp
    return answer


test = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]
print(solution(test))