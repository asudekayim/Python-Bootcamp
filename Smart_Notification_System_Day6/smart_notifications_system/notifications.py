from datetime import datetime

class Notification:
    def __init__(self,message):
         # boş mesaj kontrolü yaptık
        if not message.strip():
            raise ValueError("Bildirim mesajı boş")
        self.message = message
        self.created_at = datetime.now().strftime("%d.%m.%Y %H:%M")

    def send(self):
        pass

    def __str__(self):
        #return f"{self.message} ({self.created_at})"
        return f"{self.message}"
    
    def __len__(self):
        return len(self.message)

# EmailNotification(Notification)
class EmailNotification(Notification):
    def send(self):
        print(f"Email gönderildi: {self.message}")

# SMSNotification(Notification)
class SMSNotification(Notification):
    def send(self):
        print(f"SMS gönderildi: {self.message}")

# PushNotification(Notification)
class PushNotification(Notification):
    def send(self):
        print(f"Push bildirimi gönderildi: {self.message}")