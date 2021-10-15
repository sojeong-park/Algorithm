# https://www.acmicpc.net/problem/1062
from itertools import combinations

n, k = map(int, input().split())

words = []
for i in range(n):
    words.append(input().lstrip('anta').rstrip('tica'))

alpa = set()
fixed_words = ['a','c','i','n','t']
for word in words:
    for char in word:
        if char not in fixed_words:
            alpa.add(char)

comb_list = list(combinations(alpa, k-5))

max_cnt = 0
for i in range(len(comb_list)):
    learn_char = list(comb_list[i]) + fixed_words # 학습한 단어


print(words)
print(alpa)

print(list(combinations(alpa, k-5)))