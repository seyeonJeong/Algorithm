
#2750과 비슷한데 내장된 정렬 함수를 이용하여 빠르게 풀 수 있다.
n = int(input())

list_num = []
for i in range(n):
    list_num.append(int(input()))

list_num.sort()

for i in list_num:
    print(i)