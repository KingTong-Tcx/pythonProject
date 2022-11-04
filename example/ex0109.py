# ex0109,py
file = open("file.txt", 'r')
s1 = file.read()
file.close()
lst = s1.split(',')
lst2 = []
for item in lst:
    lst2.append(eval(item))
# print(lst2)
# notpass为不及格人数，maxscore为最高分
notpass = maxscore = 0
for item in lst2:
    if maxscore < item:
        maxscore = item
    if item < 60:
        notpass += 1
print("最高分是{}，不及格人数是{}".format(maxscore, notpass))
