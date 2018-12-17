import pymysql
import random
import re
x = pymysql.connect("46.4.115.158","beo", "beo@123","testdb")

db = x.cursor()
sql = db.execute("""create table students(rollno int,name varchar(30),marks int) """)
try:

    x.commit()
    print("success")

except:
    x.rollback()
    x.close()
    print("fail")
