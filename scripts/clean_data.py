from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "dataset" / "Environment_Temperature_change_E_All_Data_NOFLAG.csv"
OUTPUT = ROOT / "dataset" / "climate_change_clean.csv"

def main():
    raw = pd.read_csv(SOURCE, encoding="latin1")
    year_cols = [c for c in raw.columns if c.startswith("Y") and c[1:].isdigit()]
    required = {"Area", "Months", "Element", "Unit"}
    missing = required - set(raw.columns)
    if missing:
        raise ValueError(f"Kolom wajib tidak ditemukan: {sorted(missing)}")

    # Hanya gunakan pengukuran perubahan suhu, bukan baris simpangan baku.
    data = raw[raw["Element"].astype(str).str.strip().eq("Temperature change")].copy()
    data = data.melt(
        id_vars=["Area", "Months", "Element", "Unit"],
        value_vars=year_cols,
        var_name="Year",
        value_name="Temperature_Change",
    )
    data["Year"] = data["Year"].str[1:].astype(int)
    data["Temperature_Change"] = pd.to_numeric(data["Temperature_Change"], errors="coerce")
    data["Area"] = data["Area"].astype(str).str.strip()
    data["Months"] = data["Months"].astype(str).str.strip()
    data = data.dropna(subset=["Temperature_Change"])
    data = data.drop_duplicates()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(OUTPUT, index=False, encoding="utf-8")
    print(f"Data bersih tersimpan: {OUTPUT}")
    print(f"Jumlah baris: {len(data):,}")

if __name__ == "__main__":
    main()
