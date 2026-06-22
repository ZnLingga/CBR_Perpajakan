# Berdasarkan hasil evaluasi, sistem CBR berbasis TF-IDF + Majority Voting menunjukkan akurasi prediksi yang masih rendah (33%) meskipun kemampuan retrieval kasus cukup baik (67%). Hal ini menunjukkan bahwa kasus yang berhasil diretriev belum tentu mengandung solusi yang tepat atau konsisten.

# Rendahnya precision dan F1-score disebabkan oleh variasi ekspresi pada kolom amar putusan serta metode majority vote yang belum mempertimbangkan bobot kesamaan antar dokumen.

# Solusi yang dapat diterapkan ke depannya antara lain:

# Menyempurnakan preprocessing teks dan ringkasan amar putusan

# Menggunakan weighted similarity dalam voting

# Mengganti representasi TF-IDF dengan model semantik seperti IndoBERT untuk peningkatan konteks hukum