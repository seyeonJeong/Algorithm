
n,m = input().split() # n과 m을 입력받음
n= int(n)
m = int(m)
num = input().split() # list num의 값을 입력받음

for i in range(n):
    num[i] = int(num[i])   #list num을 str에서 int로 바꿔줌

sum = 0
dif = 0

for i in range(n): # list의 숫자만큼 반복한다
    for j in range(i+1,n): #list의 두번째 부터
        for h in range(j+1,n): #list의 세번째 부터
            dif = int(num[i]) + int(num[j]) + int(num[h]) #비교하기 위한 변수
            if(dif <= int(m)): #더한 값은 m보다 크면 안된다.
                if(dif>=int(sum)): # 만약 비교변수의 값이 원래 저장된 sum 보다 크거나 같다면
                    sum = int(dif) # sum을 비교변수의 값으로 변경한다.

print(sum) #sum을 출력함
