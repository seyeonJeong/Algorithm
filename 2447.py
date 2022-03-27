
def draw_stars(num):
    matrix = []
    for i in range(3*len(num)):
        if i // len(num) == 1:
            matrix.append(num[i%len(num)] + " "*len(num) +  n[i%len(n)] )
        else:
            matrix.append(n[i%len(n)] * 3)
        return(list(matrix))





star = ["***", "* *", "***"]
n = int(input())
count = 0

while n != 3:
    n = int(n/3)
    count+=1  #count 1씩 증가

for i in range(count):
    star = draw_stars(star)
for i in star:
    print(i)



