 1   class DemoClass2:
 2       def __init__(self,year=0,month=0,day=0):
 3           self.day=day
 4           self.month=month
 5           self.year=year
 6       @classmethod
 7       def get_date(cls,string_date):   
 8           #第一个参数cls， 表示调用当前的类名
 9           year,month,day=map(int,string_date.split('-'))
10           date1=cls(year,month,day)
11           return date1   #返回的是一个初始化后的类
12       def output_date(self):
13           print("year:",self.year,"month:",self.month,"day:",self.day)
14   rq1= DemoClass2(2018,6,2)
15   rq1.output_date()
16   rq2=DemoClass2.get_date("2018-6-6")
17   rq2.output_date()
