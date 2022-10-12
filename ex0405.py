# ex0405.py
s = 0
for i in range(100):
    if i % 3 == 0 or '3' in str(i):
        s += i
        print(i)

print(s)

