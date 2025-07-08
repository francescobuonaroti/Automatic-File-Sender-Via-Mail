import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Sends an email with a PDF attachment
def send_email(to_address, attachment_path):
    from_address = 'your_email@gmail.com'
    password = os.getenv('EMAIL_PASSWORD')  # Securely get the password from environment variable

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = "Receipt"

    # Email body
    msg.attach(MIMEText("Please find the attachment.\n\nBest regards.", 'plain'))

    # Attach the PDF file
    with open(attachment_path, 'rb') as f:
        part = MIMEApplication(f.read(), _subtype='pdf')
    part.add_header(
        'Content-Disposition',
        'attachment',
        filename=os.path.basename(attachment_path)
    )
    msg.attach(part)

    # Connect and send the email using SMTP over SSL
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(from_address, password)
        server.sendmail(from_address, to_address, msg.as_string())

# Directory containing PDF files
pdf_folder_path = './raccolta'

# Creates a list of email addresses and their corresponding PDF paths
def create_email_list(folder_path):
    email_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            # Extract the email address from the file name (assumes format: email_N123.pdf)
            email_address = filename.split("_N")[0]
            pdf_path = os.path.join(folder_path, filename)
            email_list.append((email_address, pdf_path))
    return email_list

if __name__ == "__main__":
    print("Email Sending Tool")

    email_data = create_email_list(pdf_folder_path)
    for email, file_path in email_data:
        print(f"Address: {email}    File -> {file_path}")

    print(f"{len(email_data)} email(s) ready to send.")
    action = input("Send emails? (Y/N): ")

    if action.strip().lower() == "y" or action.strip() == "":
        for email, file_path in email_data:
            print(f"Sending email to: {email}")
            send_email(email, file_path)
        print(f"Successfully sent {len(email_data)} email(s).")
    input("Press Enter to exit.")
