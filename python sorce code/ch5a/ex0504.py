# program0404.py
lst = list(range(2, 21, 3))
i = 0
result = []
while i < len(lst):
    result.append(lst[i] * lst[i])
    i += 1
print(result)
