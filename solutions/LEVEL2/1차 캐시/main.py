# cacheSize 가 0 인 경우에 주의한다.
# LRU list 를 활용해서, cache[i] 의 값이 마지막으로 사용된 idx 값을 LRU[i] 에 저장한다.
# cache miss 가 나고, cache 가 꽉 차 있을때, LRU 값 중 가장 작은 값을 가진 cache 데이터를 삭제한 후, 새 값을 넣는다

def solution(cacheSize, cities):
    answer = 0
    cache = []
    LRU = [0 for _ in range(cacheSize)] 
    
    if cacheSize == 0 :
        return 5 * len(cities)
    
    for i in range(len(cities)) :
        cities[i] = cities[i].lower()
    
    for idx, city in enumerate(cities) :
        if city in cache :
            answer += 1
            LRU[cache.index(city)] = idx
        else :
            if len(cache) < cacheSize :
                answer += 5
                cache.append(city)
                LRU[cache.index(city)] = idx
            else :
                answer += 5
                index = LRU.index(min(LRU))
                cache[index] = city
                LRU[index] = idx
                
    return answer