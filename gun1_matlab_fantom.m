% 1. GÜN: MATLAB İLERİ DÜZEY GÖRÜNTÜ REKONSTRÜKSİYONU
Doku_Buyuk = zeros(100, 100);
Doku_Buyuk(40:50, 40:50) = 8; % Tümör alanı
Doku_Buyuk(70:80, 20:30) = 4; % Kist alanı
imagesc(Doku_Buyuk); colorbar; title('Yapay Dokunun Radyolojik Goruntusu');
