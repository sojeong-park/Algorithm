# 문자열 재정렬 - 주어진 알파벳을 오름차순으로 정렬 후 숫자(숫자는 0~9의 정수만 주어진다)의 합을 이어서 출력한다.
# K1KA5CB7 -> ABCKK13

n = input()
alpa = []
sum = 0

for i in n:
    if i.isalpha():
        alpa.append(i)
    else:
        sum += int(i)

alpa.sort()

# 출력방법1
for i in alpa:
    print(i, end='')
print(sum)

#출력 방법2
if sum != 0:
    alpa.append(str(sum))

print(''.join(alpa))
