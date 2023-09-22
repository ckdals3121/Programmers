# 예약 시간을 분단위로 변경을 해서 sort 해준다
# 그런 다음 예약들을 모두 순회하면서, 방 중에서 손님을 받을 준비가 된 방에 넣거나, 모두 차있으면 새로운 방을 할당한다

def toMinute(min_str) :
    return int(int(min_str.split(":")[0]) * 60 + int(min_str.split(":")[1]))

def solution(book_time):
    book_times = [[toMinute(i[0]), toMinute(i[1]) + 10] for i in book_time]
    book_times = sorted(book_times)

    rooms = []
    for book in book_times :
        if not rooms :
            rooms.append(book)
            continue
        for idx, room in enumerate(rooms) :
            if book[0] >= room[1] :
                rooms[idx] = book
                break
        else :
            rooms.append(book)
    
    return len(rooms)