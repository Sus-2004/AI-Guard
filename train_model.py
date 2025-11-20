# backend/train_model.py
from model_utils import build_and_train

if __name__ == "__main__":
    print("Training model... this may take ~10 seconds")
    build_and_train()
    print("✔ Training complete!")