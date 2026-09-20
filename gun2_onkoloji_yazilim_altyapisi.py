# ==========================================================
# MEDİKAL FİZİK YÜKSEK LİSANS HAZIRLIĞI - 2. GÜN ÇALIŞMASI
# ==========================================================
import math

# 1. Kapsülleme (Encapsulation) ile Güvenli Hasta Dosyası Tasarımı
class GuvenliHastaDosyasi:
    def __init__(self, isim, ilk_boyut):
        self.isim = isim
        self.__tumor_boyutu = ilk_boyut  # Gizli değişken

    def tumor_boyutu_guncelle(self, yeni_boyut):
        if yeni_boyut < 0:
            print("HATA: Tümör boyutu negatif bir değer olamaz! Güncelleme reddedildi.")
        else:
            self.__tumor_boyutu = yeni_boyut
            print(f"Başarılı: {self.isim} için tümör boyutu {yeni_boyut} cm olarak güncellendi.")

    def rapor_goruntule(self):
        print(f"Hasta: {self.isim} | Güncel Tümör Boyutu: {self.__tumor_boyutu} cm\n")

# 2. Üst Düzey Radyasyon Zırhlama ve HVL Analiz Fonksiyonu
def zirhlama_analizi_et(I0, mu, x):
    print("--- RADYASYON ZIRHLAMA RAPORU ---")
    hvl = 0.693 / mu
    print(f"Malzemenin Yarı Değer Kalınlığı (HVL): {hvl:.3f} cm")
    
    kalan_siddet = I0 * math.exp(-mu * x)
    azalma_orani = (1 - (kalan_siddet / I0)) * 100
    
    print(f"Duvar Kalınlığı: {x} cm")
    print(f"Kalan Radyasyon Şiddeti: {kalan_siddet:.2f}")
    print(f"Radyasyon Durdurma Başarısı: %{azalma_orani:.2f}\n")

# Sistem Testleri
print("=== SİSTEM GÜVENLİK TESTİ ===")
hasta = GuvenliHastaDosyasi("Hasan Can", 3.5)
hasta.tumor_boyutu_guncelle(-1.2)  # Hata vermeli

print("\n=== KLİNİK ZIRHLAMA ANALİZİ ===")
zirhlama_analizi_et(100, 2.31, 0.9)  # 8 kat azaltma testi
