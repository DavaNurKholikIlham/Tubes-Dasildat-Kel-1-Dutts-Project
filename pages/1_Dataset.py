import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("data/dataset.csv")

# =========================
# HEADER
# =========================

st.title("📊 Dataset Overview")

st.markdown("""
Analisis dataset **Online Shoppers Purchasing Intention** yang digunakan
untuk memprediksi apakah pengunjung website akan melakukan pembelian
atau tidak.
""")

st.divider()

# =========================
# KPI
# =========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="📁 Total Data",
        value=f"{len(df):,}"
    )

with col2:
    st.metric(
        label="📌 Fitur Asli",
        value=str(df.shape[1]-1)
    )

with col3:
    st.metric(
        label="⚙️ Total Kolom",
        value=str(df.shape[1])
    )

with col4:
    st.metric(
        label="🎯 Target",
        value="Revenue"
    )

st.divider()

# =========================
# DESKRIPSI DATASET
# =========================

st.subheader("📋 Dataset Description")

st.info("""
Dataset Online Shoppers Purchasing Intention digunakan untuk memprediksi
apakah seorang pengunjung website e-commerce akan melakukan pembelian
(Purchase) atau tidak (No Purchase).

Dataset terdiri dari 12.330 observasi dan 17 fitur utama yang
merepresentasikan perilaku pengunjung selama sesi browsing.
""")

st.divider()

# =========================
# PREVIEW DATASET
# =========================

st.subheader("👀 Preview Dataset")

st.dataframe(
    df.head(10),
    use_container_width=True
)

st.divider()

# =========================
# FEATURE INFORMATION
# =========================

st.subheader("📑 Feature Information")

feature_info = pd.DataFrame({
    "Feature": [
        "Administrative",
        "Administrative_Duration",
        "Informational",
        "Informational_Duration",
        "ProductRelated",
        "ProductRelated_Duration",
        "BounceRates",
        "ExitRates",
        "PageValues",
        "SpecialDay",
        "Month",
        "OperatingSystems",
        "Browser",
        "Region",
        "TrafficType",
        "VisitorType",
        "Weekend"
    ],

    "Description": [
        "Jumlah halaman administratif",
        "Durasi halaman administratif",
        "Jumlah halaman informasi",
        "Durasi halaman informasi",
        "Jumlah halaman produk",
        "Durasi halaman produk",
        "Persentase bounce",
        "Persentase exit",
        "Nilai halaman",
        "Kedekatan hari spesial",
        "Bulan kunjungan",
        "Sistem operasi pengguna",
        "Browser pengguna",
        "Wilayah pengguna",
        "Sumber traffic",
        "Tipe pengunjung",
        "Kunjungan saat akhir pekan"
    ]
})

st.dataframe(
    feature_info,
    use_container_width=True
)

st.divider()

# =========================
# TARGET DISTRIBUTION
# =========================

st.subheader("📈 Target Distribution")

revenue_counts = df["Revenue"].value_counts()

fig, ax = plt.subplots(figsize=(5,5))

ax.pie(
    revenue_counts,
    labels=["No Purchase", "Purchase"],
    autopct="%1.1f%%"
)

st.pyplot(fig)

st.caption("""
Distribusi target menunjukkan proporsi pengguna yang melakukan pembelian
(Purchase) dan yang tidak melakukan pembelian (No Purchase).
""")

st.divider()

# =========================
# DATA QUALITY
# =========================

st.subheader("✅ Dataset Quality")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Missing Values",
        int(df.isnull().sum().sum())
    )

with col2:
    st.metric(
        "Duplicate Data",
        int(df.duplicated().sum())
    )

with col3:
    st.metric(
        "Unique Data Types",
        len(df.dtypes.unique())
    )

st.success("Dataset berhasil dimuat dan siap digunakan untuk proses machine learning.")