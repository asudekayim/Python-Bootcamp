class Notification:
    def __init__(self, message):
        self.message = message

    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Email gönderildi:", self.message)

class SMSNotification(Notification):
    def send(self):
        print("SMS gönderildi:", self.message)