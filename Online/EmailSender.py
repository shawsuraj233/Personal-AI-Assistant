import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#email configuration
def EmailSender(receiver_mail,subject,message):
    sender_mail = "shawsuraj233@gmail.com"
    sender_pass = "Your App Password"
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_mail
        msg["To"] = receiver_mail
        msg["Subject"]= subject
        msg.attach(MIMEText (message, 'plain'))
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_mail, sender_pass)
            server.sendmail( sender_mail, receiver_mail, msg.as_string())
            print("email sent succesfully")
    except Exception as e:
        print('Error: {e}')

