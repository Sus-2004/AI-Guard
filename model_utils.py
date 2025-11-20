import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
import os

DATASET_DIR = "datasets"
MODEL_PATH = "model.joblib"

def load_dataset():
    safe_path = os.path.join(DATASET_DIR, "safe.txt")
    unsafe_path = os.path.join(DATASET_DIR, "unsafe.txt")

    with open(safe_path, "r", encoding="utf-8") as f:
        safe_queries = f.read().splitlines()

    with open(unsafe_path, "r", encoding="utf-8") as f:
        unsafe_queries = f.read().splitlines()

    X = safe_queries + unsafe_queries
    y = [0]*len(safe_queries) + [1]*len(unsafe_queries)
    return X, y


def build_and_train():
    X, y = load_dataset()

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(
            analyzer="char",
            ngram_range=(1, 3),
            min_df=1
        )),
        ("clf", LinearSVC())
    ])

    pipeline.fit(X, y)

    joblib.dump(pipeline, MODEL_PATH)
    print("✔ High-accuracy model saved!")


if __name__ == "__main__":
    build_and_train()