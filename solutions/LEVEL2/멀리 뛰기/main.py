# n 칸을 멀리뛰기 하는 경우의 수는, n - 1 번째 칸에서 1칸 뛰는 것과, n - 2 번째 칸에서 2칸 뛰는 것의 합 이기 때문에, dp를 사용한다

def solution(n):
    dp = [0 for _ in range(2001)]
    
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1) :
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567
        
    return dp[n]