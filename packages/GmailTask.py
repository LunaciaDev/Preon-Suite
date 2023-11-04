from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from email.mime.text import MIMEText
import base64
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import time
import email

class GmailTask:
    def __init__(self):
        # Ask the user if they wish to sign in
        print("Do you wish to sign-in with Google?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Load credentials from the 'token.json' file
            creds = self.load_credentials()
            if not creds or not creds.valid:
                creds = self.sign_in()
            self.service = build('gmail', 'v1', credentials=creds)
        elif choice == '2':
            # The user chose not to sign in, so stop the program
            raise SystemExit("User chose not to sign in.")
        else:
            print("Invalid choice. Please try again.")

    def load_credentials(self):
        if os.path.exists('token.json'):
            return Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.send'])
        return None

    def sign_in(self):
        creds = None
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'packages\Credentials.json', ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.send'])
            creds = flow.run_local_server(port=0)
        with open('packages\\token.json', 'w') as token:
            token.write(creds.to_json())
        return creds

    def sendEmail(self, recipient_email, subject, body):
        # Create a simple email message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = "your-email@gmail.com"
        msg['To'] = recipient_email

        # Encode the message and send it
        encoded_msg = base64.urlsafe_b64encode(msg.as_bytes()).decode()
        message = self.service.users().messages().send(userId="me", body={"raw": encoded_msg}).execute()

        print(f"Message sent. Id: {message['id']}")

    def CheckInbox(self):
        # Request a list of the 10 most recent messages
        result = self.service.users().messages().list(userId='me', maxResults=10).execute()
        messages = result.get('messages')

        # Initialize the index variable
        i = 1

        # Iterate over all emails
        for msg in messages:
            txt = self.service.users().messages().get(userId='me', id=msg['id']).execute()
            try:
                payload = txt['payload']
                headers = payload['headers']
                for d in headers:
                    if d['name'] == 'Subject':
                        subject = d['value']
                    if d['name'] == 'From':
                        sender = d['value']
                print(f'{i} Subject: {subject}')
                print('  From: ', sender)
            except Exception as e:
                print('An error occurred: %s' % e)
            i += 1
            
if __name__ == "__main__":
    gmail_task = GmailTask()
    while True:
        print("1. Check Inbox")
        print("2. Compose Email")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Refresh Inbox
            gmail_task.CheckInbox()# assuming the CheckInbox task is at index 0
        elif choice == '2':
            # Compose Email
            recipient_email = input("Enter the recipient's email address: ")
            subject=input("Your sunject: ")
            body=input("Your email body: \n")
            gmail_task.sendEmail(recipient_email, subject, body) # assuming the Run task is at index 1
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

    time.sleep(0.5)
