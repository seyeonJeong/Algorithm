

num = int(input())
list_num = list(map(int,input().split()))
plus, sub, mul, div = map(int, input().split())

maxnum = -1000000000
minnum = 1000000000


def dfs(i,n):
    global plus,sub,mul,div,maxnum,minnum
    if i == num:
        maxnum = max(maxnum, n)
        minnum = min(minnum, n)
    else:
        if plus > 0:
            plus -= 1
            dfs(i+1, n+list_num[i])
            plus += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, n-list_num[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, n*list_num[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(n/list_num[i]))
            div += 1

dfs(1,list_num[0])

print(maxnum)
print(minnum)




