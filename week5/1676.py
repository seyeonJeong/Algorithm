
import math
n = int(input())

facn = math.factorial(n)
count = 0
while(1):
    mok = facn // 10
    namu = facn % 10
    facn = mok
    if(namu != 0):
        break
    count += 1

print(count)

