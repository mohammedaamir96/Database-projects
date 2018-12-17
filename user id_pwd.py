import re
import pymysql
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

t=0
title=[]

a=pymysql.connect("46.4.115.158","beo","beo@123","testdb")
db=a.cursor()

while(t==0):
    uid = input("enter your user_id: ")
    pwd = input("enter your pwd: ")

    sql="""select user_id from signup_reset where password="""+"'"+pwd+"'"
    db.execute(sql)
    res1=str(db.fetchall())
    userid=re.sub(r'[^\w$&@%]',"",res1)
    sql = """select password from signup_reset where user_id=""" + "'" + uid + "'"
    db.execute(sql)
    res = str(db.fetchall())
    password = re.sub(r'[^\w$&@%]', "", res)
    if(uid==userid):
        if(pwd==password):
            print("userid and password matched")
            break
        else:
            print("userid & password not matched")
        continue
tn=input("enter table name: ")

sql = """select email_id from signup_reset where user_id=""" + "'" + uid + "'"
db.execute(sql)
res = str(db.fetchall())
emailid = re.sub(r'[^\w$&@%]', "", res)

sql="""desc """+tn
#print(sql)
db.execute(sql)
res=db.fetchall()
for i in res:
    title.append(str(i[0]))
print(title)

sql="""select * from signup_reset where user_id="""+"'"+uid+"'"
db.execute(sql)
temp=db.fetchall()
value=list(temp[0])
print(value)

me = "mohammedaamir020@gmail.com"
you = "mohammedaamir96@gmail.com"


msg = MIMEMultipart('alternative')
msg['Subject'] = "user details"
msg['From'] = me
msg['To'] = you

html="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Table data</title>
</head>
<body>
<style>
table, th, td {
   border: 1px solid black;
   border-collapse: collapse;
}
th, td{
    padding:10px;
    text-align:centre;
 }
</style>
<table style="width:30%">
 <tr bgcolor="red">
 <tr>
 """
for j in title:
    if(str(j)=="password"):
        continue
    else:
        html=html+"<th>" + str(j) +"</th>"
html=html+"</tr><tr>"

for k in value:
    if(pwd==str(k)):
        continue
    else:
        html=html+"<td>" + str(k) +"</td>"
html=html+"</tr></table></body></html>"
part1 = MIMEText(html, 'html')
msg.attach(part1)
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('mohammedaamir020@gmail.com', 'aamir1996')
mail.sendmail(me, you, msg.as_string())
print("successfully email sent")