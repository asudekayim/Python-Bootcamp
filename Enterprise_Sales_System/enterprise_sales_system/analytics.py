import pandas as pd
import numpy as np

def get_city_performance(df):
    result = df.groupby("Şehir")["Satış Tutarı"].agg(["sum","max","min"]).reset_index()
    result.columns = ["Şehir", "Toplam Satış", "Maksimum Satış", "Minimum Satış"]
    return result

def get_product_performance(df):
    result = df.groupby("Ürün")["Satış Tutarı"].agg(["sum","count"]).reset_index()
    result.columns = ["Ürün", "Toplam Satış", "Satış Adedi"]
    return result 

def get_monthly_performance(df):
    result = df.groupby("Ay")["Satış Tutarı"].agg(["sum","mean"]).reset_index()
    result["Aylık_Değişim_%"] = (result["sum"].pct_change() * 100).round(2)
    result.columns = ["Ay", "Toplam Satış", "Ortalama Satış","Aylık Değişim(%)"]
    return result  

def calculate_performance_score(df, columnName):
    numpy_dizi = df[columnName].to_numpy()
    dizi_max = np.max(numpy_dizi)
    dizi_min = np.min(numpy_dizi)
    normalization = (numpy_dizi - dizi_min)/(dizi_max - dizi_min) * 100
    df["Performans Skoru"] = normalization.round(2)
    newdf = df.sort_values(by = "Performans Skoru", ascending = False)
    return newdf

def get_monthly_best_seller(df):
    result = df.groupby(["Ay","Ürün"])["Satış Tutarı"].sum().reset_index()
    result_df = result.sort_values(by="Satış Tutarı", ascending = False).groupby("Ay").head(1)
    return result_df