# 공백으로 split 후 list로 변환해서 max, min 사용

def solution(s):
    answer = ''
    ls = list(map(int, s.split()))

    answer += str(min(ls))
    answer += " "
    answer += str(max(ls))
    return answer