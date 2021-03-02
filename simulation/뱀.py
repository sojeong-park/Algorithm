# https://www.acmicpc.net/problem/3190
#  왼쪽('L')오른쪽('D') 90도 회전

n = int(input())
m = int(input())
arr = [[0]*n for _ in range(n)]
visits = [[0]*n for _ in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    arr[x][y] = 1

k = int(input())
directions = [] # z 초일때 방향 전환한다.

for i in range(k):
    z, direction = input().split()
    directions.append((int(z),direction))

# 시작은 0,0에서 오른쪽 방향으로 이동.
# 이동하다 directions 배열에 저장된 값과 만나면 방향 전환하여 그 방향으로 이동진행
# 사과를 만나면 꼬리를 만들고
# 사과를 못만나면 꼬리 길이 1로 만들기.
# 범위에서 벗어나거나 자기 꼬리 만나면 끝!
# 한칸 이동하고 끝나는 조건인지 체크.
# 이동할때마다 count 세기
# visits 배열로 방문 가능한지 아닌지 체크. 꼬리를 만났다면 끝내기 용도

d = [(-1,0), (0,1),(1,0),(0,-1)]
def directionChange(count, head):
    for time, direction in directions:
        if count == time:
            if direction == 'L':
                head -= 1
                if head < 0: head = 3
                return head
            else:
                head += 1
                if head > 3: head = 0
                return head
    return head

def solution():
    count = 0
    x = 0
    y = 0
    head = 1 # 오른쪽 방향
    while True:
        if x >= 0 and x < n and y >= 0 and y < n: # x,y가 전부다 범위안에 존재
            x += d[head][0]
            y += d[head][1]
            count += 1
            # 벽에 부딪혔거나 자기 꼬리와 마주쳤거나 하면 break;
            if x+d[head][0] < 0 and x+d[head][0] >= n and y+d[head][1] < 0 and y+d[head][1] >= n:
                break;
            head = directionChange(count, head)
        else:
            break
    return count

print(solution())
