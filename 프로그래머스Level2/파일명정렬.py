import re

def solution(files):
    answer = []
    for file in files:
        head, number, tail = '', '', ''
        number_flag = False
        for i in range(len(file)):
            if file[i].isdigit():
                number += file[i]
                number_flag = True
            elif not number_flag:
                head += file[i]
            else:
                tail = file[i:]
                break
        answer.append((head, number,tail))
    answer.sort(key=lambda x:(x[0].upper(), int(x[1])))
    return [''.join(t) for t in answer]

# solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])


def solution2(files):
    temp = [re.split(r"([0-9]+)", s) for s in files]
    print(temp)
    sort = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])))

    return [''.join(s) for s in sort]

solution2(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
