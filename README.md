# Global Climate Change Dashboard

## Identitas Mahasiswa
- Nama: **Neysalva Calista Firlin**
- NPM: **241051005**
- Mata kuliah: Visualisasi Data
- Program Studi: Sistem Informasi

## Deskripsi
Dashboard interaktif untuk mengeksplorasi perubahan suhu (temperature change) pada berbagai negara/wilayah dan periode pengamatan dari tahun 1961 sampai 2019. Dashboard dibuat menggunakan Python, Pandas, Plotly, dan Streamlit.

**Catatan interpretasi:** variabel pada dataset adalah perubahan suhu (°C), bukan suhu absolut. Data yang tidak tersedia dipertahankan sebagai missing value dan tidak diganti dengan nol.

## Live Dashboard
**[https://global-climate-change-uts.streamlit.app/]**

## Sumber Dataset
Dataset diunduh dari Kaggle:
**[https://www.kaggle.com/datasets/sevgisarac/temperature-change]**

Pastikan tautan yang ditempel adalah halaman dataset yang benar-benar digunakan, bukan tautan pencarian Kaggle.

## Latar Belakang
Perubahan suhu merupakan salah satu indikator yang dapat digunakan untuk mengamati dinamika iklim. Dataset ini menyediakan pengamatan perubahan suhu menurut wilayah, bulan/periode, dan tahun. Dashboard membantu pengguna melihat tren waktu, membandingkan wilayah, serta mengamati variasi antarperiode.

## Key Insights
Berdasarkan agregasi data `World` untuk periode `Meteorological year`:
1. Rata-rata perubahan suhu pada data World selama 1961–2019 sekitar **0,524 °C**.
2. Nilai tahunan tertinggi dalam rentang tersebut terjadi pada **2016**, yaitu sekitar **1,674 °C**.
3. Nilai tahunan terendah dalam rentang tersebut terjadi pada **1976**, yaitu sekitar **-0,311 °C**.
4. Rata-rata dekade meningkat dari sekitar **-0,022 °C pada 1960-an** menjadi **1,261 °C pada 2010-an**.
5. Hasil perbandingan negara/wilayah dan bulan/periode dapat dieksplorasi melalui filter dashboard; urutan hasil mengikuti filter yang dipilih.

Angka di atas merupakan ringkasan dari baris `World` dan `Meteorological year` pada dataset yang digunakan. Angka dapat sedikit berbeda bila data sumber atau pemrosesan berubah.

## Fitur Dashboard
- 3 KPI Cards: jumlah negara/wilayah, rata-rata perubahan suhu, dan jumlah tahun teramati.
- 4 visualisasi: line chart, bar chart per wilayah, bar chart per bulan/periode, dan heatmap.
- Filter interaktif: negara/wilayah, rentang tahun, serta bulan/periode.
- Insight otomatis yang berubah mengikuti filter.
- Tabel data dan unduhan CSV hasil filter.

## Struktur Repositori
```text
Global_Climate_Change_UTS/
├── app.py
├── requirements.txt
├── README.md
├── dataset/
│   ├── Environment_Temperature_change_E_All_Data_NOFLAG.csv
│   └── climate_change_clean.csv
└── scripts/
    └── clean_data.py
```

## Cara Menjalankan Secara Lokal
1. Pastikan Python 3.10 atau lebih baru sudah terpasang.
2. Unduh atau clone repositori ini.
3. Buka terminal pada folder proyek.
4. Instal dependensi:
   ```bash
   python -m pip install -r requirements.txt
   ```
5. (Opsional) Jalankan ulang proses pembersihan data:
   ```bash
   python scripts/clean_data.py
   ```
6. Jalankan dashboard:
   ```bash
   python -m streamlit run app.py
   ```
7. Buka alamat lokal yang muncul di terminal (umumnya `http://localhost:8501`).

## Metode Pra-pemrosesan
1. Membaca file CSV sumber menggunakan encoding `latin1`.
2. Memilih baris dengan `Element` bernilai `Temperature change`; baris `Standard Deviation` tidak dicampurkan dengan nilai pengukuran.
3. Mengubah data tahunan dari format wide menjadi long.
4. Mengubah kolom tahun menjadi bilangan bulat dan nilai pengukuran menjadi numerik.
5. Menghapus baris yang tidak memiliki nilai perubahan suhu dan menghapus duplikasi.
6. Menyimpan hasil ke `dataset/climate_change_clean.csv`.

## Deployment Streamlit Community Cloud
1. Unggah seluruh isi folder proyek ke repositori GitHub dengan status **Public**.
2. Buka https://share.streamlit.io/ dan masuk menggunakan akun GitHub.
3. Pilih **Create app**, lalu pilih repositori, branch, dan file utama `app.py`.
4. Klik **Deploy** dan tunggu proses selesai.
5. Salin URL aplikasi yang aktif ke bagian **Live Dashboard** di README.

## Kesimpulan
Berdasarkan pembuatan Global Climate Change Dashboard, dapat disimpulkan bahwa visualisasi data dapat membantu memahami pola dan perkembangan perubahan suhu di berbagai negara atau wilayah selama periode 1961–2019. Melalui pengolahan data menggunakan Python dan Pandas, data perubahan suhu yang sebelumnya tersaji dalam format tabel dapat diolah menjadi informasi yang lebih terstruktur dan mudah dianalisis.

Hasil analisis menunjukkan adanya kecenderungan peningkatan perubahan suhu pada data World. Rata-rata perubahan suhu selama periode pengamatan mencapai sekitar 0,524 °C, dengan nilai tertinggi pada tahun 2016 sebesar 1,674 °C dan nilai terendah pada tahun 1976 sebesar -0,311 °C. Selain itu, rata-rata perubahan suhu meningkat dari sekitar -0,022 °C pada dekade 1960-an menjadi 1,261 °C pada dekade 2010-an. Hal ini menunjukkan adanya tren peningkatan perubahan suhu dari waktu ke waktu.

Penggunaan Streamlit dan Plotly membuat dashboard menjadi interaktif sehingga pengguna dapat mengeksplorasi data berdasarkan negara atau wilayah, rentang tahun, serta bulan atau periode pengamatan. Berbagai visualisasi, seperti line chart, bar chart, dan heatmap, juga membantu menyajikan informasi secara lebih menarik dan memudahkan perbandingan data.

Dengan demikian, proyek ini menunjukkan bahwa penerapan Python, Pandas, Plotly, dan Streamlit dapat dimanfaatkan untuk mengolah, menganalisis, serta menyajikan data perubahan iklim dalam bentuk dashboard interaktif. Dashboard ini diharapkan dapat membantu pengguna memahami tren perubahan suhu dan meningkatkan kesadaran terhadap dinamika perubahan iklim berdasarkan data yang tersedia.
