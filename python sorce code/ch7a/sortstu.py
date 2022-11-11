class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
]

#sorted(student_objects, key=lambda aa: aa.age)   # sort by age

student_objects.sort(key=lambda x:x.age,reverse=False)

for i in student_objects:
    print(i)
