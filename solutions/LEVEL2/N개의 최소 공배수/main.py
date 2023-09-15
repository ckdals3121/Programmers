# gcd를 통해서 lcm 을 구하고, 그 lcm 과 그 다음 arr 수의 lcm 을 구해서 업데이트 한다.

def gcd(x, y) :
    while y :
        x, y = y, x % y
    return x

def lcm(x, y) :
    return (x * y) // gcd(x, y)

def solution(arr):
    answer = arr[0]
    
    for i in range(1, len(arr)) :
        answer = lcm(answer, arr[i])

    return answer