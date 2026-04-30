from datetime import datetime
from models import Expense
import random

def get_user_expenses():
    expenses = []
    
    while True:
        try:
            amount = float(input("Harcama giriniz:"))
            
            if amount == 0:
                print("Çıkış yapılıyor...")
                break
            
            if amount < 0:
                print("Pozitif bir sayı giriniz")
                continue
                
            category = input("Kategori giriniz:")
            
            exp = Expense(amount, category)
            expenses.append(exp)
        
        except ValueError:
            print("Lütfen geçerli değerler giriniz!")
            
    return expenses

def generate_random_notification():
    messages = [
    "Bugünkü harcamalarını kontrol etmeyi unutma 💸",
    "Yeni bir harcama eklendi 📊",
    "Bütçeni aşmaya yaklaşıyorsun ⚠️",
    "Tebrikler! Bugün tasarruf modundasın 💰",
    "Harcamalarını takip etmeye devam et 👍",
    "Küçük harcamalar birikerek büyür 🧠",
    "Bütçe planına sadık kalıyorsun, harika! 🎯",
    "Dikkat! Gereksiz harcama yapmış olabilirsin 👀",
    "Finansal hedeflerine bir adım daha yaklaştın 🚀",
    "Bugün harcama yapmadan günü kapatabilirsin 💪"
    ]
    message = random.choice(messages)
    

    return f"{message}"