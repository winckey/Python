from itertools import combinations, permutations


def solution(ability):
    n, m = len(ability), len(ability[0])
    stu = list(combinations(range(n), m))
    grade = list(permutations(range(m)))
    max_v = 0
    for i in stu:
        for j in grade:
            temp = 0
            for k in range(m):
                x, y = i[k], j[k]
                temp += ability[x][y]
            max_v = max(max_v, temp)

    return max_v