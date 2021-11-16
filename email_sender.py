"""

Email sender module.

"""
import smtplib
from email.message import EmailMessage
from template.html_template import html_template
from db import update_data_in_database


def send_email(email):
    """
    Email sender function.
    :param email: email (name@domena.host)
    :return:
    """
    msg = EmailMessage()
    msg['Subject'] = '<Title>'
    msg['From'] = '<email>'
    msg['To'] = email
    msg.set_content(html_template, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('<email login>>', '<password>')
        smtp.send_message(msg)
        update_data_in_database(email)
        print(f"Email to {email} has been sent and to_send value changed")

