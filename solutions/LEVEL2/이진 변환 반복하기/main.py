# s에서 0의 개수를 계속 추가 하고, s 를 0을 없앤 string으로 업데이트 한 후, 길이를 2진수로 변경

def solution(s):
    answer = [0 for _ in range(2)]
    
    while len(s) != 1 :
        answer[1] += s.count('0')
        
        s = format(s.count('1'), 'b')
        answer[0] += 1
    
    return answer