x,y =  map(int,input().split())

for i in range(min(x,y),0,-1): # 시작은 둘중 작은값에서 -1 큰값은 공약수가 될 수 없다
    if x%i==0 and y%i==0:
        print(i)
        break

for i in range(max(x,y),(x*y)+1): #시작은 둘중 큰값부터 작은값은 공배수가 될 수 없다
    if i%x == 0 and i%y==0:
        print(i)
        break
