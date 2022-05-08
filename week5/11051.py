import math

n = list(map(int,input().split()))

print(math.comb(n[0],n[1])%10007)