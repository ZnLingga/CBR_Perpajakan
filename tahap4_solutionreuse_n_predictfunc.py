import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from collections import Counter
import os

# === Load Data ===
df = pd.read_csv("data/processed/cases.csv")

# === Siapkan Vectorizer ===
stop_factory = StopWordRemoverFactory()
indonesian_stopwords = stop_factory.get_stop_words()

vectorizer = TfidfVectorizer(
    stop_words=indonesian_stopwords,
    max_features=5000
)
X = vectorizer.fit_transform(df["text_full"])

# === Map case_id ke solusi ===
# Gunakan kolom 'amar_putusan' (bisa diganti jika kamu pakai nama lain)
if "amar_putusan" not in df.columns:
    raise ValueError("Kolom 'amar_putusan' tidak ditemukan di cases.csv")

case_solutions = dict(zip(df["case_id"], df["amar_putusan"]))

# === Fungsi retrieve() seperti sebelumnya ===
def retrieve(query: str, k: int = 5):
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, X)[0]
    top_k_idx = scores.argsort()[-k:][::-1]
    return [(df.iloc[i]["case_id"], scores[i]) for i in top_k_idx]

# === Fungsi Prediksi Solusi ===
def predict_outcome(query: str, k: int = 5) -> str:
    top_k = retrieve(query, k)
    solutions = [case_solutions[cid] for cid, _ in top_k if cid in case_solutions]

    # Majority voting
    counter = Counter(solutions)
    predicted_solution, _ = counter.most_common(1)[0]

    return predicted_solution, [cid for cid, _ in top_k]

# === Contoh penggunaan ===
query = "wajib pajak mengajukan keberatan atas SKPKB terkait PPN"
solution, top_cases = predict_outcome(query)

print("Prediksi Amar Putusan:")
print(solution)
print("\nTop-5 Case ID:")
print(top_cases)
