#bir tümörün kararlılık durumunu analiz eden ÖZEL FONKSİYONUMUZ
def tumor_analiz_et(hastanin_adi, simdiki_boyut, eski_boyut):
    print("---KLİNİK RAPOR---")
    print("Hasta:", hastanin_adi)


    #büyüme miktarını hesapla
    degisim=simdiki_boyut-eski_boyut

    if degisim>0:
        print(f"UYARI: Tümör {degisim:.2f} cm BÜYÜDÜ! Acil tedavi revizyonu.")
    elif degisim<0:
        print(f"BAŞARI: Tümör {abs(degisim):.2f} cm KÜÇÜLDÜ! Tedavi işe yarıyor.")
    else:
        print("DURUM STABİL: Tümör boyutunda değişim yok.")

#yazdığımız fonksiyonutest edelim (farklı hastalar için çalıştıralım)
tumor_analiz_et("Mehmet Öz", 4.2, 3.5) #büyüyen tümör
print("\n")
tumor_analiz_et("Ayşe Kaya", 2.1, 2.8) #küçülen tümör




def pet_cihazi_kalibrasyon(olculen_enerji_kev):
    print("---PET DEDEKTÖR ANALİZİ---")
    #PET cihazında teorik olarak ölçülmesi gereken foton enerjisi 511 kev'dir.
    hedef_enerji=511

    if olculen_enerji_kev==hedef_enerji:
        print(f"SİSTEM ONAYLADI: Ölçülen enerji {olculen_enerji_kev} keV. Kanser teşhisi için veri güvenilir.")
    else:
        sapma = abs(olculen_enerji_kev-hedef_enerji)
        print(f"HATA UYARISI: Ölçülen enerji {olculen_enerji_kev} keV! sapma var. Cihazı kalibre edin.")

#yazdığınız gelişmiş medikal fonksiyonu test edin:
pet_cihazi_kalibrasyon(511) #Doğru çalışan dedektör
print("\n")
pet_cihazi_kalibrasyon(495) #hatalı\sapmış dedektör
