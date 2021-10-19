# https://www.acmicpc.net/problem/1157

arr = input()
# 312ms 소요
def solution(arr):
    arr_dict = {}
    for char in arr:
        lower_char = char.lower()
        if lower_char not in arr_dict:
            arr_dict[lower_char] = 1
        else:
            arr_dict[lower_char] += 1
    result = list(sorted(arr_dict.items(), key=lambda x : x[1], reverse=True))
    if len(result) > 1 and result[0][1] == result[1][1]:
        return '?'
    return result[0][0].upper()

print(solution(arr))

#128ms 소요
def solution2(arr):
    word = arr.lower()
    word_list = list(set(word))
    cnt = []
    for i in word_list:
        count = word.count(i)
        cnt.append(count)
    if cnt.count(max(cnt)) >= 2:
        print("?")
    else:
        print(word_list[(cnt.index(max(cnt)))].upper())

solution2(arr)
