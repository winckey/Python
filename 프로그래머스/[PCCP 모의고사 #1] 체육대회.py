


max = 0


def solution(ability):
    global max
    abilltyG = ability

    visited = [False for i in range(10)]
    dfs(0 , 0 ,ability ,visited)
    return max




def dfs(count , asum ,ability ,visited) :
    global max
    if count >= len(ability[0]) :
        if asum >  max : 
            max = asum
        return

    for i in range(len(ability)) :
        if not visited[i] :
            visited[i] = True
            asum += ability[i][count]
            dfs( count+1 , asum ,ability ,visited)
            asum -= ability[i][count]
            visited[i] = False



test = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]	
print(solution(test))