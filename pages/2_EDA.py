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

st.title("📊 Exploratory Data Analysis")
st.caption("Analisis perilaku pengunjung website e-commerce berdasarkan Online Shoppers Purchasing Intention Dataset")

st.divider()

# =========================
# KPI
# =========================

total_data = len(df)
total_purchase = df["Revenue"].sum()
purchase_rate = (total_purchase / total_data) * 100
total_features = len(df.columns)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📁 Total Data", f"{total_data:,}")

with col2:
    st.metric("📌 Total Fitur", total_features)

with col3:
    st.metric("🛒 Purchase", int(total_purchase))

with col4:
    st.metric("📈 Purchase Rate", f"{purchase_rate:.2f}%")

st.divider()

# =========================
# CHART 1
# =========================

col1, col2 = st.columns(2)

with col1:

    st.subheader("🛒 Revenue Distribution")

    revenue_counts = df["Revenue"].value_counts()

    fig, ax = plt.subplots(figsize=(5,5))

    ax.pie(
        revenue_counts,
        labels=["No Purchase", "Purchase"],
        autopct="%1.1f%%"
    )

    st.pyplot(fig)

    st.info("""
📌 Insight:

Sebagian besar pengunjung website tidak melakukan pembelian.

Hal ini menunjukkan bahwa dataset memiliki ketidakseimbangan kelas (imbalanced data) sehingga diperlukan teknik penanganan seperti undersampling.
""")

# =========================
# CHART 2
# =========================

with col2:

    st.subheader("👥 Visitor Type Distribution")

    visitor_counts = df["VisitorType"].value_counts()

    fig2, ax2 = plt.subplots(figsize=(8,4))

    visitor_counts.plot(
        kind="bar",
        ax=ax2
    )

    ax2.set_xlabel("Visitor Type")
    ax2.set_ylabel("Jumlah Pengunjung")

    st.pyplot(fig2)

    st.info("""
📌 Insight:

Returning Visitor mendominasi jumlah pengunjung website.

Artinya sebagian besar pengguna merupakan pengunjung yang pernah mengakses website sebelumnya.
""")

st.divider()

# =========================
# CHART 3
# =========================

st.subheader("📅 Distribusi Bulan")

month_counts = df["Month"].value_counts()

fig3, ax3 = plt.subplots(figsize=(10,5))

month_counts.plot(
    kind="bar",
    ax=ax3
)

ax3.set_xlabel("Month")
ax3.set_ylabel("Jumlah Kunjungan")

st.pyplot(fig3)

st.info("""
📌 Insight:

Aktivitas pengunjung tidak merata pada setiap bulan.

Beberapa bulan menunjukkan jumlah kunjungan yang lebih tinggi sehingga dapat digunakan sebagai dasar strategi promosi atau pemasaran.
""")

st.divider()

# =========================
# DATASET SUMMARY
# =========================

st.subheader("📋 Dataset Summary")

summary = pd.DataFrame({
    "Informasi": [
        "Jumlah Data",
        "Jumlah Fitur",
        "Target Variable",
        "Missing Value"
    ],
    "Nilai": [
        total_data,
        total_features,
        "Revenue",
        df.isnull().sum().sum()
    ]
})

st.dataframe(summary, use_container_width=True)

# =========================
# KESIMPULAN
# =========================

st.success("""
### 🎯 Kesimpulan EDA

✅ Dataset terdiri dari lebih dari 12 ribu data transaksi pengunjung website.

✅ Target Revenue menunjukkan distribusi kelas yang tidak seimbang.

✅ Returning Visitor merupakan tipe pengunjung yang paling dominan.

✅ Aktivitas pengunjung berbeda pada setiap bulan sehingga waktu kunjungan berpotensi memengaruhi keputusan pembelian.

✅ Dataset siap digunakan untuk proses klasifikasi menggunakan algoritma Machine Learning.
""")