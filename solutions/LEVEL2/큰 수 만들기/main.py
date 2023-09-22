# 처음부터 순회하면서, 숫자가 커지는 상황에서, 그 수보다 앞에 있는 수 들 중에서, 해당 수보다 작은 수를 다 지운다

def solution(number, k):
    answer = []
    
    for num in number :
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
        
    return ''.join(answer[:len(answer) - k])