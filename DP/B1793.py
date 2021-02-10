# 타일링
# https://www.acmicpc.net/problem/1793
d = [0] * 251
# 2x0 직사각형을 채우는 방법의 수는 1가지. "아무것도 안 하는 것"을 하나의 방법으로 센다.
d[0] = 1
d[1] = 1
d[2] = 3

for i in range(3, 251):
    d[i] = d[i-1] + (d[i-2] * 2)

while True:
    try: n = int(input())
    except: break
    print(d[n])