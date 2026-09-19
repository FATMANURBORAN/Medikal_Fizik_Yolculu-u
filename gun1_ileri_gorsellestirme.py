import matplotlib.pyplot as plt

# 1. GÜN: İLERİ SEVİYE KLİNİK VERİ GÖRSELLEŞTİRME
# 5 günlük tümör verilerimiz ve günler
tumor_gecmisi = [3.1, 3.2, 3.4, 3.5, 3.7]
gunler =

# Grafik çizim ve etiketleme ayarları
plt.plot(gunler, tumor_gecmisi, marker='o', color='r', linestyle='--')
plt.title("Hastanın Tümör Boyutu Değişimi (Klinik Rapor)")
plt.xlabel("Günler")
plt.ylabel("Boyut (cm)")
plt.grid(True)

# Grafiği ekranda göster
plt.show()
