# Enterprise Sales Intelligence System -Teknik Rapor

Gerçek dünya verilerini simüle eden, temizleyen, analiz eden ve sonra Excel üzerinde raporlayan modüler bir Python projesidir.

## Proje Yapısı

```
enterprise_sales_system/
│
├── data_generator.py   # Sentetik satış verisi üretimi
├── preprocessing.py    # Veri temizleme ve özellik mühendisliği
├── analytics.py        # Gruplama ve performans analizleri
├── reporting.py        # Excel raporu ve yönetici özeti üretimi
└── main.ipynb          # Pipeline'ı uçtan uca çalıştıran notebook
```

## Neden Modüler Mimari?

Proje tek bir dosyada yazılabilirdi. Ancak tek bir dosyada yazıldığında kod karmaşıklığı, okuma zorluğu gibi olumsuzluklar ortaya çıkmaktadır. Bu nedenle 4 ayrı modüle bölündü.

- Her modül yalnızca kendi işini yapıyor. Bu sayede karmaşıklık azalıyor ve okunabilirlik artıyor.
- Test edilebilirlik açısından büyük bir bağımsızlık avantajı sağlar. Tek bir modül için tüm modülleri çalıştırmaya gerek yoktur.

## Neden NumPy + Pandas?

Bu iki kütüphane birlikte kullanıldığında çok hızlı işlemler yapabiliyorlar.

- Numpy, geliştiriciyi ayrı ayrı koşul, kontrol yapıları oluşturmaktan, diziler üzerinde tek tek gezmekten kurtarıyor.
- Pandas, veri çerçeveleri oluşturarak, o çerçeveleri sorgulama, filtreleme, gruplama gibi işlemleri kolaylıkla yapabilmeyi sağlıyor.

## Eksik Veri Kararları

```python
hata_adedi = int(self.num_rows*0.05)
hatali_index = np.random.choice(self.num_rows,size=hata_adedi, replace=False)
satisTutari[hatali_index] = np.nan
sehir[hatali_index] = np.nan
```

**1.** Hata adedi, kasıtlı olarak tüm satırların %5'i kadar olacak şekilde ayarlandı.  
**2.** Hatalı olacak satırlar için numpy ile random seçme yapıldı.  
**3.** Sadece 'Satış Tutarı' ve 'Şehir' sütunları için ayarlandı.

```
Satış tutarı için medyan ile doldurma yapılmıştır. Çünkü veri setinde olan aykırı değerler, normal değerlerin yaklaşık 50 katı civarıdır. Ortalama, bu aykırı değerlerin düşüklüğünden ve yüksekliğinden etkilenir ve gerçekçi olmayan değerler verir. Bu değerler de veri setini olumsuz etkiler. Medyan ise ortadaki değeri aldığı için aykırı değerlere karşı daha gerçekçi ve doğrudur.

Şehir için 'Bilinmeyen' değer ile doldurma yapılmıştır. Şehir string bir değer olduğu için sayısal bir değerle doldurma yapılamazdı. Eksik olan bilginin olduğu satırı silmek ise veri kaybına yol açardı.
```

## `groupby` ile İş Kararı Üretmek

**groupBy**, veriyi istenilen kategoriye göre gruplamak için kullanılmaktadır. Örneğin İstanbul'daki ürünleri bir gruba, Ankara'daki ürünleri bir gruba ayır şeklinde gruplama yapmaktadır. Yani ham veriyi özetleyerek anlamlı bir şekilde ortaya sunmaktadır.

## Kullanılan Başlıca Metodlar

`np.random.choice` : Ratgele şehir, ürün, ay seçimi

`np.where` : Koşula göre etiketleme

`fillna` : Eksik değerleri doldurma

`str.strip` / `str.capitalize` : Metin temizleme ve standardizasyon

`groupby` + `agg` : Gruplama ve fonksiyonel uygulama

`pct_change` : Bir önceki aya göre değişim hesaplama

`sort_values` + `groupby().head(1)` : Aya göre en çok satan ürünü bulma

`pd.ExcelWriter` : Çok sekmeli Excel raporu üretimi

## Notlar

- Veri seti her çalıştırmada aynı sonucu vermesi için `seed=42` ile sabitlenmiştir.
