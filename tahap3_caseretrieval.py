import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import os
import json

# ======== 1. Load Dataset ==========
data_path = "data/processed/cases.csv"
df = pd.read_csv(data_path)

# Pastikan kolom text_full ada
if "text_full" not in df.columns:
    raise ValueError("Kolom 'text_full' tidak ditemukan di CSV!")

# ======== 2. Stopwords Bahasa Indonesia ==========
stop_factory = StopWordRemoverFactory()
indonesian_stopwords = stop_factory.get_stop_words()

# ======== 3. TF-IDF Vectorizer ==========
vectorizer = TfidfVectorizer(
    stop_words=indonesian_stopwords,
    max_features=5000
)
X = vectorizer.fit_transform(df["text_full"])

# ======== 4. Fungsi Retrieve ==========
def retrieve(query: str, k: int = 5):
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, X)[0]
    top_k_idx = scores.argsort()[-k:][::-1]
    return [(df.iloc[i]["case_id"], scores[i]) for i in top_k_idx]

# ======== 5. Contoh Pengujian Manual ==========
query = "pengusaha tidak membayar pajak selama 3 tahun"
top_k_results = retrieve(query, k=5)

print("Top-5 Kasus Paling Mirip:")
for case_id, score in top_k_results:
    print(f"{case_id} | Similarity: {score:.4f}")

# ======== 6. Simpan Query & Hasil (Optional) ==========
os.makedirs("data/eval", exist_ok=True)

queries = [
    {"query_id": "Q1", "query": "pengusaha tidak membayar pajak selama 3 tahun"},
    {"query_id": "Q2", "query": "keberatan wajib pajak atas SKPKB"},
    {"query_id": "Q3", "query": "pengajuan banding pajak terhadap putusan pengadilan pajak"}
]

# Simpan queries.json
with open("data/eval/queries.json", "w", encoding="utf-8") as f:
    json.dump(queries, f, indent=2, ensure_ascii=False)
