import sqlite3


# 连接数据库的通用函数
def getConnection():
    dbstring = "d:/sqlite/test.db"
    conn = sqlite3.connect(dbstring)
    cur = conn.cursor()
    sqlstring = '''create table if not exists order1(order_id integer primary key,order_dec varchar(20),price float,ordernum integer,
address varchar(30))'''
    cur = conn.execute(sqlstring)
    return conn


# 显示所有记录
def showAllDB():
    print("----------------display record--------------")
    dbinfo = getConnection()
    cur = dbinfo.cursor()
    cur.execute("select * from order1")
    records = cur.fetchall()
    for line in records:
        print(line)
    cur.close()


# 获得订单输入数据
def getOrderListInfo():
    orderId = input("Please enter Order ID:")
    orderDec = input("Please enter Order description:")
    price = eval(input("Please enter price:"))
    ordernum = eval(input("Please enter number:"))
    address = input("Please enter address:")
    return orderId, orderDec, price, ordernum, address


# 添加记录
def addRec():
    sepline = "-----------------add record----------------"
    print(sepline)
    record = getOrderListInfo()
    dbinfo = getConnection()
    sqlstr = "insert into order1(order_id,order_dec,price,ordernum,address) values(?,?,?,?,?)"
    dbinfo.execute(sqlstr, (record[0], record[1], record[2], record[3], record[4]))
    dbinfo.commit()
    print("-------------add record success------------")
    showAllDB()
    dbinfo.close()


# 删除记录
def delRec():
    sepline = "-----------------del record----------------"
    print(sepline)
    dbinfo = getConnection()
    choice = input("Please input deleted order_ID:")
    sqlstr = "delete from order1 where order_id="
    dbinfo.execute(sqlstr + choice)
    dbinfo.commit()
    print("-------------record delete success----------")
    showAllDB()
    dbinfo.close()


# 修改记录
def modifyRec():
    sepline = "-------------change record------------------"
    print(sepline)
    dbinfo = getConnection()
    choice = input("Please input change order_ID:")
    record = getOrderListInfo()
    sqlstr = "update order1 set order_id=?,order_dec=?,price=?,ordernum=?,address=? where order_id=" + choice

    dbinfo.execute(sqlstr, (record[0], record[1], record[2], record[3], record[4]))
    dbinfo.commit()
    showAllDB()
    print("--------------change record success----------")


# 查找记录
def searchRec():
    sepline = "-------------- search record-----------------"
    print(sepline)
    dbinfo = getConnection()
    cur = dbinfo.cursor()
    choice = input("Please input search order_ID:")
    sqlstr = "select * from order1 where order_id="

    cur.execute(sqlstr + choice)
    dbinfo.commit()
    print("-------------the record of your find---------")

    for row in cur:
        print(row[0], row[1], row[2], row[3], row[4])
    cur.close()
    dbinfo.close()


# 判断是否继续操作
def continueif():
    choice = input("continue(y/n)?")
    if str.lower(choice) == 'y':
        a = 1
    else:
        a = 0
    return a


# 程序入口
if __name__ == "__main__":
    flag = 1
    while flag == 1:
        sepline = "----------OrderItem Manage System-----------"
        print(sepline)
        menu = '''
Please choice item:
1) Append Record
2) Delete Record
3) Change Record
4) Search Record
Please enter order number:

'''
        choice = input(menu)
        if choice == '1':
            addRec()
            flag = continueif()
        elif choice == '2':
            delRec()
            flag = continueif()
        elif choice == '3':
            modifyRec()
            flag = continueif()
        elif choice == '4':
            searchRec()
            flag = continueif()
        else:
            print("order number error!!!")
