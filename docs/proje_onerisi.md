# Proje Konusu Öneri Formu (teslim edilen hali)

**Ders:** Makine Öğrenmesine Giriş – Dönem Projesi (2026)
**Grup:** İsmail Kayaalp (200207004), Ahmet Sadri Akıllı (210208029)

## 1. Projenin Amacı
**Proje adı:** Online Alışveriş Sitelerinde Ziyaretçinin Satın Alma Niyetinin Makine Öğrenmesi ile Tahmini

Bu projenin amacı, bir e-ticaret sitesine giren ziyaretçinin oturum bilgilerine (gezilen sayfa sayıları, sayfalarda geçirilen süreler, ay, ziyaretçi tipi vb.) bakarak o oturumun alışverişle bitip bitmeyeceğini tahmin etmektir. Problem, hedef değişkeni Revenue (alışveriş yaptı / yapmadı) olan bir ikili sınıflandırma problemidir. Böyle bir model, alışveriş ihtimali yüksek ama siteden ayrılmak üzere olan ziyaretçilere kampanya gösterilmesine yardımcı olabilir.

Oturumların yalnızca %15,5'i alışverişle bittiği için veri dengesizdir. Herkese "alışveriş yapmaz" diyen baseline model yaklaşık %84,5 doğruluk alır ama hiçbir alıcıyı yakalayamaz. Bu nedenle modelleri doğrulukla değil; F1, recall, precision ve PR-AUC ile değerlendireceğiz. Baseline ile birlikte lojistik regresyon, karar ağacı ve Random Forest modellerini karşılaştıracak, karar eşiğini doğrulama verisinde seçeceğiz.

Projenin özgün katkısı iki deneydir: (1) Önceki çalışmalarda en güçlü değişken bulunan PageValues'in tahmin anında gerçekten bilinip bilinemeyeceğini sorgulamak için modelleri bu değişkenle ve bu değişken olmadan karşılaştırmak (veri sızıntısı tartışması), (2) modeli rastgele bölme yerine önceki aylarda eğitip son aylarda test ederek zamana göre genellenebilirliğini ölçmek.

## 2. Veri Seti
Veri seti, UCI Machine Learning Repository'de açık olarak paylaşılan "Online Shoppers Purchasing Intention Dataset"tir (https://archive.ics.uci.edu/dataset/468). Python'da ucimlrepo paketiyle `fetch_ucirepo(id=468)` komutu kullanılarak indirilecektir. Veri seti CC BY 4.0 lisanslıdır; kaynak gösterilerek kullanılabilir ve kişisel bilgi içermez.

Veri seti 12.330 oturumdan oluşur. Bunların 10.422'si (%84,5) alışverişsiz, 1.908'i (%15,5) alışverişli oturumdur. 17 girdi değişkeni (10 sayısal, 7 kategorik) ve hedef değişken Revenue bulunur. Veride eksik değer yoktur. Oturumlar bir yıllık dönemden alınmış olup her biri farklı bir kullanıcıya aittir.

**Veri setinin künyesi:** Sakar, C., & Kastro, Y. (2018). Online Shoppers Purchasing Intention Dataset [Veri seti]. UCI Machine Learning Repository. https://doi.org/10.24432/C5F88Q

## 3. Literatür
1. Sakar, C. O., Polat, S. O., Katircioglu, M., & Kastro, Y. (2019). Real-time prediction of online shoppers' purchasing intention using multilayer perceptron and LSTM recurrent neural networks. *Neural Computing and Applications*, 31, 6893–6908. https://doi.org/10.1007/s00521-018-3523-0
2. Xiong, L., Chen, X., Liang, J., Cao, X., Zhu, P., & Zhao, M. (2024). Tree-based methods for analytics of online shoppers' purchasing intentions. *International Journal of Data Science*, 9(2), 99–122.

## 4. İş Planı
| İş paketi | Haftalar |
|---|---|
| 1. Literatür taraması, problemin tanımlanması ve proje önerisi | H1–H2 (19.10 – 01.11) |
| 2. Verinin indirilmesi, keşifsel veri analizi (EDA), kategorik değişkenlerin kodlanması | H3–H4 (02.11 – 15.11) |
| 3. Eğitim/doğrulama/test ayrımı, Pipeline kurulumu, baseline ve lojistik regresyon | H5–H6 (16.11 – 29.11) |
| 4. Karar ağacı ve Random Forest modelleri, üç modelin karşılaştırılması | H7–H8 (30.11 – 13.12) |
| 5. Hiperparametre ayarı, eşik seçimi, PageValues ve zaman bazlı bölme deneyleri, hata analizi | H9–H10 (14.12 – 27.12) |
| 6. Test setinde son değerlendirme, sunum ve notebook hazırlığı | H11–H12 (28.12 – 10.01) |
