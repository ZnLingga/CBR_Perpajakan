import json
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from collections import Counter

# === Load data & TF-IDF ulang ===
df = pd.read_csv("data/processed/cases.csv")
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

stopwords = StopWordRemoverFactory().get_stop_words()
vectorizer = TfidfVectorizer(stop_words=stopwords, max_features=5000)
X = vectorizer.fit_transform(df["text_full"])

case_solutions = dict(zip(df["case_id"], df["amar_putusan"]))

def retrieve(query, k=5):
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, X)[0]
    top_k_idx = scores.argsort()[-k:][::-1]
    return [(df.iloc[i]["case_id"], scores[i]) for i in top_k_idx]

def predict_outcome(query, k=5):
    top_k = retrieve(query, k)
    sols = [case_solutions[cid] for cid, _ in top_k]
    return Counter(sols).most_common(1)[0][0], [cid for cid, _ in top_k]

# === Evaluasi ===
with open("data/eval/queries.json", "r", encoding="utf-8") as f:
    queries = json.load(f)

retrieval_correct = []
y_true = []
y_pred = []

for q in queries:
    pred_sol, top_k_ids = predict_outcome(q["query"])
    
    # Evaluasi retrieval (ground truth ada di top-k?)
    retrieval_correct.append(1 if q["ground_truth_case_id"] in top_k_ids else 0)
    
    # Evaluasi prediksi solusi
    y_true.append(q["ground_truth_solution"])
    y_pred.append(pred_sol)

# === Hitung Metode Evaluasi ===
retrieval_acc = sum(retrieval_correct) / len(retrieval_correct)

precision = precision_score(y_true, y_pred, average="macro", zero_division=0)
recall = recall_score(y_true, y_pred, average="macro", zero_division=0)
f1 = f1_score(y_true, y_pred, average="macro", zero_division=0)
accuracy = accuracy_score(y_true, y_pred)

print("=== Evaluasi Retrieval ===")
print(f"Top-k Retrieval Accuracy: {retrieval_acc:.2f}")

print("\n=== Evaluasi Prediksi ===")
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-Score: {f1:.2f}")
