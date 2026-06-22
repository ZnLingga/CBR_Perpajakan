# 📘 Sistem Prediksi Amar Putusan Perpajakan Berbasis CBR dan TF-IDF

Sistem ini dikembangkan untuk memprediksi amar putusan perkara perpajakan menggunakan pendekatan **Case-Based Reasoning (CBR)** dan representasi dokumen berbasis **TF-IDF**. Sistem ini dibangun sebagai bagian dari tugas akhir mata kuliah *Penalaran Komputer*, Universitas Muhammadiyah Malang.

## 📂 Struktur Proyek

```
├── data/
│   ├── raw/              # Dokumen putusan hasil ekstraksi dari PDF
│   ├── processed/        # Metadata & representasi kasus (.csv)
│   ├── eval/             # Query uji & hasil evaluasi
│   └── results/          # Hasil prediksi
├── notebooks/            # Notebook per tahap CBR
├── scripts/              # Script Python modular
├── prediction_performance_chart.png
├── README.md             # Dokumentasi ini
```

## 🛠️ Teknologi & Pustaka

- Python 3.10+
- pandas
- scikit-learn
- matplotlib
- Sastrawi
- PyMuPDF (`fitz`)

## 🚀 Cara Menjalankan Proyek

1. **Clone repository**
   ```bash
   git clone https://github.com/username/nama-repo-cbr-pajak.git
   cd nama-repo-cbr-pajak
   ```

2. **Install dependency**
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan pipeline per tahap**

   - Ekstraksi PDF ke teks:
     ```bash
     python scripts/01_extraction.py
     ```

   - Ekstraksi metadata:
     ```bash
     python scripts/02_representation.py
     ```

   - Representasi TF-IDF & retrieve:
     ```bash
     python scripts/03_retrieval.py
     ```

   - Prediksi amar putusan:
     ```bash
     python scripts/04_predict.py
     ```

   - Evaluasi performa:
     ```bash
     python scripts/05_evaluation.py
     ```

## 📄 Contoh Penggunaan

```python
query = "pengusaha tidak membayar pajak selama 3 tahun"
solusi, referensi = predict_outcome(query)

print("Prediksi Amar Putusan:", solusi)
print("Top-5 Case Referensi:", referensi)
```

## 📊 Hasil Evaluasi

| Metrik                | Nilai |
|-----------------------|-------|
| Retrieval Accuracy    | 0.67  |
| Prediction Accuracy   | 0.33  |
| Precision             | 0.11  |
| Recall                | 0.33  |
| F1-Score              | 0.17  |

## 📚 Referensi

- Aamodt, A., & Plaza, E. (1994). *Case-Based Reasoning: Foundational Issues, Methodological Variations, and System Approaches*. AI Communications.
- Manning, C. D., et al. (2008). *Introduction to Information Retrieval*. Cambridge University Press.
- Wilie, B., et al. (2020). *IndoBERT*. EMNLP.
- Direktori Putusan MA RI: [https://putusan3.mahkamahagung.go.id](https://putusan3.mahkamahagung.go.id)
