import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def mail(sender_address, password, receiver_address, subject, message):
    msg = MIMEMultipart()
    msg['From'] = sender_address
    msg['To'] = receiver_address
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.login(sender_address, password)
    mailServer.sendmail(sender_address, receiver_address, msg.as_string())
    mailServer.close()
    
if __name__ == '__main__':
	sender_address = ''
	password = ''
	receiver_address = raw_input("Enter the recepient's email address: \n")
	subject = raw_input("Enter the subject of the mail: \n")
	message = raw_input("Enter the message to be sent: \n")	
	mail(sender_address, password, receiver_address, subject, message)