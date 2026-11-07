"""Ön işleme adımı: sayısal sütunları ölçekle, kategorik sütunları one-hot kodla.

Bu adım 02_baseline notebook'unda ilk kez adım adım anlatılıyor. Sonraki notebook'lar
aynı ön işlemeyi buradan çağırır, böylece her modelde birebir aynı hazırlık yapılır.

Önemli (slayt 61): Ön işleme Pipeline'ın içine konur. Pipeline.fit(X_train, ...) çağrılınca
ölçekleyici ve kodlayıcı SADECE eğitim verisinden öğrenir; doğrulama/test verisine sadece uygulanır.
"""
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from . import config


def make_preprocessor(num_cols=None, cat_cols=None, scale=True):
    """Ön işleme nesnesini oluşturur (henüz fit edilmez).

    num_cols : ölçeklenecek sayısal sütunlar (varsayılan: config.NUM_COLS)
    cat_cols : one-hot yapılacak kategorik sütunlar (varsayılan: config.CAT_COLS)
    scale    : False verilirse sayısal sütunlar olduğu gibi geçer (ağaç modelleri ölçeklemeye ihtiyaç duymaz)
    """
    if num_cols is None:
        num_cols = config.NUM_COLS
    if cat_cols is None:
        cat_cols = config.CAT_COLS

    if scale:
        num_step = StandardScaler()
    else:
        num_step = "passthrough"

    # handle_unknown="ignore": eğitimde görülmeyen bir kategori gelirse hata verme, sıfır yaz
    cat_step = OneHotEncoder(handle_unknown="ignore")

    return ColumnTransformer([
        ("sayisal", num_step, num_cols),
        ("kategorik", cat_step, cat_cols),
    ])


def drop_cols(cols, *to_drop):
    """Bir sütun listesinden bazı sütunları çıkarır.

    Örnek: drop_cols(config.NUM_COLS, "PageValues")  ->  PageValues olmadan sayısal sütunlar
    """
    return [c for c in cols if c not in to_drop]
