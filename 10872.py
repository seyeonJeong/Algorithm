def clac_factorial(number): # 재귀함수로 팩토리얼을 계산한다.
    if(number > 1): # 팩토리얼 계산은 1이 되면 종료하므로 1보다 클때까지 재귀
        return number * clac_factorial(number-1) # 재귀 한번 할때마다 -1을 해줌
    else:
        return 1 #number값이 1이되면 1을 return하고 종료


input_num = int(input())
print(clac_factorial(input_num))