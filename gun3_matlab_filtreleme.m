% 3. GÜN: MATLAB TIBBİ GÖRÜNTÜ FİLTRELEME VE GÜRÜLTÜ TEMİZLEME
Doku_Temiz = zeros(100, 100); 
Doku_Temiz(40:60, 40:60) = 5;

Gurultu = randn(100, 100) * 0.8;
Doku_Gurultulu = Doku_Temiz + Gurultu;

% Medyan (Ortanca Değer) Filtresi Uygulama Algoritması
Doku_Temizlenmis = medfilt2(Doku_Gurultulu, [3 3]);

% Görselleştirme
imagesc(Doku_Temizlenmis); 
colorbar; 
title('Filtre Edilmis Temiz Goruntu');
