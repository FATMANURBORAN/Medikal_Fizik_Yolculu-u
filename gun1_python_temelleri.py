#bir hastanın klinik verilerini tanımlıyoruz
hasta_adi="Ahmet Yılmaz"
hasta_yasi=42
tumor_boyutu_cm=3.4

#verileri ekrana yazdırıyoruz
print("Hasta Adı:", hasta_adi)
print("Yaşı:", hasta_yasi)
print("Tümör Boyutu (cm):", tumor_boyutu_cm)
#tümör boyutuna göre karar veren algoritma
if tumor_boyutu_cm>2.0:
    print("DİKKAT: Tümör boyutu kritik sınırın üzerinde! İleri tetkik ve tedavi planlaması gerekiyor.")
else:
    print("DURUM STABİL: Tümör boyutu kontrol sınırları içinde. Rutin takibe devam edilebilir.")
#bir hastanın son 5 gündeki tümör boyutu değişimleri (cm cinsinden liste)
tumor_gecmisi=[3.1, 3.2, 3.4, 3.5, 3.7]

#döngü kullanarak her günün verisini ekrana yazdıralım
gun=1
for boyut in tumor_gecmisi:
    print(gun, ".Gün Ölçülen Boyut:", boyut, "cm")
    gun=gun+1
#tümör boyutlarının ortalamasını hesaplayan algoritma
toplam_boyut=sum(tumor_gecmisi) #listedeki tüm sayıları toplar
gun_sayisi=len(tumor_gecmisi) #listede kaç gün olduğunu bulur

ortalama_tumor_boyutu=toplam_boyut/gun_sayisi

print("Hastanın 5 Günlük Ortalam Tümör Boyutu:", ortalama_tumor_boyutu, "cm")
