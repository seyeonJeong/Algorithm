

num = int(input()) #사람 수

list_person = [[0]*2 for _ in range(num)] #사람 몸무게 키 list
count_list = [1 for i in range(num)] # 등수

for i in range(num):
    for j in range(1):
        x, y = map(int,input().split()) # 키, 몸무게 값 받음
        list_person[i][j] = x
        list_person[i][j+1] = y

for i in range(num):
    weight = list_person[i][0] #비교할 키와 몸무게 값을 설정
    height = list_person[i][1]
    for j in range(num): # 모든 값과 비교를 한다. 같을 경우는 제외 (중복)
        if(weight < list_person[j][0]):
            if(height < list_person[j][1]):
                count_list[i] = (count_list[i] + 1) #덩치 등수에 +1된 값을 추가

for i in range(len(count_list)): #출력
    print(count_list[i], end=' ')







