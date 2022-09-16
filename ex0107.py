# ex0107.py
lst = [89, 45, 23.1, 98, 33]
# nopass 为不及格人数，maxscore为最高分
notpass = maxscore = 0
for item in lst:
    if maxscore < item:
        maxscore = item
    if item < 60:
        notpass += 1
print("最高分是{},不及格人数是{}".format(maxscore, notpass))
