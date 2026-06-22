import json
import os

# Buat folder jika belum ada
os.makedirs("data/eval", exist_ok=True)

# Data dummy query + jawaban yang sesuai dengan data dummy kamu
queries = [
    {
        "query_id": "Q1",
        "query": "pengusaha tidak membayar pajak selama 3 tahun",
        "ground_truth_case_id": "case_003",
        "ground_truth_solution": "Permohonan ditolak"
    },
    {
        "query_id": "Q2",
        "query": "keberatan wajib pajak atas SKPKB",
        "ground_truth_case_id": "case_005",
        "ground_truth_solution": "Permohonan dikabulkan sebagian"
    },
    {
        "query_id": "Q3",
        "query": "pengajuan banding pajak terhadap putusan pengadilan pajak",
        "ground_truth_case_id": "case_010",
        "ground_truth_solution": "Gugatan tidak dapat diterima"
    }
]

# Simpan ke file JSON
with open("data/eval/queries.json", "w", encoding="utf-8") as f:
    json.dump(queries, f, indent=2, ensure_ascii=False)

print("✓ File queries.json berhasil dibuat di folder data/eval/")
