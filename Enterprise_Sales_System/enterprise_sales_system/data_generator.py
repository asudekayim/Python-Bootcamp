import numpy as np
import pandas as pd

class DataGenerator:
    def __init__(self, num_rows, seed=None):
        # kaç satır veri üretilecek
        self.num_rows = num_rows
        
        self.seed = seed
        if self.seed is not None:
            np.random.seed(self.seed)
        
        self.urunler = {
            "Telefon" : 35000,
            "Tablet" : 15000,
            "Laptop" : 45000,
            "Monitör" : 10000,
            "Kulaklık" : 4000
        }
        self.sehirler = {
            "İstanbul" : 0.4, 
            "Ankara" : 0.2, 
            "İzmir" : 0.2, 
            "Bursa" : 0.1, 
            "Antalya" : 0.1
        }
        
        self.aylar = {
            "Ocak": 0.06, "Şubat": 0.06, "Mart": 0.15, 
            "Nisan": 0.06, "Mayıs": 0.06, "Haziran": 0.06,
            "Temmuz": 0.06, "Ağustos": 0.06, "Eylül": 0.06,
            "Ekim": 0.06, "Kasım": 0.25, "Aralık": 0.06  
            }
        
    def generate_data(self):
        musteriID = np.random.randint(1000,9999, size=self.num_rows)
        urun = np.random.choice(list(self.urunler.keys()), size=self.num_rows)
        sehir = np.random.choice(list(self.sehirler.keys()), size=self.num_rows, p=list(self.sehirler.values())) # string array
        sehir = sehir.astype(object) # çözüm: "object" tipi hem metin hem de gerçek NaN tutabilir
        ay = np.random.choice(list(self.aylar.keys()), size=self.num_rows, p=list(self.aylar.values()))

        taban_fiyatlar = np.array([self.urunler[i] for i in urun])
        gurultu = np.random.uniform(0.95, 1.05, size=self.num_rows)
        satisTutari = np.round((taban_fiyatlar * gurultu),2)

        hata_adedi = int(self.num_rows*0.05)
        hatali_index = np.random.choice(self.num_rows, size=hata_adedi, replace=False)
        satisTutari[hatali_index] = np.nan
        sehir[hatali_index] = np.nan 
        # --> 'sehir' numpy string bir dizisidir. (object olarak tanımlamadan önce)
        # np.nan denildiğinde nan string'e çevrilir ve string bir nan elde ederiz. Bunu istemeyiz.
        
        outlier_adedi = int(self.num_rows * 0.01)
        outlier_index = np.random.choice(self.num_rows, outlier_adedi, replace=False)
        satisTutari[outlier_index] = satisTutari[outlier_index] * 50

        sozluk = {
            "Müşteri ID" : musteriID,
            "Ürün" : urun,
            "Satış Tutarı" : satisTutari,
            "Şehir" : sehir,
            "Ay" : ay
        }
        
        df = pd.DataFrame(sozluk)
        return df