# 인접행렬
INF = 999999999 # 무한의 비용선언

# 2차원 리스트를 이용해 인접 행렬 표현
gragh = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]

# 인접리스트 표현
graghList = [[] for _ in range(3)] # row가 3개인 2차원 리스트로 인접 리스트 표현
graghList[0].append((1,7))
graghList[0].append((2,5))

graghList[1].append((0,7))

graghList[2].append((0,5))

print(graghList)