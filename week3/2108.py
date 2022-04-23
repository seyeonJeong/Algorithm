import sys
from collections import Counter

n = int(sys.stdin.readline())
list_num = []
for i in range(n):
    list_num.append(int(sys.stdin.readline()))
list_num.sort()
list_num_c = Counter(list_num).most_common()
print(round(sum(list_num)/n))
print(list_num[n//2])
if len(list_num_c) > 1:
    if list_num_c[0][1] == list_num_c[1][1]: #최빈 count가 같으면 두번째로 작은 수 출력
        print(list_num_c[1][0])
    else:
        print(list_num_c[0][0])
else:
    print(list_num_c[0][0])
print(list_num[-1] - list_num[0])