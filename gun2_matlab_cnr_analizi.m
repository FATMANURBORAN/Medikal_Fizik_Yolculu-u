% 2. GÜN: MATLAB İLERİ GÖRÜNTÜ KALİTESİ VE GÜRÜLTÜ MODELLEME
Doku_Temiz = zeros(100, 100); 
Doku_Temiz(40:60, 40:60) = 5;

Gurultu = randn(100, 100) * 0.8;
Doku_Gurultulu = Doku_Temiz + Gurultu;

% CNR (Contrast-to-Noise Ratio) Hesaplama Algoritması
Tumor_Bolgesi = Doku_Gurultulu(40:60, 40:60);
Normal_Bolge = Doku_Gurultulu(1:20, 1:20);

Mean_Tumor = mean(Tumor_Bolgesi(:));
Mean_Normal = mean(Normal_Bolge(:));
Noise_Standart = std(Normal_Bolge(:));

CNR = abs(Mean_Tumor - Mean_Normal) / Noise_Standart;
disp(['Hesaplanan Goruntunun CNR Degeri: ', num2str(CNR)]);
