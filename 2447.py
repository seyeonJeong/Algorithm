n = int(input())



def make_star(num):
    arr = []
    if num == 1:
        return ['*']
    star = make_star(num//3)
    for i in star:
        arr.append(i * 3)
    for i in star:
        arr.append(i + ' ' *(num//3) + i)
    for i in star:
        arr.append(i * 3)

    return arr

for i in make_star(n):
    print(i)