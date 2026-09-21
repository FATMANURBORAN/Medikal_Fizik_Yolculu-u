# ==========================================================
# MEDİKAL FİZİK YÜKSEK LİSANS HAZIRLIĞI - 3. GÜN ÇALIŞMASI
# ==========================================================
import numpy as np

# 1. Kalıtsallık (Inheritance) ile Tıbbi Cihaz Mimari Tasarımı
class TibbiCihaz:
    def __init__(self, marka, model, oda_numarasi):
        self.marka = marka
        self.model = model
        self.oda_numarasi = oda_numarasi

    def sistem_durumu(self):
        print(f"--- SİSTEM KONTROLÜ ---")
        print(f"Cihaz: {self.marka} {self.model} | Konum: Oda {self.oda_numarasi}")
        print("Durum: Çalışmaya Hazır (Ready)")

class TomografiCihazi(TibbiCihaz):
    def __init__(self, marka, model, oda_numarasi, x_isini_voltaji_kv):
        super().__init__(marka, model, oda_numarasi)
        self.voltaj = x_isini_voltaji_kv

    def radyasyon_raporu(self):
        self.sistem_durumu()
        print(f"Tüp Voltajı: {self.voltaj} kV | DİKKAT: Kontrollü Radyasyon Alanı!\n")

# 2. Yapay Zekâ / Veri Artırma (Data Augmentation) Matris Yapısı
orijinal_goruntu = np.array([,
 ,
    [1, 4, 1]
])

# 3. Nükleer Tıp Kolimatör Çözünürlüğü Analiz Fonksiyonu
def kolimator_cozunurluk_hesapla(d, l, b):
    print("--- NÜKLEER TIP CİHAZ ANALİZİ ---")
    R_g = (d * (l + b)) / l
    print(f"Delik Çapı (d): {d} mm | Delik Uzunluğu (l): {l} mm")
    print(f"Hasta - Cihaz Mesafesi (b): {b} mm")
    print(f"Hesaplanan Sistem Çözünürlüğü (Rg): {R_g:.2f} mm")
    
    if R_g <= 3.0:
        print("SİSTEM DURUMU: MÜKEMMEL! Görüntü çok net, küçük tümörler kolayca teşhis edilebilir.")
    else:
        print("SİSTEM DURUMU: UYARI! Görüntü bulanık. Daha net teşhis için hastayı cihaza yaklaştırın.")
    print("-" * 40 + "\n")

# Sistem Testleri
print("=== SİSTEM MİMARİ VE VERİ TESTİ ===")
cihaz_bt = TomografiCihazi("Siemens", "Somatom", "102-A", 120)
cihaz_bt.radyasyon_raporu()

print("=== NÜKLEER TIP KALİBRASYON TESTLERİ ===")
kolimator_cozunurluk_hesapla(2, 40, 0)
kolimator_cozunurluk_hesapla(2, 40, 160)
