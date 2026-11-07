"""Veriyi UCI'den indirir, doğrular ve data/raw/online_shoppers_intention.csv olarak kaydeder.

Çalıştırma (proje klasöründe):  python scripts/download_data.py
Önce ucimlrepo paketini dener; olmazsa UCI'nin zip dosyasını doğrudan indirir.
"""
import io
import sys
import zipfile
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "raw" / "online_shoppers_intention.csv"
ZIP_URL = "https://archive.ics.uci.edu/static/public/468/online+shoppers+purchasing+intention+dataset.zip"

EXPECTED_ROWS = 12330
EXPECTED_BUYERS = 1908


def from_ucimlrepo() -> pd.DataFrame:
    from ucimlrepo import fetch_ucirepo
    ds = fetch_ucirepo(id=468)
    df = ds.data.original
    if df is None:
        df = pd.concat([ds.data.features, ds.data.targets], axis=1)
    return df


def from_zip() -> pd.DataFrame:
    import requests
    r = requests.get(ZIP_URL, timeout=120)
    r.raise_for_status()
    with zipfile.ZipFile(io.BytesIO(r.content)) as z:
        name = next(n for n in z.namelist() if n.endswith(".csv"))
        return pd.read_csv(z.open(name))


def main():
    if OUT.exists():
        print(f"Zaten var: {OUT}")
        df = pd.read_csv(OUT)
    else:
        try:
            df = from_ucimlrepo()
            print("ucimlrepo ile indirildi.")
        except Exception as e:  # noqa: BLE001
            print(f"ucimlrepo olmadı ({e}); UCI zip deneniyor...")
            df = from_zip()
            print("UCI zip ile indirildi.")
        OUT.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(OUT, index=False)
        print(f"Kaydedildi: {OUT}")

    buyers = int(df["Revenue"].astype(bool).sum())
    ok = len(df) == EXPECTED_ROWS and buyers == EXPECTED_BUYERS
    print(f"Satır: {len(df)} (beklenen {EXPECTED_ROWS}) | Alışveriş: {buyers} (beklenen {EXPECTED_BUYERS}) | "
          f"Sütun: {df.shape[1]}")
    if not ok:
        print("UYARI: Boyutlar beklenenle tutmuyor, dosyayı kontrol edin.")
        return 1
    print("Doğrulama tamam.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
