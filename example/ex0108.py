# ex0108.py
lst = [89, 45, 23.1, 98, 33]
maxscore = max(lst)
lst2 = filter(lambda x: x < 60, lst)
notpass = len(list(lst2))
print("最高分是{}，不及格人数是{}".format(maxscore, notpass))
