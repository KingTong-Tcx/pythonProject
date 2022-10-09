# ex0401.py
import math

x = -37
if x < 0:
    y = math.fabs(x)
else:
    y = math.sqrt(x)
print("计算的结果是：", y)

import random

# 模拟科目一考试，随机生成一个成绩，如果成绩大于等于90分，显示"通过，恭喜！"，否则显示"不通过，欢迎下次再考！"
score = random.randint(80, 100)
print(score)
if score >= 90:
    print("通过，恭喜！")
else:
    print("不通过，欢迎下次再考！")
