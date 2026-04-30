import numpy as np
import pandas as pd
import data_generator as dg

def missing_values(df):
    try:
        print("--- Veri Genel Bilgisi ---")
        #genel bilgi
        df.info()
        
        print("\n--- İstatistiksel Özet ve Eksik Veri Sayısı ---")
        #tablo özeti
        #print(df.describe())
        
        #print("\n--- Eksik Veri Sayısı ---")
        #eksik veriler
        #print(df.isnull().sum())
        
        return df.describe(), df.isnull().sum() 
        
    except Exception as e:
        print(f"Beklenmedik bir hata oluştu: {e}")
        return None

def fill_missing_values(df):
    try:
        # mean ile doldursaydık aykırı bir değer yüzünden aykırı değerler ile doldurulacaktı
        # o yüzden median ile orta değerler arasında doldurmayı tercih ettik
        median_value = df['Satış Tutarı'].median()
        df['Satış Tutarı'] = df['Satış Tutarı'].fillna(median_value)

        # sağ, sol boşluk temizliği
        df['Şehir'] = df['Şehir'].str.strip()
        
        # boş değerleri bilinmeyen ile doldurduk
        df['Şehir'] = df['Şehir'].fillna("Bilinmeyen")
        
        # string nan değerleri bilinmeyen ile doldurduk(sahte nan)
        #df['Şehir'] = df['Şehir'].replace("nan","Bilinmeyen")
        # bu satıra artık gerek yok çünkü object tanımlaması yaptık
        
        # büyük-küçük harf
        df['Şehir'] = df['Şehir'].str.capitalize()
        
        return df
    except Exception as e:
        print(f"Doldurma sırasında bir hata oluştu: {e}")
        return df

def add_features(df):
    try:
        df['KDV Dahil Tutar'] = df['Satış Tutarı'] * 1.2
        # numpy ile koşul kontrolü
        df['Müşteri Etiketi'] = np.where(df['Satış Tutarı'] > 20000, "VIP", "STANDART")

        return df
        
    except Exception as e:
        print(f"Özellik eklenirken hata oluştu: {e}")
        return df