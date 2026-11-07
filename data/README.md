# Veri Kartı: Online Shoppers Purchasing Intention

> Slayt 29'daki "veri kartı" şablonuna göre hazırlandı. EDA ilerledikçe **Sınırlamalar** bölümünü kendi bulgularınızla doldurun.

## Kaynak
- **Veri:** UCI Machine Learning Repository, dataset id **468**. https://archive.ics.uci.edu/dataset/468
- **Lisans:** CC BY 4.0. Kaynak gösterilerek kullanılabilir.
- **Künye:** Sakar, C., & Kastro, Y. (2018). Online Shoppers Purchasing Intention Dataset. UCI Machine Learning Repository. https://doi.org/10.24432/C5F88Q
- **İndirme:** `python scripts/download_data.py` (önce `ucimlrepo`, olmazsa UCI zip). Dosya `data/raw/online_shoppers_intention.csv` olarak kaydedilir.

## Toplama yöntemi
- Bir e-ticaret sitesinin Google Analytics kayıtlarından alınmış oturumlar.
- Bir yıllık dönemi kapsıyor. Her oturum farklı bir kullanıcıya ait; böylece belirli bir kampanyaya, güne ya da kullanıcıya yığılma önlenmiş.

## Boyut ve hedef
- 12.330 oturum, 17 girdi değişkeni, 1 hedef.
- **Hedef `Revenue`:** Oturum alışverişle bitti mi (True/False). 10.422 False (%84,5), 1.908 True (%15,5).
- **Etiketleme:** Elle yapılmamış; alışveriş işleminin kaydından geliyor.

## Değişkenler
| Değişken | Tür | Anlamı |
|---|---|---|
| `Administrative`, `Informational`, `ProductRelated` | sayısal | O türden kaç sayfa ziyaret edildi |
| `Administrative_Duration`, `Informational_Duration`, `ProductRelated_Duration` | sayısal | O sayfalarda geçen toplam süre (saniye) |
| `BounceRates` | sayısal | Ziyaret edilen sayfaların ortalama "hemen çıkma" oranı (Google Analytics) |
| `ExitRates` | sayısal | Ziyaret edilen sayfaların ortalama çıkış oranı (Google Analytics) |
| `PageValues` | sayısal | Ziyaret edilen sayfaların ortalama "sayfa değeri" (Google Analytics). **Sızıntı şüphesi var, bkz. aşağı** |
| `SpecialDay` | sayısal | Oturum tarihinin özel bir güne (ör. Sevgililer Günü) yakınlığı, 0–1 |
| `Month` | kategorik | Oturumun ayı |
| `OperatingSystems`, `Browser`, `Region`, `TrafficType` | kategorik | Sayıyla kodlanmış ama **sayısal anlamı yok** → one-hot |
| `VisitorType` | kategorik | Returning_Visitor / New_Visitor / Other |
| `Weekend` | ikili | Oturum hafta sonunda mı |

## Bilinen sınırlamalar ve dikkat noktaları
- **PageValues:** Google Analytics'te bir sayfanın değeri, o sayfanın **alışveriş yapılan** oturumlarda ziyaret edilmesinden hesaplanır. Oturumun kendi alışverişi bu değere katkı vermiş olabilir. Bu yüzden projede PageValues'lu ve PageValues'suz modeller karşılaştırılıyor.
- **Oturum sonu toplamları:** Sayfa sayıları ve süreler oturum bittikten sonra hesaplanmış toplamlar. Oturum devam ederken bu değerler henüz tam değil; gerçek zamanlı kullanım için bu bir kısıt.

### EDA bulguları (`notebooks/01_eda.ipynb`)
- **Tekrar eden satırlar:** 125 birebir tekrar var. Hepsi alışverişsiz ve tek ürün sayfasında 0 saniye kalınmış oturumlar. Bölmeden önce silindi; temiz veri **12.205 satır**, alışveriş oranı %15,6.
- **Eksik ve mantıksız değer:** Yok. `BounceRates` ve `ExitRates` en fazla 0,2.
- **Aylar:** Ocak ve Nisan veride yok; Haziran `June` diye yazılmış (diğer aylar üç harfli). Yıl bilgisi yok, ayların aynı takvim yılına ait olduğu varsayılıyor.
- **Aylara göre değişim:** Alışveriş oranı Şubat'ta %1,6, Kasım'da %25,4. Oturumların yarıdan fazlası Mayıs ve Kasım'da. Zaman bölmesinde eğitim (Şub–Ağu) %11,1, doğrulama (Eyl–Eki) %20,2, test (Kas–Ara) %20,7 alıcı içeriyor: **dağılım kayması** var.
- **Çarpıklık ve aykırı değerler:** Tüm sayısal değişkenler sağa çarpık (skew 2–7,6). En uzun oturum 17,8 saat; aykırı değerler gerçek davranış sayılıp tutuldu.
- **Sayıyla kodlanmış kategorikler:** `OperatingSystems`, `Browser`, `Region`, `TrafficType` kodlarının sırası anlamsız; one-hot ile 65 sütun oluşuyor. Bazı kategoriler çok seyrek (ör. `TrafficType` 12 ve 17'de birer oturum).
- **`SpecialDay`:** Sadece Şubat ve Mayıs'ta sıfırdan farklı.
- **PageValues:** Oturumların %77,9'unda 0. Revenue ile korelasyonu 0,49, diğer tüm değişkenlerden çok daha güçlü; alıcıların %19,4'ünde ise 0. Sızıntı şüphesi sürüyor.
- **Birbirine çok benzeyen değişkenler:** BounceRates–ExitRates (0,91), ProductRelated–ProductRelated_Duration (0,86).

## Uygun kullanım
- **Uygun:** Ders projesi; sınıflandırma, dengesiz veri, sızıntı ve zaman bölmesi denemeleri.
- **Uygun değil:** Bireysel kullanıcı hakkında çıkarım (veri anonim ve kullanıcı kimliği içermez).
