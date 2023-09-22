# permutations 로 가능한 경우의 수를 모두 구하고, 각각에 대해서 소수인지 판별하다

from itertools import permutations

def is_prime_number(x):
    if x == 1 or x == 0:
        return False
    for i in range(2, int(x ** 0.5) + 1) :
        if x % i == 0 :
            return False 
    return True 

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    primes = []
    
    for i in range(1, len(numbers) + 1) :
        nums = list(permutations(numbers, i))
        for num in nums :
            if is_prime_number(int(''.join(map(str, num)))) and int(''.join(map(str, num))) not in primes :
                answer += 1
                primes.append(int(''.join(map(str, num))))
        
    return answer