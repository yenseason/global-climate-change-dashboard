from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Global Climate Change", page_icon="🌍", layout="wide")
ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "dataset" / "climate_change_clean.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    df["Temperature_Change"] = pd.to_numeric(df["Temperature_Change"], errors="coerce")
    df = df.dropna(subset=["Year", "Temperature_Change"])
    df["Year"] = df["Year"].astype(int)
    return df

df = load_data()
st.title("🌍 Global Climate Change Dashboard")
st.markdown("**Visualisasi perubahan suhu global dan regional, 1961–2019**")
st.caption("Satuan pengukuran: °C | Dataset berisi perubahan suhu terhadap periode acuan dataset, bukan suhu absolut.")
st.info("Nilai positif menunjukkan perubahan suhu di atas acuan dataset, sedangkan nilai negatif menunjukkan di bawah acuan. Data kosong tidak diubah menjadi nol.")

st.sidebar.header("Filter Dashboard")
areas = sorted(df["Area"].dropna().unique())
default_area = ["World"] if "World" in areas else areas[:1]
selected_areas = st.sidebar.multiselect("Negara/wilayah", areas, default=default_area)
years = sorted(df["Year"].unique())
year_range = st.sidebar.slider("Rentang tahun", int(min(years)), int(max(years)), (int(min(years)), int(max(years))))
periods = sorted(df["Months"].dropna().unique())
default_period = ["Meteorological year"] if "Meteorological year" in periods else periods
selected_periods = st.sidebar.multiselect("Bulan/periode", periods, default=default_period)

filtered = df[df["Year"].between(*year_range) & df["Months"].isin(selected_periods)]
if selected_areas:
    filtered = filtered[filtered["Area"].isin(selected_areas)]
if filtered.empty:
    st.warning("Tidak ada data pada kombinasi filter tersebut. Ubah pilihan filter.")
    st.stop()

# KPI
k1, k2, k3 = st.columns(3)
k1.metric("Negara/wilayah terpilih", f"{filtered['Area'].nunique():,}")
k2.metric("Rata-rata perubahan suhu", f"{filtered['Temperature_Change'].mean():.3f} °C")
k3.metric("Jumlah tahun teramati", f"{filtered['Year'].nunique():,}")

st.divider()
st.subheader("1. Tren perubahan suhu dari waktu ke waktu")
trend = filtered.groupby("Year", as_index=False)["Temperature_Change"].mean()
fig1 = px.line(trend, x="Year", y="Temperature_Change", markers=True,
    labels={"Year":"Tahun", "Temperature_Change":"Perubahan suhu rata-rata (°C)"})
fig1.add_hline(y=0, line_dash="dash", line_color="gray")
st.plotly_chart(fig1, use_container_width=True)

c1, c2 = st.columns(2)
with c1:
    st.subheader("2. Perbandingan rata-rata antarwilayah")
    area_mean = filtered.groupby("Area", as_index=False)["Temperature_Change"].mean()
    area_mean = area_mean.sort_values("Temperature_Change", ascending=False).head(15)
    fig2 = px.bar(area_mean.sort_values("Temperature_Change"), x="Temperature_Change", y="Area",
        orientation="h", labels={"Area":"Negara/wilayah", "Temperature_Change":"Rata-rata perubahan suhu (°C)"})
    st.plotly_chart(fig2, use_container_width=True)
with c2:
    st.subheader("3. Rata-rata perubahan suhu per bulan/periode")
    month_mean = filtered.groupby("Months", as_index=False)["Temperature_Change"].mean()
    fig3 = px.bar(month_mean, x="Months", y="Temperature_Change",
        labels={"Months":"Bulan/periode", "Temperature_Change":"Rata-rata perubahan suhu (°C)"})
    fig3.update_layout(xaxis_tickangle=-35)
    st.plotly_chart(fig3, use_container_width=True)

st.subheader("4. Heatmap perubahan suhu berdasarkan tahun dan periode")
heat = filtered.groupby(["Months", "Year"], as_index=False)["Temperature_Change"].mean()
pivot = heat.pivot(index="Months", columns="Year", values="Temperature_Change")
fig4 = px.imshow(pivot, aspect="auto", color_continuous_scale="RdBu_r", origin="lower",
    labels={"x":"Tahun", "y":"Bulan/periode", "color":"Perubahan suhu (°C)"})
st.plotly_chart(fig4, use_container_width=True)

st.subheader("Insight dari data yang sedang ditampilkan")
highest = trend.loc[trend["Temperature_Change"].idxmax()]
lowest = trend.loc[trend["Temperature_Change"].idxmin()]
st.markdown(
    f"- **Tahun tertinggi:** {int(highest['Year'])}, dengan rata-rata perubahan suhu **{highest['Temperature_Change']:.3f} °C**.\n"
    f"- **Tahun terendah:** {int(lowest['Year'])}, dengan rata-rata perubahan suhu **{lowest['Temperature_Change']:.3f} °C**.\n"
    f"- **Rata-rata seluruh data terfilter:** **{filtered['Temperature_Change'].mean():.3f} °C**.\n"
    "Insight akan berubah mengikuti filter wilayah, rentang tahun, dan periode."
)
with st.expander("Lihat data dan unduh hasil filter"):
    st.dataframe(filtered, use_container_width=True)
    st.download_button("Unduh CSV hasil filter", filtered.to_csv(index=False).encode("utf-8"),
        "climate_change_filtered.csv", "text/csv")

st.caption("Sumber data: halaman dataset Kaggle perlu dicantumkan pada README.md. Pengolahan dilakukan melalui scripts/clean_data.py.")
