import pymysql
import random

a=pymysql.connect("46.4.115.158","beo","beo@123","testdb")

db=a.cursor()
v=0
tn=input("enter table name: ")
sql="""
"""
sql=sql+"desc "+tn
db.execute(sql)
result=db.fetchall()
aa=int(db.execute(sql))
print(aa)
for j in result:
    j[0]
sql = """
"""
sql=sql+"insert into "+tn+" values"
row=int(input("enter the number of values to be added: "))
for i in range(1,row+1):
    count = 1
    sql=sql+"("
    print("row", i)
    for k in result:
        print("enter ",k[0] ,end='')
        value=input()
        sql=sql+value
        if(count<aa):
            sql=sql + ","
        count=count+1
    sql = sql + ")"
    if(i<row):
        sql=sql+","
print(sql)
try:

    db.execute(sql)
    a.commit()
    print("success")
except:
    a.rollback()
    a.close()
    print("fail")