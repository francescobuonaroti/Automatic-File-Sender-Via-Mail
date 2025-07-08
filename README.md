# Automatic-File-Sender-Via-Mail

This is a simple Python script to automate the sending of emails with PDF attachments.

## Features

- Automatically reads PDF files from a folder
- Extracts email addresses from filenames
- Sends a personalized email with the PDF as an attachment
- Uses secure SMTP connection with Gmail

## File Format Assumption

The script assumes that PDF files are named using the recipient's email address followed by `_N`, for example: john.doe@example.com_N123.pdf

## Requirements

- Python 3.6+
- A Gmail account with an App Password (see this: https://support.google.com/accounts/answer/185833?hl=en)

## Setup

1. Install dependencies (if not already available):
    ```bash
    pip install --upgrade pip
    ```

2. Set your Gmail App Password as an environment variable:
    ```bash
    export EMAIL_PASSWORD='your_app_password_here'
    ```

3. Place all your PDF files in the `raccolta/` directory.

4. Run the script:
    ```bash
    python send_emails.py
    ```

## Security Notice

Do **not** hardcode your email password in the script. Always use environment variables or secret managers to protect sensitive data.

## License

This project is open source under the MIT License.
