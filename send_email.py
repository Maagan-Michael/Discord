from email.message import EmailMessage
import smtplib
import ssl

def send_mail(reciever_email, email_subject, email_text):
    email_password = "usfrrnjjypczhojl"
    sender_email = "maaganm.hub@gmail.com"



    em = EmailMessage()

    em["From"] = sender_email
    em["To"] = reciever_email
    em["Subject"] = email_subject
    em.set_content(email_text)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
        smtp.login(sender_email,email_password)
        smtp.sendmail(sender_email,reciever_email, em.as_string())