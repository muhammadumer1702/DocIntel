import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"
LABEL_FILE = BASE_DIR / "data" / "labels.csv"
MODEL_DIR = BASE_DIR / "models"
MODEL_FILE = MODEL_DIR / "document_model.pkl"

labels = pd.read_csv(LABEL_FILE)

texts = []
y = []

for _, row in labels.iterrows():
    text = (DATA_DIR / row["filename"]).read_text()
    texts.append(text)
    y.append(row["label"])

pipeline = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB())
])

pipeline.fit(texts, y)

MODEL_DIR.mkdir(exist_ok=True)
joblib.dump(pipeline, MODEL_FILE)

print(f"Model saved to {MODEL_FILE}")
