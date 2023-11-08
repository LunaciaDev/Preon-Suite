from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import time
import base64

from PySide6.QtCore import Slot, Signal, QObject

class GmailTask(QObject):
    credentialsValidity = Signal(bool)
    inboxPayload = Signal(list)
    sentEmail = Signal()

    signedIn = False
    creds = None

    def getCredentialsValidity(self):
        self.credentialsValidity.emit(self.signedIn)

    def __init__(self):
        super(GmailTask, self).__init__()

    @Slot()
    def signIn(self):
        self.load_credentials()

        if self.creds and self.creds.expired and self.creds.refresh_token:
            self.creds.refresh(Request())

        if self.creds and self.creds.valid:
            self.service = build('gmail', 'v1', credentials=self.creds)
            self.signedIn = True
            self.getCredentialsValidity()
            self.CheckInbox()

    def load_credentials(self):
        if os.path.exists('./packages/token.json'):
            self.creds = Credentials.from_authorized_user_file('./packages/token.json', ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.send'])
            return
        
        self.creds = None

    def refreshToken(self):
        if self.creds and self.creds.expired and self.creds.refresh_token:
            self.creds.refresh(Request())   

        with open(r'./packages/token.json', 'w') as token:
            token.write(self.creds.to_json())
    
    @Slot()
    def generateToken(self):
        flow = InstalledAppFlow.from_client_secrets_file(
                r'./packages/Credentials.json', ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.send'])
        
        try:
            self.creds = flow.run_local_server(port=0)
        except:
            pass
        else:
            with open(r'./packages/token.json', 'w') as token:
                token.write(self.creds.to_json())

            self.signIn()

    @Slot(str, str, str)
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
        self.sentEmail.emit()

    @Slot()
    def CheckInbox(self):
        if not self.signedIn:
            return

        # Request a list of the 10 most recent messages
        result = self.service.users().messages().list(userId='me', maxResults=10).execute()
        messages = result.get('messages')
        emailPayload = []

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

                emailPayload.append({"sender": sender, "subject": subject})

            except Exception as e:
                print('An error occurred: %s' % e)
        
        self.inboxPayload.emit(emailPayload)
