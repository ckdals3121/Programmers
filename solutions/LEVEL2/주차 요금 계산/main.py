# record 단위로 뽑아 내서, 입차면 추가를 하고, 출차면 입차에서 기록을 불러와서 주차 시간을 계산함

import math

def time_difference(time2, time1) :
    h1, m1 = map(int, time1.split(':'))
    h2, m2 = map(int, time2.split(':'))
    
    diff = (h2 * 60 + m2) - (h1 * 60 + m1)
    return diff

def solution(fees, records):
    answer = []
    
    in_car = {}
    parking_time = {}
    
    for record in records :
        time, number, t = map(str, record.split())
        
        if t == "IN" :
            in_car[number] = time
        else :
            if number in list(parking_time.keys()) :
                parking_time[number] += time_difference(time, in_car[number])
            else :
                parking_time[number] = time_difference(time, in_car[number])
            del in_car[number]
    
    for car in list(in_car.keys()) :
        if car in list(parking_time.keys()) :
            parking_time[car] += time_difference("23:59", in_car[car])
        else :
            parking_time[car] = time_difference("23:59", in_car[car])
    
    car_numbers = list(parking_time.keys())
    car_numbers.sort()
    
    for number in car_numbers :
        if parking_time[number] > fees[0] :
            fee = fees[1] + math.ceil((parking_time[number] - fees[0]) / fees[2]) * fees[3]
        else :
            fee = fees[1]
        answer.append(fee)
    
    return answer