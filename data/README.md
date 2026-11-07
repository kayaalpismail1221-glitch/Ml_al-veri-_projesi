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
- **EDA'da kontrol edilecekler:** Tekrar eden satır var mı? Hangi aylar veride var, hangileri yok? Ay adlarının yazımı tutarlı mı? Süre değişkenleri ne kadar çarpık? `SpecialDay` hangi aylarda sıfırdan farklı? Alışveriş oranı aylara göre nasıl değişiyor?
- (EDA sonrası buraya kendi bulgularınızı ekleyin.)

## Uygun kullanım
- **Uygun:** Ders projesi; sınıflandırma, dengesiz veri, sızıntı ve zaman bölmesi denemeleri.
- **Uygun değil:** Bireysel kullanıcı hakkında çıkarım (veri anonim ve kullanıcı kimliği içermez).
