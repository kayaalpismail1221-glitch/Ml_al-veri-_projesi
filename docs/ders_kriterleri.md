# Ders Kriterleri: Hocanın Slaytlarından Özet

Kaynak: `docs/ders_slayti.pdf` (Makine Öğrenmesine Giriş, Hafta 1–2). Parantez içindeki sayılar slayt numaraları.

## Puanlama (69)
| Bölüm | Ağırlık | Bu projede karşılığı |
|---|---|---|
| Problem tanımı ve veri seti gerekçesi | %15 | Öneri formu, `data/README.md` |
| EDA ve ön işleme | %20 | `01_eda.ipynb` |
| Baseline ve model karşılaştırması | %25 | `02_baseline.ipynb`, `03_modeller.ipynb` |
| Değerlendirme ve hata analizi | %20 | `04_deneyler.ipynb`, `05_hata_analizi.ipynb`, `06_final_test.ipynb` |
| Notebook kalitesi ve tekrarlanabilirlik | %10 | Baştan sona çalışan notebook'lar, `reports/deney_gunlugu.md` |
| Sunum ve yorum | %10 | `sunum/` |

## Kilometre taşları (66)
- **Hafta 2:** Proje fikri, veri seti, hedef değişken, metrik.
- **Hafta 4:** Veri temizliği ve keşifsel analiz.
- **Hafta 6:** Baseline model ve ilk metrik.
- **Hafta 8:** En az üç modelin karşılaştırılması.
- **Hafta 10:** Hiperparametre ayarı ve hata analizi.
- **Hafta 12:** Final sunumu ve notebook.

Hoca ilerlemeyi dönem boyunca kontrol ediyor. Son dakika yapılmış (ör. yapay zekâyla üretilmiş) projeleri yakalamak için her aşamanın kanıtını istiyor (65).

## Veri seti kriterleri (30, 67)
- En az birkaç yüz örnek, net hedef, yeterli özellik.
- Yasal olarak paylaşılabilir, kişisel veya hassas değil.
- Birebir aynı adımlarla çözülmüş bir tutorial'ın kopyası değil.
- Model karşılaştırmaya yetecek kadar zor.
- **Veri kartı (29):** Kaynak, toplama yöntemi, değişken anlamları, etiketleme, sınırlamalar, uygun kullanım.

## Değerlendirme kuralları
- **Eğitim / doğrulama / test (33–34):** Model seçimi ve ayarı doğrulama setinde yapılır. Test seti en sonda **bir kez** kullanılır.
- **Bölme problemin yapısına uymalı (35):** Zaman verisinde geçmişle eğitilir, gelecekle test edilir. Tekrar eden ya da çok benzer örnekler bölmeler arasında dağılmamalı.
- **Veri sızıntısı (37–38):** Tahmin anında bilinmeyen bilgi modele girmemeli. "Fazla iyi" sonuçlar sızıntı denetimi gerektirir.
- **Baseline (39):** Çoğunluk sınıfı baseline'ı ve basit insan kuralı (alan bilgisi baseline'ı). Baseline'ı zar zor geçen karmaşık model işe yaramaz.
- **Metrik (44–48):** "Hangi hata daha pahalı?" sorusuna göre seçilir. Dengesiz veride accuracy yanıltır. Karar eşiği bir tercihtir ve doğrulama setinde seçilir.
- **Hata analizi (50):** Hangi örnekler yanlış? Hatalar bir alt grupta mı toplanıyor? **Final sunumunda en az bir hata analizi slaytı zorunlu.**

## Tekrarlanabilirlik (51)
- Minimum deney günlüğü: veri sürümü, bölme, özellikler, model, parametreler, metrik, tarih.
- Rastgele tohumlar sabitlenir. Bölmeler değişmez. Ön işleme seçimleri ve hiperparametreler kaydedilir.
- Veri boyutu ve sınıf dağılımı raporlanır.

## Notebook kuralları (54, 61)
- Her ana kod bloğunun ne yaptığı açıklanmalı. Notebook bir laboratuvar raporudur.
- Başka bir öğrenci notebook'u baştan sona tekrar çalıştırabilmeli.
- Sık hatalar: hücreleri sırasız çalıştırmak, ön işlemeyi bölmeden önce tüm veriye uygulamak, X ile y'yi karıştırmak, sınıf dağılımı vermeden tek skor raporlamak, açıklamasız kod teslim etmek.
