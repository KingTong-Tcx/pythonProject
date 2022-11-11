import sqlite3


def getConnection():
    dbstring="d:/sqlite/test.db"
    conn=sqlite3.connect(dbstring)
    cur=conn.cursor()
    sqlstring='''create table if not exists order1(order_id integer primary key,order_dec varchar(20),price float,ordernum integer,
address varchar(30))'''
    cur=conn.execute(sqlstring)
    return conn




def showAllDB():
    print("-------------------显示内容-------------------")
    dbinfo=getConnection()
    cur=dbinfo[1].cursor()
    cur.execute("select * from order1")
    records=cur.fetchall()
    for line in records:
        print(line)
    cur.close()


def getOrderInfo():
    orderId=input("Please enter Order ID:")
    orderDec=input("Please enter Order description:")
    price=eval(input("Please enter price:"))
    ordernum=eval(input("Please enter number:"))
    address=input("Please enter address:")
    return orderId,orderDec,price,ordernum,address

def addRec():
    welcome="-----------------------------welcome add record------------------------"
    print(welcome)
    record=getOrderInfo()
    dbinfo=getConnection()
    sqlstr="insert into order1(order_id,order_dec,price,ordernum,address) values(?,?,?,?,?)"
    dbinfo[1].execute(sqlstr,(record[0],record[1],record[2],record[3],record[4]))
    dbinfo[1].commit()
    print("-------------data add success----------")
    showAllDB()
    dbinfo[1].close()

def delRec():
    welcome="-----------------------------welcome del record------------------------"
    print(welcome)
    dbinfo=getConnection()
    choice=input("Please input deleted order_ID:")
    sqlstr="delete from order1 where order_id="
    dbinfo[1].execute(sqlstr+choice)
    dbinfo[1].commit()
    print("-------------record delete success----------")
    showAllDB()
    dbinfo[1].close()

def modifyRec():
    welcome="-----------------------------welcome to change record------------------------"
    print(welcome)
    dbinfo=getConnection()
    choice=input("Please input change order_ID:")
    record=getOrderInfo()
    sqlstr="update order1 set order_id=?,order_dec=?,price=?,ordernum=?,address=? where order_id="+choice
    
    dbinfo[1].execute(sqlstr,(record[0],record[1],record[2],record[3],record[4]))
    dbinfo[1].commit()
    showAllDB()
    print("-------------record change success----------")

def searchRec():
    welcome="-----------------------------welcome to search record------------------------"
    print(welcome)
    dbinfo=getConnection()
    cur=dbinfo[1].cursor()
    choice=input("Please input search order_ID:")
    sqlstr="select * from order1 where order_id="
    
    cur.execute(sqlstr+choice)
    dbinfo[1].commit()
    
    print("-------------the record of your find----------")

    for row in cur:
        print(row[0],row[1],row[2],row[3],row[4])
    cur.close()
    dbinfo[1].close()

def continueif():
    choice=input("continue(y/n)?")
    if choice=='y':
        a=1
    else:  
        a=0
    return a

if __name__=="__main__":
    flag=1
    while flag==1:
        welcome="-------------OrderItem Manage System--------------------"
        print(welcome)
        menu='''
Please choice item:
1) Append Record
2) Delete Record
3) Change Record
4) Search Record
Please enter order number:

'''
        choice=input(menu)
        if choice=='1':
            addRec()
            flag=continueif()
        elif choice=='2':
            delRec()
            flag=continueif()
        elif choice=='3':
            modifyRec()
            flag=continueif()
        elif choice=='4':
            searchRec()
            flag=continueif()
        else:
            print("order number error!!!")
            


    
