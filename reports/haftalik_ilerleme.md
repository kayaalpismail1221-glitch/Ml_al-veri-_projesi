# Haftalık İlerleme

Hoca kilometre taşlarını dönem boyunca kontrol ediyor (slayt 65–66). Her haftanın sonunda tamamlananları işaretleyin ve kim ne yaptı yazın.

## H1–H2 (19.10 – 01.11): Fikir, veri, hedef, metrik
- [x] Öneri formu teslim edildi
- [ ] 30 saniyelik proje tanıtımı (hedef, görev tipi, veri kaynağı, metrik, bir risk)

## H3–H4 (02.11 – 15.11): Temizlik ve EDA → `01_eda.ipynb`
- [x] Veri indirildi ve doğrulandı (`scripts/download_data.py`)
- [x] Veri kalitesi: eksik değer, tekrar eden satır, tutarsız yazımlar
- [x] Hedef dağılımı ve dengesizlik
- [x] Sayısal değişkenlerin dağılımı, çarpıklık, aykırı değerler
- [x] Kategorik değişkenler: sayıyla kodlanmış olanlar, kategori sayıları
- [x] Aylara göre oturum sayısı ve alışveriş oranı
- [x] PageValues ile alışveriş ilişkisi
- [x] `data/README.md` "Sınırlamalar" bölümü güncellendi
- **Kim ne yaptı:**

## H5–H6 (16.11 – 29.11): Baseline ve ilk metrik → `02_baseline.ipynb`
- [ ] Rastgele ve zamana göre bölmeler kuruldu, boyutları ve sınıf oranları raporlandı
- [ ] Pipeline kuruldu (ölçekleme + one-hot sadece eğitimde fit)
- [ ] Baseline 1: herkese "almaz"
- [ ] Baseline 2: "PageValues > 0 ise alır"
- [ ] Lojistik regresyon, PR-AUC ve F1
- **Kim ne yaptı:**

## H7–H8 (30.11 – 13.12): En az 3 model → `03_modeller.ipynb`
- [ ] Karar ağacı ve Random Forest
- [ ] Doğrulama setinde 3 model + 2 baseline karşılaştırma tablosu
- [ ] PR eğrileri grafiği
- **Kim ne yaptı:**

## H9–H10 (14.12 – 27.12): Ayar ve hata analizi → `04_deneyler.ipynb`, `05_hata_analizi.ipynb`
- [ ] Hiperparametre ayarı (doğrulama seti veya çapraz doğrulama)
- [ ] Eşik seçimi (doğrulama setinde)
- [ ] Deney 1: PageValues'lu / PageValues'suz
- [ ] Deney 2: rastgele bölme / zamana göre bölme
- [ ] Hata analizi: yanlış tahminler hangi gruplarda toplanıyor?
- **Kim ne yaptı:**

## H11–H12 (28.12 – 10.01): Final → `06_final_test.ipynb`, `sunum/`
- [ ] Test setinde tek değerlendirme
- [ ] Tüm notebook'lar "Restart & Run All" ile hatasız çalışıyor
- [ ] Sunum hazır (en az 1 hata analizi slaytı)
- **Kim ne yaptı:**
