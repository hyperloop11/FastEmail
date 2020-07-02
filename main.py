import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd

email_list = pd.read_excel("Email_list.xlsx") #write name of excel file which has headings NAME and EMAIL

all_names = email_list['NAME']
all_emails = email_list['EMAIL']

msg = MIMEMultipart()
msg['Subject'] = 'subject' # add subj here

body='''Hello! #add body here
This is sample body for your automated email B) '''


msg.attach(MIMEText(body, 'plain'))
fromadd = "senders_email@gmail.com"#add sender's email
smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.login(fromadd ,'xxxx') # add your email's password replacing xxxx
sum=0

for idx in range(len(all_emails)):

    toadd =all_emails[idx]

    msg['From'] = fromadd
    msg['To'] = toadd 

    filename = "anyfile.extention" #extension imp
    attachment = open('anyfile.extention', 'rb')

    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)

    text = msg.as_string()
    smtpobj.sendmail(fromadd , toadd , text)
    sum+=1
    print("SENT EMAIL "+str(sum))
smtpobj.quit()
