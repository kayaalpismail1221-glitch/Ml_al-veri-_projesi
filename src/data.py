"""Veriyi okuma, temizleme ve bölme.

Kural (slayt 51): Bölmeler sadece buradaki fonksiyonlarla yapılır. Böylece her notebook
birebir aynı eğitim / doğrulama / test ayrımını kullanır.
"""
from sklearn.model_selection import train_test_split

import pandas as pd

from . import config


def load_raw(path=config.RAW_CSV):
    """Ham CSV'yi okur. Dosya yoksa önce `python scripts/download_data.py` çalıştırılmalı."""
    if not path.exists():
        raise FileNotFoundError(f"{path} bulunamadı. Önce: python scripts/download_data.py")
    return pd.read_csv(path)


def clean(df, verbose=True):
    """Bölmeden ÖNCE yapılan temizlik.

    1) Birebir tekrar eden satırları siler. Bölmeden sonra silinseydi aynı satır hem eğitimde
       hem testte kalabilirdi; bu bir sızıntı türüdür (slayt 35, 37).
    2) True/False sütunlarını 0/1 sayıya çevirir.
    """
    n_before = len(df)
    df = df.drop_duplicates().reset_index(drop=True)
    if verbose:
        print(f"Tekrar eden satır silindi: {n_before - len(df)}  (kalan: {len(df)})")

    df[config.TARGET] = df[config.TARGET].astype(int)
    df["Weekend"] = df["Weekend"].astype(int)
    return df


def split_xy(df, num_cols=None, cat_cols=None):
    """Tabloyu girdiler (X) ve hedef (y) olarak ayırır (slayt 16)."""
    if num_cols is None:
        num_cols = config.NUM_COLS
    if cat_cols is None:
        cat_cols = config.CAT_COLS
    X = df[num_cols + cat_cols]
    y = df[config.TARGET]
    return X, y


def random_split(df, seed=config.RANDOM_STATE):
    """Tabakalı rastgele bölme: %70 eğitim, %15 doğrulama, %15 test (slayt 33).

    İki adımda yapılır:
      1) Verinin %30'unu ayır (geri kalan %70 eğitim).
      2) Ayrılan %30'u ikiye böl: yarısı doğrulama, yarısı test.
    stratify: her parçada alışveriş oranı aynı (~%15,5) kalsın diye (slayt 27).
    """
    holdout_share = config.RANDOM_SPLIT["val"] + config.RANDOM_SPLIT["test"]   # 0.30
    test_share_in_holdout = config.RANDOM_SPLIT["test"] / holdout_share         # 0.50

    train, holdout = train_test_split(
        df, test_size=holdout_share, stratify=df[config.TARGET], random_state=seed
    )
    val, test = train_test_split(
        holdout, test_size=test_share_in_holdout, stratify=holdout[config.TARGET], random_state=seed
    )
    return train.reset_index(drop=True), val.reset_index(drop=True), test.reset_index(drop=True)


def time_split(df):
    """Zamana göre bölme: önceki aylarla eğitim, sonraki aylarla test (slayt 35).

    Aylar config.TIME_SPLIT'te: Şub–Ağu eğitim, Eyl–Eki doğrulama, Kas–Ara test.
    Bu bölmede `Month` sütunu modelden çıkarılmalı: test ayları eğitimde hiç görülmüyor.
    """
    months = config.TIME_SPLIT
    train = df[df["Month"].isin(months["train"])].reset_index(drop=True)
    val = df[df["Month"].isin(months["val"])].reset_index(drop=True)
    test = df[df["Month"].isin(months["test"])].reset_index(drop=True)

    assert len(train) + len(val) + len(test) == len(df), "Bazı aylar TIME_SPLIT'te tanımlı değil"
    return train, val, test


def describe_split(name, parts):
    """Her parçanın satır sayısı ve alışveriş oranı (slayt 51: boyut ve sınıf dağılımı raporlanır)."""
    rows = []
    for part_name, part in zip(["eğitim", "doğrulama", "test"], parts):
        rows.append({
            "bölme": name,
            "parça": part_name,
            "satır": len(part),
            "alışveriş oranı": round(part[config.TARGET].mean(), 3),
        })
    return pd.DataFrame(rows)
