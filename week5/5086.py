
while(1): #정해진 수가 없으면 무한 반복
    a,b = map(int,input().split())
    if a==0 and b==0: #조건확인 과정에서 마지막에 0을 넣으면 0으로 나누어보기 때문에 이거 먼저 써야 런타임 에러가 안뜬다.
        break
    elif b % a == 0:
        print('factor')
    elif a % b == 0 :
        print('multiple')
    else:
        print('neither')


