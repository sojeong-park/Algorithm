s1 = ["h", "e", "l", "l", "o"]
s2 = ["H", "a", "n", "n", "a", "h"]


a = s2

i=0
end_index = len(a)-1
while len(a) < 0:
    start = a.pop(0)
    end = a.pop()
    s2[i] = end
    s2[end_index] = start
    i+=1
    end_index -= 1

print(s2)