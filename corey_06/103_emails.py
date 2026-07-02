import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_USER")
APP_PASSWORD = os.getenv("APP_PASS")

if EMAIL_ADDRESS is None:
    raise ValueError("EMAIL_USER environment variable is not set.")

if APP_PASSWORD is None:
    raise ValueError("APP_PASS environment variable is not set.")

# this is testing instead sending real emails
# >python -m pip install aiosmtpd
# >python -m aiosmtpd -n -l localhost:1025

# this will produce error if no cmd running
# with smtplib.SMTP('localhost', 1025) as smtp:
#     subject = 'Demo Subject'
#     body = 'Demo Body'
#     msg = f"Subject: {subject}\n\n{body}"

    # smtp.sendmail('demo', 'demo', msg)

# terminal
# C:\Users\Vijay Karthik>python -m aiosmtpd -n -l localhost:1025
# ---------- MESSAGE FOLLOWS ----------
# Subject: Demo Subject
# X-Peer: ('::1', 62383, 0, 0)

# Demo Body
# ------------ END MESSAGE ------------


# this is real way of sending emails
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, APP_PASSWORD)

    subject = 'Demo Subject'
    body = 'Demo Body'
    msg = f"Subject: {subject}\n\n{body}"

    # smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)
    # this is not recommneded to send emials to urself each time


# instead of doing elho and starttls we can do it better way using ssl
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, APP_PASSWORD)

    subject = 'Demo Subject'
    body = 'Demo Body'
    msg = f"Subject: {subject}\n\n{body}"

    # smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)

# for structured email
from email.message import EmailMessage
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, APP_PASSWORD)

    msg =  EmailMessage()
    msg['Subject'] = 'Demo Subject'
    msg['From'] = EMAIL_ADDRESS
    msg['to'] = EMAIL_ADDRESS
    msg.set_content('Demo body')

    # smtp.send_message(msg)

# to add img attachment
from PIL import Image
import io

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, APP_PASSWORD)

    msg = EmailMessage()
    msg['Subject'] = 'Checkout comic'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content('Attached comic...')

    with open('comic.png', 'rb') as f:
        file_content = f.read()
        file_name = f.name
    
    image = Image.open(io.BytesIO(file_content))
    # print(image.format)
    # PNG

    msg.add_attachment(
        file_content,
        maintype = 'image',
        subtype = image.format,
        filename = file_name
    )

    # smtp.send_message(msg)

# lets say wanna add multiple attachements
from pathlib import Path
attachments = ['comic.png', 'RYALI_VENKATA_SRI_VIJAY_KARTHIK.pdf', 'plan.txt']

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, APP_PASSWORD)

    msg = EmailMessage()
    msg['Subject'] = 'Checkout attachments'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content('Attached docs...')

    for file in attachments:
        with open(file, 'rb') as f:
            file_data = f.read()

        path = Path(file)
        ext = path.suffix.lower()
        filename = path.name

        if ext in ['png', 'jpg', 'jpeg']:
            maintype = 'image'
            subtype = ext if ext != 'jpg' else 'jpeg'
        elif ext == 'pdf':
            maintype = 'application'
            subtype = 'pdf'
        elif ext == 'txt':
            maintype = 'text'
            subtype = 'plain'
        else:
            maintype = 'application'
            subtype = 'octet-stream'
        msg.add_attachment(
            file_data,
            maintype=maintype,
            subtype=subtype,
            filename=filename
        )
        
    # smtp.send_message(msg)

# sending multiple emails
# simply in place of To pass comma sep values
# msg['To'] = ', '.join(emails_list_to_send)

# now final tip!
# how to send emial in form of html

# simple add alternative with html str and subtype'html'
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, APP_PASSWORD)

    msg = EmailMessage()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg['Subject'] = 'Demo Subject'
    msg.set_content('Demo Body')
    msg.add_alternative("""\
        <!DOCTYPE html>
        <html>
        <body>
            <h2>SMTP Test Email</h2>
            <p>This is a simple test email sent via SMTP.</p>
            <p>If you can see this, your email setup is working 🎉</p>
        </body>
        </html>
    """, subtype='html')

    smtp.send_message(msg)

