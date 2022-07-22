def solution(numbers, target):
    
    graph = [True for i in range(5)]
    print(graph)
    
    
    answer = 0
    return answer

def dfs_recursive(graph, start, visited = []):
    ## 데이터를 추가하는 명령어 / 재귀가 이루어짐 
    visited.append(start)
 
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited