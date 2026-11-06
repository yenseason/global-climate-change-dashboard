# GLOBAL CLIMATE CHANGE DASHBOARD

## Identitas Mahasiswa

- **Nama:** Neysalva Calista Firlin
- **NPM:** 241051005
- **Mata Kuliah:** Visualisasi Data
- **Program Studi:** Sistem Informasi

---

## 1. Deskripsi Proyek

**Global Climate Change Dashboard** merupakan sebuah dashboard interaktif yang dibuat untuk mengeksplorasi dan menganalisis perubahan suhu (*temperature change*) pada berbagai negara atau wilayah selama periode pengamatan tahun 1961 sampai 2019.

Dashboard ini dikembangkan menggunakan Python, Pandas, Plotly, dan Streamlit. Data perubahan suhu disajikan melalui berbagai bentuk visualisasi agar pengguna dapat memahami tren perubahan suhu, membandingkan kondisi antarwilayah, serta mengamati variasi perubahan suhu berdasarkan bulan atau periode pengamatan.

**Catatan interpretasi:** Variabel pada dataset merupakan perubahan suhu dalam satuan derajat Celsius (°C), bukan suhu absolut. Data yang tidak tersedia tetap dipertahankan sebagai *missing value* dan tidak diganti dengan nilai nol.

## 2. Tujuan Proyek

Pembuatan dashboard ini memiliki beberapa tujuan, yaitu:

1. Mengolah dataset perubahan suhu global agar menjadi data yang lebih terstruktur dan mudah dianalisis.
2. Menampilkan perkembangan perubahan suhu dari tahun 1961 hingga 2019.
3. Membandingkan perubahan suhu antara berbagai negara atau wilayah.
4. Mengidentifikasi pola dan kecenderungan perubahan suhu berdasarkan tahun serta bulan atau periode pengamatan.
5. Menerapkan penggunaan Python, Pandas, Plotly, dan Streamlit dalam proses pengolahan serta visualisasi data.
6. Menyajikan informasi perubahan suhu melalui dashboard interaktif yang mudah digunakan dan dipahami.

## 3. Latar Belakang

Perubahan iklim merupakan salah satu isu lingkungan global yang semakin mendapat perhatian karena dapat memengaruhi berbagai aspek kehidupan, seperti lingkungan, pertanian, kesehatan, dan aktivitas manusia. Salah satu indikator yang dapat digunakan untuk mengamati dinamika perubahan iklim adalah perubahan suhu. Dengan mengamati perubahan suhu dari tahun ke tahun, kita dapat memperoleh gambaran mengenai pola dan kecenderungan perubahan iklim yang terjadi di berbagai wilayah.

Dataset yang digunakan dalam proyek ini menyediakan informasi perubahan suhu berdasarkan negara atau wilayah, bulan atau periode pengamatan, serta tahun, mulai dari 1961 hingga 2019. Data tersebut dapat dimanfaatkan untuk melihat perkembangan perubahan suhu dari waktu ke waktu, membandingkan kondisi antarwilayah, dan mengidentifikasi periode ketika perubahan suhu mengalami peningkatan maupun penurunan.

Namun, data dalam jumlah besar sering kali sulit dipahami apabila hanya disajikan dalam bentuk tabel. Oleh karena itu, diperlukan proses pengolahan dan visualisasi data agar informasi yang terkandung di dalamnya dapat disampaikan secara lebih jelas, menarik, dan mudah dianalisis.

Berdasarkan permasalahan tersebut, dibuatlah **Global Climate Change Dashboard** menggunakan Python, Pandas, Plotly, dan Streamlit. Dashboard ini dilengkapi dengan berbagai visualisasi interaktif, seperti *line chart*, *bar chart*, dan *heatmap*, serta fitur filter berdasarkan negara atau wilayah, rentang tahun, dan bulan atau periode pengamatan. Dengan adanya dashboard ini, pengguna diharapkan dapat mengeksplorasi data, memahami tren perubahan suhu, serta memperoleh informasi mengenai dinamika perubahan iklim berdasarkan data yang tersedia.

## 4. Sumber Dataset

Dataset yang digunakan dalam proyek ini diunduh dari Kaggle.

- **Nama Dataset:** Temperature Change
- **Sumber:** Kaggle
- **Link Dataset:** https://www.kaggle.com/datasets/sevgisarac/temperature-change
- **Periode Pengamatan:** 1961–2019

Dataset tersebut berisi informasi perubahan suhu berdasarkan negara atau wilayah, bulan atau periode pengamatan, dan tahun.

## 5. Tahapan Pengelolaan Data

Sebelum digunakan dalam dashboard, dataset melalui beberapa tahapan pengolahan agar data lebih bersih dan siap dianalisis.

1. **Pengumpulan Data**  
   Mengunduh dataset perubahan suhu dari Kaggle dalam format CSV.

2. **Membaca Dataset**  
   Membaca file CSV menggunakan library Pandas dengan encoding `latin1` agar data dapat dibaca dengan baik.

3. **Pemilihan Data**  
   Memilih baris dengan nilai `Element` berupa `Temperature change`. Baris `Standard Deviation` tidak dicampurkan dengan nilai pengukuran perubahan suhu.

4. **Transformasi Data**  
   Mengubah format data tahunan dari bentuk *wide* menjadi *long* agar setiap tahun memiliki baris pengamatan tersendiri.

5. **Pembersihan Data**  
   Mengubah kolom tahun menjadi bilangan bulat dan nilai perubahan suhu menjadi numerik. Baris yang tidak memiliki nilai perubahan suhu dihapus, kemudian data duplikat dihilangkan.

6. **Penyimpanan Data Bersih**  
   Menyimpan hasil pengolahan ke dalam file `climate_change_clean.csv` yang digunakan sebagai sumber data dashboard.

## 6. Visualisasi yang Digunakan

Dashboard ini menggunakan empat jenis visualisasi utama untuk membantu pengguna memahami data perubahan suhu.

### A. Line Chart (Grafik Garis)

Digunakan untuk menampilkan tren perubahan suhu dari tahun ke tahun. Grafik ini membantu pengguna mengamati pola peningkatan maupun penurunan perubahan suhu selama periode pengamatan.

### B. Bar Chart per Wilayah

Digunakan untuk membandingkan rata-rata perubahan suhu antara negara atau wilayah yang dipilih. Visualisasi ini membantu pengguna melihat perbedaan perubahan suhu antarwilayah.

### C. Bar Chart per Bulan/Periode

Digunakan untuk menampilkan perbandingan perubahan suhu berdasarkan bulan atau periode pengamatan. Dengan grafik ini, pengguna dapat mengamati variasi perubahan suhu pada periode yang berbeda.

### D. Heatmap

Digunakan untuk menampilkan pola perubahan suhu berdasarkan tahun dan bulan atau periode pengamatan melalui gradasi warna. Heatmap memudahkan pengguna dalam mengidentifikasi periode dengan perubahan suhu yang relatif tinggi maupun rendah.

## 7. Fitur Dashboard

Dashboard Global Climate Change memiliki beberapa fitur utama, yaitu:

- **3 KPI Cards:** Menampilkan jumlah negara atau wilayah, rata-rata perubahan suhu, dan jumlah tahun yang teramati.
- **4 Visualisasi Interaktif:** Terdiri dari line chart, bar chart per wilayah, bar chart per bulan atau periode, dan heatmap.
- **Filter Negara/Wilayah:** Memungkinkan pengguna memilih negara atau wilayah yang ingin dianalisis.
- **Filter Rentang Tahun:** Memungkinkan pengguna menentukan periode pengamatan.
- **Filter Bulan/Periode:** Memungkinkan pengguna memilih bulan atau periode tertentu.
- **Insight Otomatis:** Menampilkan ringkasan informasi berdasarkan filter yang sedang digunakan.
- **Tabel Data:** Menampilkan data hasil penyaringan agar dapat diperiksa lebih lanjut.
- **Unduhan CSV:** Memungkinkan pengguna mengunduh data sesuai filter yang dipilih.

## 8. Hasil Analisis Awal (Key Insights)

Berdasarkan agregasi data `World` dengan periode `Meteorological year` untuk rentang tahun 1961–2019, diperoleh beberapa temuan awal sebagai berikut:

1. Rata-rata perubahan suhu pada data World selama periode 1961–2019 adalah sekitar **0,524 °C**.
2. Nilai perubahan suhu tahunan tertinggi terjadi pada tahun **2016**, yaitu sekitar **1,674 °C**.
3. Nilai perubahan suhu tahunan terendah terjadi pada tahun **1976**, yaitu sekitar **-0,311 °C**.
4. Rata-rata perubahan suhu menunjukkan peningkatan dari sekitar **-0,022 °C pada dekade 1960-an** menjadi **1,261 °C pada dekade 2010-an**.
5. Perbandingan perubahan suhu antarnegara atau wilayah serta bulan atau periode pengamatan dapat dieksplorasi lebih lanjut melalui filter interaktif pada dashboard.

Angka-angka tersebut merupakan ringkasan dari baris `World` dan `Meteorological year` pada dataset yang digunakan. Hasil dapat sedikit berbeda apabila sumber data atau proses pengolahan mengalami perubahan.

## 9. Teknologi yang Digunakan

Dalam proses pengembangan dashboard ini digunakan beberapa teknologi dan library berikut:

| Teknologi | Kegunaan |
|---|---|
| Python | Bahasa pemrograman utama untuk pengembangan proyek. |
| Pandas | Membaca, membersihkan, mengolah, dan menganalisis dataset. |
| Plotly | Membuat visualisasi data interaktif. |
| Streamlit | Membangun tampilan dashboard berbasis web. |
| CSV | Format penyimpanan dataset mentah dan data hasil pembersihan. |
| GitHub | Menyimpan dan mengelola repositori proyek. |
| Streamlit Community Cloud | Melakukan deployment agar dashboard dapat diakses secara online. |

## 10. Live Dashboard

Dashboard dapat diakses secara online melalui tautan berikut:

**https://global-climate-change-uts.streamlit.app/**

Pengguna dapat membuka dashboard melalui browser tanpa perlu menjalankan program secara lokal.

## 11. Struktur Folder Proyek

Berikut merupakan struktur folder dari proyek Global Climate Change Dashboard:

```text
Global_Climate_Change_UTS/
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
├── dataset/
│   ├── Environment_Temperature_change_E_All_Data_NOFLAG.csv
│   └── climate_change_clean.csv
│
└── scripts/
    └── clean_data.py
```

**Keterangan:**

- `app.py`: File utama untuk menjalankan aplikasi dashboard Streamlit.
- `requirements.txt`: Berisi daftar library atau dependensi Python yang diperlukan.
- `README.md`: Berisi dokumentasi proyek, penjelasan fitur, dan panduan penggunaan.
- `dataset/`: Folder untuk menyimpan dataset mentah dan dataset yang sudah dibersihkan.
- `Environment_Temperature_change_E_All_Data_NOFLAG.csv`: Dataset asli yang diperoleh dari Kaggle.
- `climate_change_clean.csv`: Dataset yang telah melalui proses pembersihan dan siap digunakan.
- `scripts/`: Folder untuk menyimpan script pendukung pengolahan data.
- `clean_data.py`: Script untuk membersihkan dan mengubah format dataset.

## 12. Cara Menjalankan Secara Lokal

Untuk menjalankan dashboard pada komputer, ikuti langkah-langkah berikut:

1. Pastikan Python versi 3.10 atau lebih baru sudah terpasang.
2. Unduh atau lakukan clone repositori proyek.
3. Buka terminal pada folder proyek.
4. Instal seluruh dependensi yang diperlukan dengan perintah:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Jika ingin menjalankan ulang proses pembersihan data, gunakan perintah:

   ```bash
   python scripts/clean_data.py
   ```

6. Jalankan dashboard menggunakan perintah:

   ```bash
   python -m streamlit run app.py
   ```

7. Buka alamat lokal yang muncul pada terminal, biasanya:

   ```text
   http://localhost:8501
   ```

## 13. Deployment Streamlit Community Cloud

Dashboard dipublikasikan menggunakan Streamlit Community Cloud agar dapat diakses secara online.

Tahapan deployment yang dilakukan:

1. Mengunggah seluruh isi folder proyek ke repositori GitHub dengan status **Public**.
2. Membuka https://share.streamlit.io/ dan masuk menggunakan akun GitHub.
3. Memilih menu **Create app**.
4. Memilih repositori GitHub, branch, dan file utama `app.py`.
5. Menekan tombol **Deploy** dan menunggu proses deployment selesai.
6. Menyalin URL aplikasi yang telah aktif untuk dicantumkan pada bagian Live Dashboard di README.

## 14. Kesimpulan

Berdasarkan pembuatan **Global Climate Change Dashboard**, dapat disimpulkan bahwa visualisasi data dapat membantu memahami pola dan perkembangan perubahan suhu di berbagai negara atau wilayah selama periode 1961–2019. Melalui pengolahan data menggunakan Python dan Pandas, data perubahan suhu yang sebelumnya tersaji dalam format tabel dapat diolah menjadi informasi yang lebih terstruktur dan mudah dianalisis.

Hasil analisis menunjukkan adanya kecenderungan peningkatan perubahan suhu pada data World. Rata-rata perubahan suhu selama periode pengamatan mencapai sekitar **0,524 °C**, dengan nilai tertinggi pada tahun 2016 sebesar **1,674 °C** dan nilai terendah pada tahun 1976 sebesar **-0,311 °C**. Selain itu, rata-rata perubahan suhu meningkat dari sekitar **-0,022 °C pada dekade 1960-an** menjadi **1,261 °C pada dekade 2010-an**. Hal ini menunjukkan adanya tren peningkatan perubahan suhu dari waktu ke waktu.

Penggunaan Streamlit dan Plotly membuat dashboard menjadi interaktif sehingga pengguna dapat mengeksplorasi data berdasarkan negara atau wilayah, rentang tahun, serta bulan atau periode pengamatan. Berbagai visualisasi, seperti *line chart*, *bar chart*, dan *heatmap*, juga membantu menyajikan informasi secara lebih menarik dan memudahkan perbandingan data.

Dengan demikian, proyek ini menunjukkan bahwa penerapan Python, Pandas, Plotly, dan Streamlit dapat dimanfaatkan untuk mengolah, menganalisis, serta menyajikan data perubahan iklim dalam bentuk dashboard interaktif. Dashboard ini diharapkan dapat membantu pengguna memahami tren perubahan suhu dan meningkatkan kesadaran terhadap dinamika perubahan iklim berdasarkan data yang tersedia.

---
**Dibuat untuk memenuhi tugas Ujian Tengah Semester (UTS) Mata Kuliah Visualisasi Data.**

**Program Studi Sistem Informasi**
