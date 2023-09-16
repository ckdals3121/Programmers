# DP 를 활용한 풀이이며, 각각의 값을 가능한 최대값으로 업데이트한다

def solution(land):
    for i in range(1, len(land)) :
        for j in range(4) :
            x, y, z = [temp for temp in range(4) if temp != j]
            land[i][j] += max(land[i - 1][x], land[i - 1][y], land[i - 1][z])
            
    return max(land[-1])