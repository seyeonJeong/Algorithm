
n = int(input())

list_word = []
for i in range(n):
    list_word.append(input())

result1 = set(list_word)
list_word = list(result1)
list_word.sort()
list_word.sort(key = len)
for i in list_word:
    print(i)