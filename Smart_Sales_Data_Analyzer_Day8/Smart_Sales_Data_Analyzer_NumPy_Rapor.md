# Smart Sales Data Analyzer

Projenin amacı, NumPy kütüphanesiyle 7 günlük, 5 ürünlü satış verisinin analiz edilmesi.

# Giriş — Proje Hakkında

Bu proje, bir işletmenin haftalık satış verilerini NumPy kullanarak analiz etmeyi amaçlamaktadır. Veriler 7×5'lik bir matris yapısında modellenmiş; toplam, ortalama, maksimum-minimum hesaplamaları, axis mantığını anlama çalışmaları yapılmıştır.

# Kullanılan Python Konuları

- **NumPy Array:** Tüm satış verisinin tek bir iki boyutlu yapıda tutulmasını sağlar.
- **Array Özellikleri:** .shape, .ndim, .dtype, .size ile verinin yapısı incelenir.
- **İstatistiksel Metotlar:** .sum(), .mean(), .max(), .min() ile veri özetlenir.
- **Eksen İşlemleri**: axis=0 sütun bazlı, axis=1 satır bazlı toplamlar üretir.
- **Dizi Dönüşümleri:** .reshape(), .transpose(), .flatten(), .ravel() ile veri farklı biçimlere taşınır.

# Kavramsal Sorular

**NumPy neden listelerden daha hızlıdır?**

    Python listelerinde her eleman ayrı bir nesne olarak bellekte tutulur. NumPy ise tüm elemanları bellekte yan yana, bitişik bir blok halinde depolar. Bu sayede işlemci veriyi önbelleğe tek seferde yükler ve döngüler Python yorumlayıcısı yerine derlenmiş C kodu düzeyinde çalışır.

**Array kavramı veri analizinde neden kritiktir?**

    Satışlar hem ürüne hem güne göre ayrışır. Array bu çok boyutlu yapıyı temsil eder.

**Axis mantığı neden sık karıştırılır?**

    Çoğu kişi axis=0'ı satırlar için sanarken, axis=0 satır ekseni boyunca aşağı inerek her sütun için bir sonuç üretir. Pratik kural şudur: axis=0 sonucun satır sayısını azaltır, axis=1 ise sütun sayısını azaltır. Bu projede axis=0 her ürünün haftalık toplamını, axis=1 ise her günün tüm ürünler üzerindeki toplamını vermiştir.

**Bu projede NumPy hangi problemi çözdü?**

    Satış matrisi Python listeleriyle modellenebilirdi ama satırların eşit uzunlukta kalacağına dair güvence olmaz ve her analiz için ayrı döngüler yazılması gerekirdi. NumPy bu üç problemi birden çözmektedir: veriyi yapısal olarak bir matrise dönüştürür, analizleri tek satırlık ifadelerle yapar ve reshape/transpose gibi dönüşümleri veriyi kopyalamadan gerçekleştirir.

# Sonuç ve Değerlendirme

Proje, NumPy'ın sağladığı avantajların yalnızca hız değil aynı zamanda yapısal netlik olduğunu göstermiştir. Verinin nasıl modellendiğini ve axis mantığını kavramak; ileride pandas, scikit-learn veya derin öğrenme kütüphaneleriyle çalışırken sağlam bir zemin oluşturmaktadır.
