# 순간이동을 최대한 많이 활용해야 하며, 도착지점에서 시작해서 끝지점으로 간다고 생각한다.

def solution(n):
    ans = 0
    
    while n != 0  :
        if n % 2 == 0 :
            n /= 2
        else :
            ans += 1
            n -= 1

    return ans