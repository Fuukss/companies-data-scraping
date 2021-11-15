"""

Email sender module.

"""
import smtplib
from email.message import EmailMessage
from template.html_template import html_template


def check_new_email_sender(email):
    """
    Email sender function.
    :param email: email (name@domena.host)
    :return:
    """
    msg = EmailMessage()
    msg['Subject'] = 'Może potrzebujesz wsparcia informatycznego?'
    msg['From'] = '<email>'
    msg['To'] = email
    msg.set_content(html_template, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('<email_login>', '<password>')
        smtp.send_message(msg)
        print(f"Email to {email} has been sent")

