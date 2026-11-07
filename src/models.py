"""Alan bilgisi baseline'ı: "PageValues > 0 ise alışveriş yapar" kuralı.

Diğer modeller (DummyClassifier, LogisticRegression, DecisionTreeClassifier, RandomForestClassifier)
notebook'larda AÇIKÇA oluşturulur ki slayt 56'daki kalıp görünsün:
    model = ...      ->  model.fit(X_train, y_train)  ->  model.predict(X_val)  ->  metrik
"""
import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin


class PageValuesRule(BaseEstimator, ClassifierMixin):
    """Öğrenme yapmayan basit kural (slayt 39: "basit insan kuralı" baseline'ı).

    Diğer modellerle aynı şekilde kullanılabilsin diye fit / predict / predict_proba yöntemleri var.
    Ham veri (DataFrame) ile kullanılır; Pipeline'a konmaz.
    """

    def __init__(self, threshold=0.0):
        self.threshold = threshold

    def fit(self, X, y=None):
        # Kural öğrenme yapmaz; sadece sınıf etiketlerini kaydeder.
        self.classes_ = np.array([0, 1])
        return self

    def predict(self, X):
        # PageValues eşikten büyükse 1 (alır), değilse 0 (almaz)
        page_values = X["PageValues"].to_numpy()
        return (page_values > self.threshold).astype(int)

    def predict_proba(self, X):
        # Kural kesin karar verir: olasılık ya 0 ya 1
        p_buy = self.predict(X).astype(float)
        return np.column_stack([1 - p_buy, p_buy])
