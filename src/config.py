"""Proje genelinde kullanılan sabitler: dosya yolları, seed, değişken listeleri, bölme tanımları."""
from pathlib import Path

# --- Yollar ---
ROOT = Path(__file__).resolve().parents[1]
RAW_CSV = ROOT / "data" / "raw" / "online_shoppers_intention.csv"
PROCESSED_DIR = ROOT / "data" / "processed"
FIG_DIR = ROOT / "reports" / "figures"

# --- Tekrarlanabilirlik (slayt 51) ---
RANDOM_STATE = 42

# --- Hedef ve değişkenler ---
TARGET = "Revenue"

NUM_COLS = [
    "Administrative", "Administrative_Duration",
    "Informational", "Informational_Duration",
    "ProductRelated", "ProductRelated_Duration",
    "BounceRates", "ExitRates", "PageValues", "SpecialDay",
]

# Sayıyla kodlanmış ama sayısal anlamı olmayan değişkenler de burada (slayt 24): one-hot yapılacak.
CAT_COLS = ["Month", "OperatingSystems", "Browser", "Region", "TrafficType", "VisitorType", "Weekend"]

# Google Analytics'ten gelen sayfa metrikleri (sızıntı deneyinde kullanılabilir)
GA_COLS = ["BounceRates", "ExitRates", "PageValues"]

# --- Bölmeler ---
# Rastgele (tabakalı) bölme oranları: eğitim / doğrulama / test
RANDOM_SPLIT = {"train": 0.70, "val": 0.15, "test": 0.15}

# Zamana göre bölme (proje katkısı 2). Veride Ocak ve Nisan yok; Haziran "June" diye yazılmış.
# Not: Veride yıl bilgisi yok, ayların aynı takvim yılına ait olduğu varsayılıyor.
MONTH_ORDER = ["Feb", "Mar", "May", "June", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
TIME_SPLIT = {
    "train": ["Feb", "Mar", "May", "June", "Jul", "Aug"],
    "val": ["Sep", "Oct"],
    "test": ["Nov", "Dec"],
}
