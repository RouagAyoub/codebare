import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def print_hi(name):
    fileopen = open('file.txt', 'r')
    for line in fileopen.readlines():
        sender_address = 'rouagayoub@gammacodes.com'
        sender_pass = 'rouag.ayoub'
        receiver_address = 'rouag.ayb@gmail.com'
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = ''
        message.attach(MIMEText('', 'plain'))
        session = smtplib.SMTP(host='gammacodes.com', port=587)
        session.ehlo()
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print("sent to {}".format(line))


if __name__ == '__main__':
    print_hi('PyCharm')
