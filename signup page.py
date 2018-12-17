import numpy as np
import re
import pymysql
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

user_id=str(np.random.randint(1000,10000))
name=input("enter your name: ")
age=input("enter your age: ")
gender=input("enter your gender{m/f}: ")
c=0
t=0
while(c==0):
    email=input("enter your email: ")
    if(re.search("[\w,.$&]{6,30}@[\w,.]{1,19}",email)):
        email=email
        print("correct email id")
        c=c+1
    else:
        print("wrong email id try again")
        continue

while(t==0):
    password = input("enter password: ")
    password=password
    print("correct password")
    confirm_password = input("confirm your password: ")
    if(password==confirm_password):
        password=confirm_password
        print("Success")
        break
    else:
        print("confirm_password is incorrect")
        continue
print("successfully signed in!")

a=pymysql.connect("46.4.115.158","beo","beo@123","testdb")
db=a.cursor()
v=0
sql="""
"""
try:
    sql=sql+"insert into signup values"+"('"+user_id+"','"+name+"','"+age+"','"+gender+"','"+email+"','"+password+"')"
    #db.execute(sql)
    a.commit()
    print("successfully added to db")
except:
    a.rollback()
    a.close()
    print("failed to add in db")
print(sql)
me = "mohammedaamir020@gmail.com"
you = email

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "User data"
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
    <th>User_id</th>
    <th>password</th>
  </tr>"""
html=html+"<tr><td>" + user_id + "</td><td >" + password + "</td></tr>"
html=html+"""</table>
</body>
</html>
"""
part1 = MIMEText(html, 'html')
msg.attach(part1)
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('mohammedaamir020@gmail.com', 'aamir1996')
mail.sendmail(me, you, msg.as_string())
print("Sucessfully email Sent")