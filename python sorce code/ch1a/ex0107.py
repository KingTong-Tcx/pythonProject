# program0108.py
lst = [89, 45, -34, 23.1, 98, 33]
maxscore = max(lst)  # 最高分
lst2 = filter(lambda x: x < 60, lst)  # 不及格数据的序列
notpass = len(list(lst2))  # 不及格人数
print("最高分是{}，不及数人数是{}".format(maxscore, notpass))
