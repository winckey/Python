

def solution(money, stocks):
    global stocksR
    global moneyR
    global maxR
    moneyR = 10;
    stocksR = [[1,1] , [3,5] , [3,5] , [4, 9]]
    


    combi(1,[],int(0))
          


    print(maxR)
    answer = 0
    return maxR

def combi(n, ans , sum):
    if moneyR < sum:
        val = int(0)
        ans.pop()
        for i in ans :
            val +=stocksR[i][0];

        if val > max :
            maxR = val
        return;
    ans.append(stocksR[n][0])
    sum += stocksR[n][1]
    
    combi(n + 1, ans , sum)
    
    sum -= stocksR[n][1]
    ans.pop()
    combi(n + 1, ans , sum)
    
solution(0, [])