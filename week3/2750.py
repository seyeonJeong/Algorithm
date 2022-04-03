

n = int(input()) #개수를 받는다

list_num = [] #빈 list를 만듦

for i in range(n): #list에 int값의 입력값을 받아준다.
    list_num.append(int(input()))

for i in range(n): #버블정렬로 구현함
    for j in range(i+1,n): #인덱스 0과1, 0과2, 0과3, 0과4 ...를 반복해서 비교하는 정렬
        if(list_num[i]>list_num[j]): #만약 list_num[i]가 list_num[j]보다 크면 두 값의 자리를 바꿔준다.
            temp = list_num[j]
            list_num[j] = list_num[i]
            list_num[i] = temp
            ##제출하고 알게된 사실인데 list_num[i],list_num[j] = list_num[j],list_num[i]를 이용하면 한줄에 바꿀수 있다..


for i in list_num: #배열을 프린트
    print(i)
