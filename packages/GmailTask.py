from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from email.mime.text import MIMEText
import base64
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path

class GmailTask:
    def __init__(self):
        # Load credentials from the 'token.json' file
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.send'])
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.send'])
                creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        self.service = build('gmail', 'v1', credentials=creds)

    # Rest of your GmailTask methods...

    def GmailTask_Run(self):
        # Create a simple email message
        msg = MIMEText("This is the body of the email.")
        msg['Subject'] = "This is the subject of the email."
        msg['From'] = "your-email@gmail.com"
        msg['To'] = "recipient-email@gmail.com"
        
        # Encode the message and send it
        encoded_msg = base64.urlsafe_b64encode(msg.as_bytes()).decode()
        message = self.service.users().messages().send(userId="me", body={"raw": encoded_msg}).execute()

        print(f"Message sent. Id: {message['id']}")

    def GmailTask_CheckInbox(self):
        # Request a list of the 10 most recent messages
        result = self.service.users().messages().list(userId='me', maxResults=10).execute()
        messages = result.get('messages')

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
                print('Subject: ', subject)
                print('From: ', sender)
            except Exception as e:
                print('An error occurred: %s' % e)
