import re
import numpy as np
import pymysql
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

userid=str(input("enter your user_id: "))

a=pymysql.connect("46.4.115.158","beo","beo@123","testdb")
db=a.cursor()
t=0

sql="""
"""
sql=sql+"select password from signup_reset where user_id="+"'"+userid+"'"
#print(sql)
db.execute(sql)
res=str(db.fetchall())
#print(res)
pwd=re.sub(r'[^\w$&@%]',"",res)
#print(pwd)
#email=input("enter emailid: ")
while(t==0):
    password = str(input("enter your old_password: "))
    if(pwd==password):
        reset_password=str(input("enter a new password: "))
        confirmpassword = str(input("enter your password once again: "))
        if(pwd==confirmpassword):
            print("new password should be different")
            continue
        if(reset_password==confirmpassword):
            password = confirmpassword
            t=t+1
        else:
            print("password doesn't match")
            continue
    else:
        print("your new password id incorrect")
        continue
print("successfully signed in!")

sql="""
"""
sql=sql+"update signup_reset set password="+"'"+password+"'"+" where user_id="+"'"+userid+"'"

try:
    db.execute(sql)
    a.commit()
    print("data updated successfully!")

except:
    a.rollback()

    print("data not updated successfully")
sql="""select email_id from signup_reset where user_id="""+"'"+userid+"'"
db.execute(sql)
res1=str(db.fetchall())
#print(res)
email=re.sub(r'[^\w$&@.%]',"",res1)
print(email)
a.close()

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
html=html+"<tr><td>" + userid + "</td><td >" + password + "</td></tr>"
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