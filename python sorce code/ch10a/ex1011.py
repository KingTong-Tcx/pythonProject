# program0811.py
class UserDefinedException(Exception):	
    def __init__(self,eid,message):    #异常描述
        self.eid=eid
        self.message=message
        
class ExceptionDemo:                   #业务逻辑
    def draw(self,number):
        print("called compute("+str(number)+")");
        if (number>500 or number<=0):
            raise UserDefinedException(101,"number out of bounds")
        else:
            print("normal exit")
myobject=ExceptionDemo()          #功能测试
try:
    myobject.draw(125)
    myobject.draw(900)
except UserDefinedException as e:
    print("Exception caught,id:{},message:{}".format(e.eid,e.message))
