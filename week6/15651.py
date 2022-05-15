

n,m = map(int, input().split())
s = []
def dfs():#dfs 함수를 구현
    if len(s) == m: # list s의 길이가 m과 같으면 출력한다.
        print(' '.join(map(str,s)))
        return
    for i in range(1,n+1): #1~n+1까지 탐색
         #만약 i가 s에 없다면?
        s.append(i) # i를 s에 추가한다.
        dfs() #재귀
        s.pop() #재귀가 끝나면 pop
    # 예시 n=4, m=2
    # i는 1부터 탐색
    # s = [1,2]가 되면 재귀를 통해 출력
    # i는 3이므로 2를 pop하고 s = [1,3] -> [1,4]
    # i = 1일때의 재귀가 끝
    # i = 2가 됨
    # 반복
dfs()




