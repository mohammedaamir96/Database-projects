import numpy as np
import pymysql
import random
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

user_id=str(np.random.randint(1000,10000))
user_id="ID"+user_id
print("your user id id:",user_id)
name=input("enter your name: ")
c=0
t=0
while(c==0):
    email_id=input("enter your email: ")
    if(re.search("[\w,.$&]{6,30}@[\w,.]{1,19}",email_id)):
        email_id=email_id
        print("correct email id")
        c=c+1
    else:
        print("wrong email id try again")
        continue

password=str(np.random.randint(10000,100000))
print("this is your password:",password)

a=pymysql.connect("46.4.115.158","beo","beo@123","testdb")
db=a.cursor()

sql="""
"""
sql=sql+"insert into signup_reset values"+"('"+user_id+"','"+name+"','"+email_id+"','"+password+"')"

try:
    db.execute(sql)
    a.commit()
    print("successfully added to DB")
except:
    a.rollback()
    a.close()
    print("failed to add data in DB")
print(sql)

me = "mohammedaamir020@gmail.com"
you = email_id

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
#mail.sendmail(me, you, msg.as_string())
print("Sucessfully email Sent")