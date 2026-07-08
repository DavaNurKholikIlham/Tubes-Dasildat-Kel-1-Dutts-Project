import streamlit as st

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="DuttsProject",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

.main-header{
    text-align:center;
    padding:20px;
}

.hero-title{
    font-size:55px;
    font-weight:700;
    color:#6366F1;
}

.hero-subtitle{
    font-size:20px;
    color:#94A3B8;
}

.kpi-card{
    background:#1E293B;
    padding:25px;
    border-radius:15px;
    text-align:center;
    border:1px solid #334155;
}

.kpi-card:hover{
    border:1px solid #6366F1;
}

.kpi-number{
    font-size:32px;
    font-weight:bold;
    color:#6366F1;
}

.kpi-title{
    color:#CBD5E1;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================


st.sidebar.image(
    "assets/logodt.png",
    width=150
)

st.sidebar.markdown("# 🛒 DuttsProject")

st.sidebar.info("""
Online Shopper Purchase Prediction

Kelompok 1
""")

st.sidebar.markdown("""
### 👨‍💻 Anggota

- Dava Nur Kholik Ilham
- Fajri Nugraha
- Nicko Radja Athallah
""")

st.sidebar.divider()

st.sidebar.success("""
🏆 Best Model

Decision Tree

Accuracy: 87.79%
""")
# =========================
# HERO SECTION
# =========================

st.markdown("""
<div class="main-header">

<div class="hero-title">
🛒 DuttsProject
</div>

<div class="hero-subtitle">
Online Shopper Purchase Prediction Using Machine Learning
</div>

</div>
""", unsafe_allow_html=True)

st.success("""
🚀 Sistem prediksi kemungkinan pelanggan melakukan pembelian berdasarkan perilaku browsing menggunakan algoritma Machine Learning.
""")

st.divider()

# =========================
# KPI SECTION
# =========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-number">12,330</div>
        <div class="kpi-title">Dataset Records</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-number">17</div>
        <div class="kpi-title">Features</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-number">4</div>
        <div class="kpi-title">Algorithms</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-number">87.79%</div>
        <div class="kpi-title">Best Accuracy</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =========================
# OVERVIEW
# =========================

left, right = st.columns([2,1])

with left:

    st.subheader("📖 Project Overview")

    st.write("""
Dataset Online Shoppers Purchasing Intention digunakan untuk memprediksi
apakah seorang pengunjung website akan melakukan pembelian berdasarkan
aktivitas browsing yang dilakukan selama mengakses website.

Algoritma yang digunakan:

- K-Nearest Neighbor (KNN)
- Decision Tree
- Support Vector Machine (SVM)
- Neural Network (NN)

Berdasarkan hasil evaluasi, model terbaik adalah **Decision Tree**
dengan akurasi sebesar **87.79%**.
""")

with right:

    st.info("""
### 📌 Features

✔ Dataset Overview

✔ Exploratory Data Analysis

✔ Model Comparison

✔ Purchase Prediction

✔ Evaluation Dashboard
""")

st.divider()

# =========================
# TEAM
# =========================

st.subheader("👥 Team DuttsProject")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("""
### Dava Nur Kholik Ilham

707012400118
""")

with c2:
    st.success("""
### Fajri Nugraha

707012400099
""")

with c3:
    st.success("""
### Nicko Radja Athallah

707012400144
""")

st.divider()

st.caption(
    "© 2026 DuttsProject | Online Shopper Purchase Prediction System"
)