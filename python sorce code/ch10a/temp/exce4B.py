class AgeException(Exception):
    def __init__(self,description):
        self.description=description

class Student():
     def __init__(self,strname,age):
         self.strname=strname
         self.age=age
         
try:
    s2=Student('Lisi',20)
finally:
    print(2)
##try: 
##   
##except Exception as e:
##    print(e)
