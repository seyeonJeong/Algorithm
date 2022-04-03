
# 새로 짠 코드 (정답) pypy3에서는 메모리 초과로 뜸
import sys

n = int(sys.stdin.readline()) #파이썬에서 입력값이 클때는 이걸 사용해야함
list_count = [0]*10001 # 1~10000인 수의 범위를 이용한다. 왜인지는 모르지만 이방법이 append를 하는 것 보다 메모리가 절약된다고 함
for _ in range(n):
    list_count[int(sys.stdin.readline())] += 1 # 마찬가지로 sys.stdin.readline()을 사용함

for i in range(10001): # 범위도 10001까지
    if(list_count[i] != 0): # 자잘구레한 배열을 쓰지않고 카운트만 배열에 저장한 후 바로 출력함
        for j in range(list_count[i]):
            print(i)

# 메모리를 생각을 안해봐서 문제 자체는 이해가 갔지만 메모리를 줄이는 방법을 몰랐다. 파이썬에는 내장된 함수를 쓰면 쓸수록 메모리를 적게 쓴다고함
# 그리고 굳이 필요없는 배열을 쓰기보다는 한번에 할 수 있는 코드는 줄이는게 좋을 것 같다.


# 카운팅 정렬의 정의대로 코딩해봄. 답은 맞는데 메모리초과가 계속뜸
# 그래서 구글링 좀 해서 새로 찾아서 코딩함
# 간단히 설명하면 입력 배열을 받고, 카운트하는 배열, 누적 합 배열, 그리고 새로 정렬될 배열을 생성하여 만든 프로그램
# 근데 메모리 제한이 적어서 배열을 여러개 쓰면 안되는거 같았음.
#n = int(input())

#list_num = []
#for i in range(n):
#    list_num.append(int(input()))
#
#list_count = [0 for i in range(n)]
#for i in range(n):
#    list_count[list_num[i]-1] += 1

#list_sum = []
#sum = 0
#for i in range(n):
#    if(list_count[i] == 0):
#        continue
#    else:
#        sum += list_count[i]
#        list_sum.append(int(sum))
#
#list_sort = []
#for i in range(n):
#    if(list_count[i] == 0):
#        continue
#    else:
#        for j in range(list_count[i]):
#            list_sort.append(i+1)

#for i in list_sort:
#    print(i)
