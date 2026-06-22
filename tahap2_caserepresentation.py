import os
import re
import pandas as pd

input_folder = "data/raw"
output_file = "data/processed/cases.csv"
os.makedirs("data/processed", exist_ok=True)

def ekstrak_metadata(teks):
    meta = {
        "no_perkara": None,
        "tanggal": None,
        "jenis_perkara": "Perpajakan",
        "pasal": None,
        "pihak": None,
        "text_full": teks
    }

    # Coba regex metadata (disesuaikan dari pola umum putusan)
    no_perkara = re.search(r"Nomor\s*[:\-]?\s*(\S+)", teks, re.IGNORECASE)
    if no_perkara:
        meta["no_perkara"] = no_perkara.group(1)

    tanggal = re.search(r"(Tanggal|Dibacakan)\s*[:\-]?\s*(\d{1,2}\s+\w+\s+\d{4})", teks, re.IGNORECASE)
    if tanggal:
        meta["tanggal"] = tanggal.group(2)

    pasal = re.search(r"Pasal\s*[:\-]?\s*(\d+[^.,;\n]*)", teks)
    if pasal:
        meta["pasal"] = pasal.group(1)

    pihak = re.search(r"(antara|penggugat\s+dengan\s+tergugat)[^\n]+", teks, re.IGNORECASE)
    if pihak:
        meta["pihak"] = pihak.group(0).strip()

    return meta

# Proses semua file
data = []
raw_files = sorted(os.listdir(input_folder))
for idx, filename in enumerate(raw_files, 1):
    path = os.path.join(input_folder, filename)
    with open(path, encoding="utf-8") as f:
        teks = f.read()
        meta = ekstrak_metadata(teks)
        meta["case_id"] = f"case_{idx:03}"
        data.append(meta)

# Simpan ke CSV
df = pd.DataFrame(data)
df.to_csv(output_file, index=False)
print(f"✓ Data berhasil disimpan ke {output_file}")
