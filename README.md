# Online Alışveriş Sitelerinde Satın Alma Niyeti Tahmini

Makine Öğrenmesine Giriş, dönem projesi (2026). İsmail Kayaalp ve Ahmet Sadri Akıllı.

Bir e-ticaret oturumunun alışverişle bitip bitmeyeceğini (`Revenue`) oturum bilgilerinden tahmin eden ikili sınıflandırma projesi. Veri: UCI Online Shoppers Purchasing Intention (12.330 oturum, %15,5 alışveriş).

Projenin iki özgün deneyi var:
1. **PageValues sızıntı deneyi:** PageValues tahmin anında gerçekten biliniyor mu? Modeller bu değişkenle ve bu değişken olmadan karşılaştırılıyor.
2. **Zamana göre bölme:** Şubat–Ağustos verisiyle eğitim, Eylül–Ekim doğrulama, Kasım–Aralık test.

## Kurulum
```bash
python -m venv .venv
# Windows:  .venv\Scripts\activate      macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt
python scripts/download_data.py
jupyter lab
```

## Adım adım çalışma
Her notebook hocanın slaytlardaki iş akışını izler (slayt 32, 53, 56, 57, 59):
`veri → X ve y → bölme → model = ... → fit() → predict() → metrik → yorum`

Her adım dört parçadan oluşur:
1. Adım başlığı ve slayt numarası
2. Sözde kod
3. Adım yorumlu kısa kod (`# modeli oluştur`, `# eğit`, `# tahmin et`, `# değerlendir`)
4. Çıktı ve 1–2 cümle yorum

`02_baseline` içindeki "Baseline 1" adımı bu kalıbın tam örneğidir. `fit` ve `predict` her zaman notebook'ta açıkça görünür.

## Notebook'lar (sırayla)
| Notebook | Hafta | İçerik |
|---|---|---|
| `notebooks/01_eda.ipynb` | H3–H4 | Veri kalitesi, dağılımlar, dengesizlik, aylar, PageValues |
| `notebooks/02_baseline.ipynb` | H5–H6 | Bölmeler, Pipeline, iki baseline, lojistik regresyon |
| `notebooks/03_modeller.ipynb` | H7–H8 | Karar ağacı, Random Forest, 3 modelin karşılaştırılması |
| `notebooks/04_deneyler.ipynb` | H9–H10 | Hiperparametre, eşik, PageValues ve zaman bölmesi deneyleri |
| `notebooks/05_hata_analizi.ipynb` | H9–H10 | Yanlış tahminler hangi alt gruplarda toplanıyor? |
| `notebooks/06_final_test.ipynb` | H11 | Test setinde **tek** değerlendirme |

## Klasörler
- `data/`: ham ve işlenmiş veri, veri kartı (`data/README.md`)
- `src/`: ortak kod (ayarlar, veri temizleme ve bölme, ön işleme, kural baseline'ı, metrik ve grafik yardımcıları). Modeller notebook'larda açıkça oluşturulur.
- `docs/`: öneri formu, hocanın kriterleri, ders slaytı
- `reports/`: deney günlüğü, haftalık ilerleme, figürler
- `sunum/`: final sunumu

## Tekrarlanabilirlik
Tüm bölmeler `src/data.py`'de, seed `src/config.py`'de (`RANDOM_STATE = 42`). Her deney `reports/deney_gunlugu.md`'ye kaydedilir.
