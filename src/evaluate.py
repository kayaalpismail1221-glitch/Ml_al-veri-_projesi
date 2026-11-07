"""Değerlendirme yardımcıları.

02_baseline notebook'unda metrikler önce tek tek, açıkça hesaplanıyor. Sonraki notebook'lar
aynı hesabı tekrar yazmamak için `scores` fonksiyonunu kullanır.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    PrecisionRecallDisplay,
    accuracy_score,
    average_precision_score,
    f1_score,
    precision_recall_curve,
    precision_score,
    recall_score,
)

from . import config


def scores(y_true, p_buy, threshold=0.5):
    """Bir modelin metrikleri.

    y_true    : gerçek etiketler (0/1)
    p_buy     : modelin "alır" olasılıkları
    threshold : bu olasılığın üstü "alır" sayılır

    Ana metrik PR-AUC'dir (eşikten bağımsız). Accuracy sadece bağlam için var (slayt 46).
    """
    y_pred = (np.asarray(p_buy) >= threshold).astype(int)
    return {
        "PR-AUC": average_precision_score(y_true, p_buy),
        "F1": f1_score(y_true, y_pred, zero_division=0),
        "Precision": precision_score(y_true, y_pred, zero_division=0),
        "Recall": recall_score(y_true, y_pred, zero_division=0),
        "Accuracy": accuracy_score(y_true, y_pred),
        "Eşik": threshold,
    }


def best_threshold(y_val, p_val):
    """Doğrulama setinde F1'i en yüksek yapan eşiği döndürür (slayt 48).

    SADECE doğrulama verisiyle çağrılır. Test setinde eşik seçmek sızıntıdır.
    """
    precision, recall, thresholds = precision_recall_curve(y_val, p_val)
    f1 = 2 * precision * recall / (precision + recall + 1e-12)
    best_index = np.nanargmax(f1[:-1])  # son nokta bir eşiğe karşılık gelmez
    return float(thresholds[best_index])


def results_table(results):
    """{model adı: scores(...)} sözlüğünü okunur bir tabloya çevirir."""
    return pd.DataFrame(results).T.round(3)


def plot_pr_curves(y_true, probas, title="Precision-Recall eğrileri", save_as=None):
    """Birden fazla modelin PR eğrisini aynı grafikte çizer.

    probas : {model adı: "alır" olasılıkları}
    Kesikli çizgi: hiçbir şey öğrenmeyen modelin seviyesi (alışveriş oranı).
    """
    fig, ax = plt.subplots(figsize=(6, 5))
    for name, p_buy in probas.items():
        PrecisionRecallDisplay.from_predictions(y_true, p_buy, name=name, ax=ax)
    ax.axhline(np.mean(y_true), linestyle="--", color="grey", linewidth=1, label="Şans seviyesi")
    ax.set_title(title)
    ax.legend(loc="upper right", fontsize=8)
    save_figure(fig, save_as)
    return fig


def plot_confusion(y_true, p_buy, threshold, title="", save_as=None):
    """Karışıklık matrisi (slayt 45)."""
    y_pred = (np.asarray(p_buy) >= threshold).astype(int)
    fig, ax = plt.subplots(figsize=(4, 4))
    ConfusionMatrixDisplay.from_predictions(
        y_true, y_pred, display_labels=["Almaz", "Alır"], ax=ax, colorbar=False
    )
    ax.set_title(title or f"Karışıklık matrisi (eşik = {threshold:.2f})")
    save_figure(fig, save_as)
    return fig


def save_figure(fig, file_name):
    """Grafiği reports/figures/ altına kaydeder (sunumda kullanmak için)."""
    if file_name:
        config.FIG_DIR.mkdir(parents=True, exist_ok=True)
        fig.savefig(config.FIG_DIR / file_name, dpi=150, bbox_inches="tight")
