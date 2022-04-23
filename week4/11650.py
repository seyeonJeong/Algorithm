
import sys

n = int(sys.stdin.readline())
list_num = []

for i in range(n):
    x,y = map(int, input().split())
    list_num.append((x,y))

list_num.sort()
for i in range(n):
    print(list_num[i][0], list_num[i][1])