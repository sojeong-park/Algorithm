# https://www.acmicpc.net/problem/16916

# s = input()
# x = input()
#
# x_len = len(x)

# 시간초과 o(n)
def solution(s, x, x_len):
    if len(s) == x_len and s == x:
        return 1
    for i in range(len(s)-x_len):
        # print(i, i + x_len, s[i:i+x_len])
        if s[i:i+x_len] == x:
            return 1
    return 0

# print(solution(s,x,x_len))

# 시간초과
def solution2(s, x, x_len):
    if len(s) == x_len and s == x:
        return 1
    s_size = len(s)
    for i in range((s_size//2)-1):
        if s[i:i+x_len] == x:
            return 1
        b_index = x_len + i
        if s[-b_index:s_size-i] == x:
            return 1
    return 0

# print(solution2(s,x,x_len))

# KMP 활용한 풀이

def make_table(pattern):
    length = len(pattern)
    table = [0] * length
    j = 0

    for i in range(1, length):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

    return table


def kmp(parent, pattern):
    table = make_table(pattern)
    print(table)
    parent_length = len(parent)
    pattern_length = len(pattern)

    j = 0
    for i in range(parent_length):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j - 1]

        if parent[i] == pattern[j]:
            if j == pattern_length - 1:
                return 1
            else:
                j += 1

    return 0


parent = input()
pattern = input()
print(kmp(parent, pattern))