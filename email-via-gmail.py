import smtplib
content='Hello sir. This mail has been sent via Pycharm using PYTHON 3'
try:
    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.starttls()
    mail.login('<sender-email>>','<password>>')
    mail.sendmail('<sender-email>>','<receiver-emial>',content)
    print('Mail is sent successfully.')
    mail.close()
except smtplib.SMTPException as e:
    print('Error while sending mail.')