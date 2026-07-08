import streamlit as st

st.title("👨‍💻 About DuttsProject")

st.markdown("""
### Online Shopper Purchase Prediction

Aplikasi ini dikembangkan untuk memprediksi kemungkinan pelanggan melakukan pembelian berdasarkan perilaku browsing pada website e-commerce menggunakan beberapa algoritma Machine Learning.

Model yang digunakan:
- K-Nearest Neighbor (KNN)
- Decision Tree
- Support Vector Machine (SVM)
- Neural Network (NN)

Dataset:
- Online Shoppers Purchasing Intention Dataset
""")

st.divider()

st.header("👥 Kelompok 1 - DuttsProject")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 👨‍🎓 Dava Nur Kholik Ilham
    **NIM:** 707012400118

    - Project Manager
    - Streamlit Development
    """)

with col2:
    st.markdown("""
    ### 👨‍🎓 Fajri Nugraha
    **NIM:** 707012400099

    - Model Training
    - Data Preprocessing
    """)

with col3:
    st.markdown("""
    ### 👨‍🎓 Nicko Radja Athallah
    **NIM:** 707012400144

    - Model Training 
    - Documentation
    """)

st.divider()

st.header("📊 Project Information")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Dataset", "12,330")

with col2:
    st.metric("Features", "17")

with col3:
    st.metric("Models", "4")

with col4:
    st.metric("Best Model", "Decision Tree")

st.divider()

st.success("""
🎯 Tujuan Proyek

Membangun sistem prediksi pembelian pelanggan menggunakan Machine Learning
untuk membantu bisnis memahami perilaku pengunjung website dan meningkatkan
strategi pemasaran digital.
""")

st.divider()

st.caption("© 2026 DuttsProject | Sistem Informasi Kota Cerdas - Telkom University")