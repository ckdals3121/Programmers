# 직사각형의 각 변으로 4개로 나눠준 후, 행렬의 값을 회전시켜 준다

def solution(rows, columns, queries):
    answer = []
    matrix = []
    for i in range(rows) :
        matrix.append([x for x in range(i * columns + 1, (i + 1) * columns + 1)])
        
    for query in queries :
        query = [x - 1 for x in query]
        temp = matrix[query[0]][query[1]]
        small = temp
        
        for i in range(query[0] + 1, query[2] + 1) :
            matrix[i - 1][query[1]] = matrix[i][query[1]]
            small = min(small, matrix[i][query[1]])
        for i in range(query[1] + 1, query[3] + 1) :
            matrix[query[2]][i - 1] = matrix[query[2]][i]
            small = min(small, matrix[query[2]][i])
        for i in range(query[2] - 1, query[0] - 1, -1) :
            matrix[i + 1][query[3]] = matrix[i][query[3]]
            small = min(small, matrix[i][query[3]])
        for i in range(query[3] - 1, query[1] - 1, -1) :
            matrix[query[0]][i + 1] = matrix[query[0]][i]
            small = min(small, matrix[query[0]][i])
        matrix[query[0]][query[1] + 1] = temp
        
        answer.append(small)
        
    return answer