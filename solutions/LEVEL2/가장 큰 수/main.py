# 각 원소를 3번 이어 붙여서 그걸 key로 해서 sort 한다

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x * 3, reverse = True)
    
    for number in numbers :
        answer += number
        
    return str(int(answer))