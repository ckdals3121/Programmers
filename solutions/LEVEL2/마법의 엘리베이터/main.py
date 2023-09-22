# 1의 자리수 부터 비교하면서 5보다 크면 10으로 보내고, 5보다 작으면 0으로 보내고, 5랑 같으면 그 다음 자리수가 5 이상일 때 10으로 만드는 식으로 진행한다

def solution(storey):
    answer = 0
    
    while storey != 0 :
        mod = storey % 10
        
        if mod > 5 :
            answer += (10 - mod)
            storey += 10
        elif mod < 5 :
            answer += (mod)
        else :
            if (storey // 10) % 10 >= 5 :
                storey += 10
            answer += mod

        storey //= 10
                
    return answer