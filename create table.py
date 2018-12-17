import pymysql
import random

x=pymysql.connect("46.4.115.158","beo","beo@123","testdb")
db=x.cursor()
count=1
a=input("enter the tablename:")

sql = """
"""
sql=sql+"create table "+a+"("
b=int(input("enter the number of columns: "))
for i in range(count,b+1):
    c=input("enter column name: ")
    d=input("enter column datatype :")
    sql=sql+c+" "+d
    if(i<b):
        sql=sql+","
sql=sql+")"
print(sql)
try:
    db.execute(sql)
    x.commit()
    print("success")
    #db.execute("""alter table students modify address varchar(255)""")
    #db.execute("""insert into students values(1,"aamir",60,"chennai"),(2,"ronil",70,"chennai"),(3,"kana",80,"bangalore"),(4,"vikas",90,"maduravoyal"),(5,"suriya",40,"chennai")""")
except:
    x.commit()
    x.rollback()
    print("fail")