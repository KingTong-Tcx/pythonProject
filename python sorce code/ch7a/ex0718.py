# program1118.py
class SelectData:
    def __init__(self, data):
        self.data = data[:]

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __delitem__(self, index):
        del self.data[index]


x = SelectData([12, 33, 23, "ab", False])
print(x)  # x的地址
print(x[:])  # x中的全部元素
print(x[2])  # x中的第2个元素
print(x[2:])  # x中从第2个起的全部元素
x[4] = 100  # 替换x中的第4个元素
print(x[:])
del (x[3])  # 删除x中的第3个元素
for num in x:  # 遍历对象x中的元素
    print(num, end=" ")
