# phone_number 들로 hashmap 을 만든다
# phone number 들을 순회하면서, 숫자 하나씩을 더하면서, hashmap 을 통해서 이미 존재하는지 확인한다

def solution(phone_book):
    answer = True
    hash = {}
    
    for number in phone_book :
        hash[number] = 1
    
    for number in phone_book :
        temp = ""
        for num in number :
            temp += num
            if temp in hash and temp != number :
                return False
            
    return answer