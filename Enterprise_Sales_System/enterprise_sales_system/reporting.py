import pandas as pd
import numpy as np

class Report:
    def __init__(self, df_dict):
        # df.dict: Dışarıdan gelen, içinde analiz sonuçlarımızın olduğu bir sözlük 
        # (Örn: {"Satislar": df1, "Sehirler": df2})
        self.df_dict = df_dict
    
    def generate_info(self):
        info = []

        if "Şehir Analizi" in self.df_dict:
            city_df = self.df_dict["Şehir Analizi"]
            # df_dict içerisinde 'city_based' tablosu varsa üzerinde 
            # işlem yapabilmek için 'city_df' değişkenine atadık.
            
            avg_sales = city_df["Toplam Satış"].mean()
            # baraj puanı

            risky_cities = city_df[city_df["Toplam Satış"] < avg_sales]["Şehir"].tolist()
            # ortalamadan küçük şehirleri listeledik

            if risky_cities:
                info.append(f"RISK UYARISI: {', '.join(risky_cities)} şehirlerinde...")

        if "Ürün Analizi" in self.df_dict:
            prod_df = self.df_dict["Ürün Analizi"]
            top_products = prod_df.sort_values(by="Toplam Satış", ascending=False).head(2)["Ürün"].tolist()
            # en çok satan 2 ürün
            info.append(f"STOK ARTIRIM ÖNERİSİ: {', '.join(top_products)} ürünlerine talep çok yüksek...")

        return pd.DataFrame({"Sistem Özeti": info})

    def toExcel(self, file_name="Rapor.xlsx"):
        try:
            df_info = self.generate_info()

            with pd.ExcelWriter(file_name, engine = "openpyxl") as writer:
            # writer takma adıyla dosya konteyner gibi açtık
                
                df_info.to_excel(writer, sheet_name="Yönetici Özeti", index=False)
                # ilk sayfa yönetici özeti
                
                for sheet_name, df in self.df_dict.items():
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
                    # sözlükteki her df'yi kendi ismiyle bir sekme olarak kaydettik
            
            print(f"Rapor '{file_name}' adıyla başarıyla oluşturuldu.")

        except Exception as e:
            print(f"Excel oluşturulurken bir hata oluştu: {e}")