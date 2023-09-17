# 숫자를 스택에 쌓는데, 쌓기 전에 pop을 하면서 넣을려는 수보다 작은 수가 있으면, answer 값을 업데이트 한다.

def solution(numbers):
    stack = []
    answer = [-1 for _ in range(len(numbers))]
    
    for i in range(len(numbers)) :
        while stack and numbers[stack[-1]] < numbers[i] :
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer