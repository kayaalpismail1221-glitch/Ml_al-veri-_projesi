# Online Alışveriş Sitelerinde Satın Alma Niyeti Tahmini

Makine Öğrenmesine Giriş, dönem projesi (2026). İsmail Kayaalp ve Ahmet Sadri Akıllı.

Bir e-ticaret oturumunun alışverişle bitip bitmeyeceğini (`Revenue`) oturum bilgilerinden tahmin eden **ikili sınıflandırma** projesi.

## Problem ve metrik
| | |
|---|---|
| **Hedef (y)** | `Revenue`: 1 = oturum alışverişle bitti |
| **Girdiler (X)** | 17 değişken: sayfa sayıları ve süreleri, Google Analytics oranları, ay, ziyaretçi tipi vb. |
| **Sınıf dağılımı** | %84,5 alışverişsiz, %15,5 alışverişli (dengesiz) |
| **Ana metrik** | **PR-AUC**; yanında precision, recall, F1 |
| **Karar eşiği** | Doğrulama setinde F1'i en yüksek yapan değer |

Accuracy tek başına raporlanmaz: herkese "almaz" diyen model %84,5 accuracy alır ama hiçbir alıcıyı yakalamaz.

## Modeller
- **Baseline 1:** Herkese "almaz" diyen `DummyClassifier`
- **Baseline 2:** "PageValues > 0 ise alır" kuralı (`src/models.py` → `PageValuesRule`)
- **Lojistik Regresyon**, **Karar Ağacı**, **Random Forest** (scikit-learn)

## Özgün katkılar
1. **PageValues sızıntı deneyi:** Google Analytics'te bir sayfanın değeri alışveriş yapılan oturumlardan hesaplanır. Bu bilgi tahmin anında gerçekten biliniyor mu? Aynı modeller PageValues ile ve PageValues olmadan karşılaştırılıyor.
2. **Zamana göre bölme:** Şubat–Ağustos verisiyle eğitim, Eylül–Ekim doğrulama, Kasım–Aralık test. Model geçmişle eğitilip gelecekte sınanıyor; bu deneyde `Month` modelden çıkarılıyor.

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

## Notebook'lar ve ilerleme
| Notebook | Hafta | İçerik | Durum |
|---|---|---|---|
| `notebooks/01_eda.ipynb` | H3–H4 | Veri kalitesi, dağılımlar, dengesizlik, aylar, PageValues | 🔄 Adım 0–3 tamam |
| `notebooks/02_baseline.ipynb` | H5–H6 | Bölmeler, Pipeline, iki baseline, lojistik regresyon | ⬜ |
| `notebooks/03_modeller.ipynb` | H7–H8 | Karar ağacı, Random Forest, 3 modelin karşılaştırılması | ⬜ |
| `notebooks/04_deneyler.ipynb` | H9–H10 | Hiperparametre, eşik, PageValues ve zaman bölmesi deneyleri | ⬜ |
| `notebooks/05_hata_analizi.ipynb` | H9–H10 | Yanlış tahminler hangi alt gruplarda toplanıyor? | ⬜ |
| `notebooks/06_final_test.ipynb` | H11 | Test setinde **tek** değerlendirme | ⬜ |

Haftalık ayrıntı: [`reports/haftalik_ilerleme.md`](reports/haftalik_ilerleme.md). Commit geçmişi her adımın ne zaman yapıldığını gösterir.

## Klasörler
- `data/`: ham ve işlenmiş veri, veri kartı ([`data/README.md`](data/README.md)). Ham CSV repoda yok; `scripts/download_data.py` indirir.
- `src/`: ortak kod (ayarlar, veri temizleme ve bölme, ön işleme, kural baseline'ı, metrik ve grafik yardımcıları). Modeller notebook'larda açıkça oluşturulur.
- `docs/`: öneri formu ve hocanın kriterlerinin özeti (ders slaytı repoda paylaşılmaz)
- `reports/`: deney günlüğü, haftalık ilerleme, figürler
- `sunum/`: final sunumu

## Tekrarlanabilirlik
Tüm bölmeler `src/data.py`'de, seed `src/config.py`'de (`RANDOM_STATE = 42`). Tekrar eden satırlar bölmeden önce silinir, ön işleme `Pipeline` içinde sadece eğitim verisine fit edilir, test seti yalnızca `06_final_test`'te bir kez kullanılır. Her deney [`reports/deney_gunlugu.md`](reports/deney_gunlugu.md)'ye kaydedilir.

## Veri ve lisans
Sakar, C., & Kastro, Y. (2018). *Online Shoppers Purchasing Intention Dataset*. UCI Machine Learning Repository. https://doi.org/10.24432/C5F88Q. Lisans: CC BY 4.0.
