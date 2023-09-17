# 왼쪽부터 값을 pop 해서, 처음으로 값보다 작은 값이 나올 때 까지 count += 1 한다

from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices :
        temp = prices.popleft()

        count = 0
        for price in prices :
            if temp > price :
                count += 1
                break
            count += 1

        answer.append(count)

    return answer