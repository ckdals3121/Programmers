# NUMBER 부분 (숫자로만 이루어진 부분) 을 기준으로 split 해서 HEAD, NUMBER 로 나눈후 sort 한다

import re
def solution(files):
    temp = [re.split(r"([0-9]+)", s) for s in files]
    
    sort = sorted(temp, key = lambda x: (x[0].lower(), int(x[1])))
    
    return [''.join(s) for s in sort]