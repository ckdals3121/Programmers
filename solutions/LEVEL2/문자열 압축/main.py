# 완전탐색으로 문자열을 i개 만큼씩 잘라서 같은게 있는지 찾는 식으로 진행한다

def solution(s) :
    if len(s) == 1 :
        return 1
    
    result = []

    for i in range(1, len(s) // 2 + 1) :
        b = ''
        cnt = 1
        temp = s[:i]

        for j in range(i, len(s), i) :
            if temp == s[j: j + i] :
                cnt += 1
            else :
                if cnt != 1 :
                    b += str(cnt) + temp
                else :
                    b += temp
                temp = s[j: j + i]
                cnt = 1
        
        if cnt != 1 :
            b += str(cnt) + temp
        else :
            b += temp

        result.append(len(b))
    
    return min(result)