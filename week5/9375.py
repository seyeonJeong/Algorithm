
n = int(input())

for _ in range(n):
    n2 = int(input())

    clothes_type = {}
    for _ in range(n2):
        name,type=input().split()
        if(type in clothes_type):
            clothes_type[type] +=1
        else:
            clothes_type[type] = 1
    case = 1

    for key in clothes_type.keys():
        case = case*(clothes_type[key] + 1)
    print(case-1)

