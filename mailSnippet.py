import smtplib
sender_address = 'liptopersonal@gmail.com'
password = 'Erzalucy'

def mail(receiver_address, message):
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.login(sender_address, password)
    mailServer.sendmail(sender_address, receiver_address, message)
    mailServer.close()
    
if __name__ == '__main__':
    receiver_address = raw_input("Enter the recepient's email address: \n")
    message = raw_input("Enter the message to be sent: \n")
    mail(receiver_address, message)