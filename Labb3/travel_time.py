from joblib import dump, load
from datetime import datetime
from sklearn.preprocessing import *


def load_model():
    filename="Labb3/models/" + datetime.now().strftime("%Y-%m-%d %H")
    model = load(filename + "_model.joblib")
    poly = load(filename + "_poly.joblib")
    min_max = load(filename + "_min_max.joblib")
    return (model, poly, min_max)
(model, poly, min_max) = load_model()
def predict(X_data):
    scaled = poly.fit_transform(min_max.fit_transform([X_data]))
    y_pred = model.predict(scaled)
    return y_pred