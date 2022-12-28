#  编程题
# 1、设计一个Group类 该类中包括：一个数据成员score（每个学生的分数）、两个类成员total（班级的总分）和count（班级的人数）。
# 成员方法setScore（score）用于设置分数，成员方法sum（）用于累计总分，类方法average（）用于求平均值。交互式输入某组学生的成绩，显示该组的总分和平均分
class Group:
    total = count = 0

    def __init__(self, score):
        self.score = score
        self.sum()

    def setScore(self):  # 设置分数
        Group.count += 1  # 每增加一个分数人数 +1
        return self.score

    def sum(self):  # 累加成绩
        Group.total += self.setScore()

    @classmethod
    def average(cls):  # 计算平均分
        return Group.total / Group.count

    @classmethod
    def show(cls):
        print("总分是:{}".format(Group.total))
        # print("总人数是:{}".format(Group.count))
        print("平均分是:{:.2f}".format(Group.average()))


a = eval(input("请输入学生数量："))
lst = [a]
for i in range(a):
    lst.append(Group(eval(input("请输入第{}位同学成绩：".format(i + 1)))))
Group.show()
