# 뒤에서부터 처음 나온 '0'을 '1'로 바꾸고, 그 뒤의 '1'을 '0'으로 변경한다

def fx(number) :
    if number % 2 == 0 :
        return number + 1
    
    binary = list(format(number, 'b'))
    binary.insert(0, '0')
    
    idx = len(binary) - 1
    while True :
        if binary[idx] == '0' :
            binary[idx] = '1'
            binary[idx + 1] = '0'
            return int(''.join(map(str,binary)), 2)
        idx -= 1

def solution(numbers):
    answer = []
    for number in numbers :
        answer.append(fx(number))
    return answer