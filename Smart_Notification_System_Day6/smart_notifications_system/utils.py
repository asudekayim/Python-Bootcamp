import random
from datetime import datetime

def generate_message():
    bildirimler = [
        "Fotoğrafın beğenildi!📸",
        "İndirim fırsatını kaçırma!🎉",
        "Toplantı 15 dk sonra başlıyor.🗓️",
        "450 TL harcama yapıldı.💳",
        "Su içme vakti geldi!💧",
        "Yeni cihazdan giriş yapıldı.🚨",
        "Kargon dağıtıma çıktı!📦",
        "Günlük ödülün seni bekliyor!✨",
        "Son Dakika: Dev iş birliği!🚀",
        "Bugünkü dersini unutma!🔥"
    ]
    return random.choice(bildirimler) + f"({datetime.now().strftime('%d.%m.%Y %H:%M')})"    

