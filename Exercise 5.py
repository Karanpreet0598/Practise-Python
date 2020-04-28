a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

i = 0
j = 0
result = dict()
for i in a:
    for j in b:
        if i == j:
            result.update({i: 1})
            c = list(dict.fromkeys(result))
print(c)
