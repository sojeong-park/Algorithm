# 간단한 구현문제

n = int(input())
maxNum = -1e9
for i in range(n):
    nums = input().split(' ')
    a, b, c = nums[0], nums[1], nums[2]
    total = 0
    if a==b and b==c: # 세개가 같은경우
        total = 10000+(int(a)*1000)
    elif a==b or a==c:
        total = 1000+(int(a)*100)
    elif b == c:
        total = 1000 + (int(b) * 100)
    else:
        total= max(int(a),int(b), int(c)) * 100
    maxNum = max(maxNum, total)

print(maxNum)