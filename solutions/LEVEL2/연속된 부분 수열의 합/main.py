# 투포인터로 푼다

def solution(sequence, k):
    answer = []
    right = 0
    count = 0    
    
    for left in range(len(sequence)) :
        while right < len(sequence) and count < k :
            count += sequence[right]
            right += 1
        
        if count == k:
            if not answer:
                answer = [left, right-1]
            else:
                if answer[1] - answer[0] > right - left - 1 :
                    answer = [left, right - 1]
        
        count -= sequence[left]

    return answer