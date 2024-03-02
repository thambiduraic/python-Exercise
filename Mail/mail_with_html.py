import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(sender_email, sender_password, receiver_email, subject, html_file_path):
    # Create a multipart message
    message = MIMEMultipart()

    # Setup the parameters of the message
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Read the HTML file
    with open(html_file_path, 'r') as html_file:
        html_content = html_file.read()

    # Attach HTML content
    html_part = MIMEText(html_content, 'html')
    message.attach(html_part)

    # Create SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    # Login to the SMTP server
    server.login(sender_email, sender_password)

    # Send email
    server.send_message(message)

    # Quit the SMTP server
    server.quit()

# Example usage
sender_email = 'sender_mail'
sender_password = 'app_password'
receiver_email = 'receiver_mail'
subject = 'HTML File Test'
html_file_path = 'D:\Thambidurai\pycharm_work_dir\PycharmProjects\pythonProject\Mail\demo.templatemonster.com-1709368894\index.html' # add your html file path
html_file_path.replace("\\", "/")

send_email(sender_email, sender_password, receiver_email, subject, html_file_path)
