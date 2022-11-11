class DemoClass2:
    def __init__(self,year=0,month=0,day=0):
        self.day=day
        self.month=month
        self.year=year
    @classmethod
    def get_date(cls,string_date):   
        #第一个参数cls， 表示调用当前的类名
        year,month,day=map(int,string_date.split('-'))
        date1=cls(year,month,day)
        return date1   #返回的是一个初始化后的类
    def output_date(self):
        print("year:",self.year,"month:",self.month,"day:",self.day)
rq1= DemoClass2(2018,6,2)
rq1.output_date()
rq2=DemoClass2.get_date("2018-6-6")
rq2.output_date()
