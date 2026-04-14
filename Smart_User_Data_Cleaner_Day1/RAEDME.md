# Smart User Data Cleaner

Elde bulunan hatalı verilerin, Python'un string metotlarıyla temizlenerek daha okunabilir bir hale getirilmesi.

## Giriş - Proje Hakkında

Projenin amacı, gerçek hayatta karşılaşabileceğimiz problemlere karşı kendimizi geliştirmektir. Hatalı bir veriyle karşılaştığımızda temel olarak neler yapmamız gerektiğini Python'un temelleriyle öğretmektedir.

Veri temizleme, verinin anlaşılabilirliği için çok önemlidir. Veri okunabilir olmazsa veriyi kullanacak olan kişi zorluk yaşayabilir ve bu zorluk da süreci uzatabilir.

Bu projede kullandığımız string metotlar, boşlukları temizlemek, büyük-küçük harf düzeltmesi yapmak, veriyi anlamlı parçalara ayırmak gibi işlemleri yapmaktadır.

## Kullanılan Python Konuları

**Değişkenler:** Integer, string ve float veri tipinde değişkenler kullanılmıştır. Yapılacak olan işlemin anlamına uygun isimler kullanılarak değişkenler belirlenmiştir. Değişkenlerin her birinin anlamlı bir değeri vardır.

**String Veri Tipi:** Metin türünde verileri tutmaktadır. Projeden örnek olarak isim ve mail verilebilir.

**String Slicing:** Belirlenmiş indeksler arasındaki bir değeri almak, onun üzerinde işlemler yapmaktır.

**String metodları**

- **strip():** Metnin başındaki ve sonundaki boşlukları temizlemek için kullanılır.
- **split():** Metni parçalara ayırmak için kullanılır.
- **lower():** Metnin tamamını küçük harfe çevirmek için kullanılır.
- **find():** Metnin içinde geçen istenilen bir kısmı bulmak için kullanılır.

**int ve float Dönüşümleri:** Değişkenleri int veya float tipinde parantez içine almaktır. string tipinden float tipine veya string tipinden int tipine dönüşüm yapılabilir.

## Veri Temizleme Süreci

Verideki promblemler şunlardı:

- Düzensiz boşluklar
- Büyük-küçük harf düzensizliği
- Uygun bir şekilde yazılmamış olan mail adresi
- Matematiksel işlem yapılabilecek olan değişkenlerin string veri tipinde verilmesi

**ÇÖZÜM:** İlk olarak metotlarla boşluklar giderildi, parçalara ayrıldı. Parçalardan gerekli olanlar için büyük-küçük harf düzeltilmesi yapıldı. Daha sonra sayısal veri olarak kullanılabilecek veriler için gerekli veri dönüşümleri yapıldı. Sonda mail adresi için de tekrar büyük-küçük harf düzeltilmesi yapıldı ve kod haline getirildi. Projenin bitiminde tüm değişkenler düzgün bir şekilde gösterildi.

**Yanlış girilmiş verilerin sisteme etkisi:** Yanlış girilmiş veriler, zaman ve maliyet açısından kayıplara yol açabilir. Doğru şekilde girmek, gruplandırmak çok önemli bir olaydır.

# Sonuç ve Değerlendirme

Projedeki isim-soyisim, yaş, boy ve mail adresi sorunları düzenlenerek uygun bir şekilde alınmıştır.

Gerçek hayatta form verisi temizleme, CSV formatındaki düzensiz verileri düzenleme gibi işlemlerde kullanılmaktadır.

**Kazanılan Python Becerileri:** String veri tipindeki değişkenleri belirli metotlarla temizleyip düzenlemek ve veri tipi dönüşümü yapmak.
