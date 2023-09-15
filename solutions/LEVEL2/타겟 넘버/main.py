# 모든 수가 양수일 때의 합과 target 수를 알면, negative가 되어야 하는 수의 합들에 대해 구할 수 있다. 
# 그런다음, combinations 으로 1개, 2개, 3개 ... 으로 구하고 나서, 각각의 경우에서의 합을 구하고, 그게 negative가 되어야 하는 수의 합과 같은지 비교한다

from itertools import combinations

def solution(numbers, target):
    answer = 0
    
    all_positive = sum(numbers)
    if (all_positive - target) % 2 != 0 :
        return 0
    negative = (all_positive - target) // 2
    
    if all_positive == target :
        return 1
    
    for i in range(1, len(numbers) + 1) :
        temps = list(combinations(numbers, i))
        
        for temp in temps :
            if sum(temp) == negative :
                answer += 1
    
    return answer