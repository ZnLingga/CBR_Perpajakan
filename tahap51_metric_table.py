import pandas as pd

metrics = {
    "Model": ["TF-IDF + Majority Voting"],
    "Retrieval Accuracy": [0.67],
    "Prediction Accuracy": [0.33],
    "Precision": [0.11],
    "Recall": [0.33],
    "F1-Score": [0.17]
}

df_metrics = pd.DataFrame(metrics)
df_metrics.to_csv("data/eval/retrieval_metrics.csv", index=False)
print("✓ Tabel metrik disimpan ke data/eval/retrieval_metrics.csv")
