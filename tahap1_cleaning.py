import os
import fitz  # PyMuPDF
import re

input_folder = "data/pdf"
output_folder = "data/raw"
os.makedirs(output_folder, exist_ok=True)

def bersihkan_teks(teks):
    # Hapus karakter aneh, header/footer standar, spasi ganda
    teks = re.sub(r'\s+', ' ', teks)  # normalisasi spasi
    teks = re.sub(r'Halaman\s+\d+\s+dari\s+\d+', '', teks, flags=re.IGNORECASE)
    teks = re.sub(r'Putusan Nomor.*', '', teks, flags=re.IGNORECASE)
    teks = teks.strip()
    return teks

def ekstrak_pdf_ke_txt(nama_file, index):
    path_pdf = os.path.join(input_folder, nama_file)
    path_txt = os.path.join(output_folder, f"case_{index:03}.txt")

    doc = fitz.open(path_pdf)
    teks_total = ""
    for page in doc:
        teks_total += page.get_text()

    teks_bersih = bersihkan_teks(teks_total)

    with open(path_txt, "w", encoding="utf-8") as f:
        f.write(teks_bersih)

    print(f"✓ Sukses ekstrak: {nama_file} → case_{index:03}.txt")

# Proses semua file PDF
pdf_files = sorted([f for f in os.listdir(input_folder) if f.endswith(".pdf")])
for idx, pdf in enumerate(pdf_files, 1):
    ekstrak_pdf_ke_txt(pdf, idx)
