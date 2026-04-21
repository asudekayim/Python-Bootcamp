# Smart Notification System

Proje, Python'ın OOP(Nesne Yönelimli Programlama) kavramlarının kullanılarak farklı bildirim türlerinin tek bir yerden yönetildiği bir sistemdir.

## Giriş - Proje Hakkında

Projenin amacı, gerçek hayatta karşılaşabileceğimiz bildirim türlerini OOP ile modellemektir. Class, attribute, inheritance, polymorphism gibi temel kavramların nasıl kullanıldığını göstermektedir.

E-posta, SMS ve push bildirimleriyle farklı farklı bildirimler gönderilmiştir. Hepsinin parent class'ı vardır. Kodun kullanılabilirliğini ve sürdürülebilirliğini artır. Child sınıflar inheritance yani miras alarak kendi metotlarını düzenlemiş ve kullanmışlardır. Try/except hata kontrolüyle boş mesajlar için kontrol yapılmıştır.

## Kullanılan Python Konuları

- **Sınıflar (Class)**

- **Kalıtım (Inheritance):** Child sınıflar Notification'dan miras almıştır. Bu sayede attribute'lar ve metotlar tekrar yazılmadan tüm alt sınıflarda kullanılabilmiştir.

- **Polimorfizm (Polymorphism):** Her alt sınıf send() metodunu kendi ihtiyacına göre yeniden tanımlamıştır.

- **init, str, len** gibi metotlar, nesnelerin farklı durumlarlarda birbirleriyle düzgün bir şekilde çalışabilmesi için önemlidir.

- **Hata Yönetimi (try/except)**

- **Modüler Yapı:** notifications.py, utils.py, main.ipynb Fazla kod yüzünden oluşan karmaşıklık bu şekilde engellenmiştir. Her dosyanın amacı farklıdır. Tekrar kullanılabilirlik ve okunabilirlik artmıştır.

# Sonuç ve Değerlendirme

Bu projede Notification base class'ı üzerinden EmailNotification, SMSNotification ve PushNotification alt sınıfları oluşturulmuştur. Nesnelerin farklı durumlarlarda birbirleriyle düzgün bir şekilde çalışabilmesi için özel metotlar kullanılmıştır. Boş mesajlar için oluşabilecek hatalar, try/except ile önlenmeye çalışılmıştır.
