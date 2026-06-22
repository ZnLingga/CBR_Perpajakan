import pandas as pd

# Load data CSV
df = pd.read_csv("data/processed/cases.csv")

# Tambahkan kolom dummy amar_putusan (isi diputar ulang)
dummy_putusan = [
    "Permohonan ditolak",
    "Permohonan dikabulkan sebagian",
    "Permohonan dikabulkan seluruhnya",
    "Gugatan tidak dapat diterima",
    "Tidak berwenang mengadili"
]

# Panjangkan daftar dummy sesuai jumlah baris
df["amar_putusan"] = (dummy_putusan * ((len(df) // len(dummy_putusan)) + 1))[:len(df)]

# Simpan ulang ke CSV
df.to_csv("data/processed/cases.csv", index=False)

print("✓ Kolom 'amar_putusan' dummy berhasil ditambahkan.")
