import sys

n = int(sys.stdin.readline())
list_num = []
for i in range(n):
    list_num.append(list(map(int, input().split())))

def gcd(x,y):
    while(1):
        r = x%y
        if(r == 0):
            break
        x = y
        y = r
    return y

def lcm(x,y):
    result = (x*y)//gcd(x,y)
    return result

for i in range(n):
    print(lcm(list_num[i][0],list_num[i][1]))