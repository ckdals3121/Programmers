# citations 을 정렬 하고, H 값을 len(citations) - i 로 설정해서 완전탐색 해본다

def solution(citations):
    answer = 0
    citations.sort()
    
    for i in range(len(citations)) :
        H = len(citations) - i
        
        if citations[i] >= H :
            return H
    
    return answer