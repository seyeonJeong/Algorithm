def clac_Fibonacci(number): # n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램
    if(number <= 0): # 0번째와 1번째 수는 각각 0과 1로 고정이므로 0이하의 수가 함수에 들어오면 0으로 return 해줌
        return 0
    elif(number == 1): # 1번째 수는 1이므로 1이 함수에 들어오면 1로 return
        return 1
    else: #0번째와 1번째가 아니라면 피보나치 수의 공식대로 재귀를 이용하여 계산
        return clac_Fibonacci(number-1) + clac_Fibonacci(number-2)

result = int(input())
print(clac_Fibonacci(result))