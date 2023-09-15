# 단어의 첫 글자를 발견하면 대문자로 추가하고, 공백이 나올 때 까지 나머지 부분을 소문자로 추가

def solution(s):
    answer = ''
    idx = 0
    while idx < len(s) :
        if s[idx].isalnum() :
            if s[idx].isalpha() :
                answer += s[idx].upper()
            else :
                answer += s[idx]
            idx += 1
            while idx < len(s) and s[idx].isalnum() :
                answer += s[idx].lower()
                idx += 1
        else :
            answer += s[idx]
            idx += 1
            
    return answer