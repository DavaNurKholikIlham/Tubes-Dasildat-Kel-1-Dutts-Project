import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# DATA EVALUASI
# =========================

df = pd.DataFrame({
    "Model": [
        "KNN",
        "Decision Tree",
        "SVM",
        "Neural Network"
    ],
    "Accuracy": [
        81.71,
        87.79,
        87.10,
        86.54
    ],
    "Precision": [
        0.48,
        0.59,
        0.56,
        0.55
    ],
    "Recall": [
        0.57,
        0.71,
        0.74,
        0.68
    ],
    "F1-Score": [
        0.52,
        0.64,
        0.64,
        0.61
    ]
})

# =========================
# HEADER
# =========================

st.title("📊 Model Evaluation Dashboard")

st.markdown("""
Evaluasi performa model klasifikasi yang digunakan untuk memprediksi
kemungkinan pengunjung melakukan pembelian pada website e-commerce.
""")

st.divider()

# =========================
# KPI
# =========================

best_model = df.loc[df["Accuracy"].idxmax()]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🏆 Best Model",
        best_model["Model"]
    )

with col2:
    st.metric(
        "🎯 Accuracy",
        f"{best_model['Accuracy']}%"
    )

with col3:
    st.metric(
        "📌 Precision",
        best_model["Precision"]
    )

with col4:
    st.metric(
        "📈 Recall",
        best_model["Recall"]
    )

st.divider()

# =========================
# TABLE
# =========================

st.subheader("📋 Evaluation Result")

st.dataframe(
    df,
    use_container_width=True
)

st.divider()

# =========================
# ACCURACY
# =========================

st.subheader("🎯 Accuracy Comparison")

fig1, ax1 = plt.subplots(figsize=(8,4))

bars = ax1.bar(
    df["Model"],
    df["Accuracy"]
)

ax1.set_ylabel("Accuracy (%)")

for bar in bars:
    height = bar.get_height()
    ax1.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f"{height:.2f}",
        ha="center"
    )

st.pyplot(fig1)

st.info("""
Accuracy menunjukkan persentase prediksi yang benar dibandingkan seluruh data uji.
Semakin tinggi nilai accuracy, semakin baik performa model secara umum.
""")

st.divider()

# =========================
# PRECISION
# =========================

st.subheader("📌 Precision Comparison")

fig2, ax2 = plt.subplots(figsize=(8,4))

bars = ax2.bar(
    df["Model"],
    df["Precision"]
)

for bar in bars:
    height = bar.get_height()
    ax2.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f"{height:.2f}",
        ha="center"
    )

st.pyplot(fig2)

st.info("""
Precision mengukur seberapa tepat model ketika memprediksi kelas Purchase.
""")

st.divider()

# =========================
# RECALL
# =========================

st.subheader("📈 Recall Comparison")

fig3, ax3 = plt.subplots(figsize=(8,4))

bars = ax3.bar(
    df["Model"],
    df["Recall"]
)

for bar in bars:
    height = bar.get_height()
    ax3.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f"{height:.2f}",
        ha="center"
    )

st.pyplot(fig3)

st.info("""
Recall mengukur kemampuan model menemukan seluruh data Purchase yang sebenarnya.
""")

st.divider()

# =========================
# F1 SCORE
# =========================

st.subheader("⚖️ F1-Score Comparison")

fig4, ax4 = plt.subplots(figsize=(8,4))

bars = ax4.bar(
    df["Model"],
    df["F1-Score"]
)

for bar in bars:
    height = bar.get_height()
    ax4.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f"{height:.2f}",
        ha="center"
    )

st.pyplot(fig4)

st.info("""
F1-Score merupakan kombinasi Precision dan Recall.
Metrik ini digunakan untuk mengukur keseimbangan performa model.
""")

st.divider()

# =========================
# RANKING
# =========================

st.subheader("🏅 Model Ranking")

ranking = df.sort_values(
    by="Accuracy",
    ascending=False
).reset_index(drop=True)

ranking.index += 1

st.dataframe(
    ranking,
    use_container_width=True
)

st.divider()

# =========================
# KESIMPULAN
# =========================

st.success(f"""
### 🎯 Kesimpulan

Berdasarkan hasil evaluasi:

🥇 Model terbaik adalah **{best_model['Model']}**

📊 Accuracy : **{best_model['Accuracy']}%**

📌 Precision : **{best_model['Precision']}**

📈 Recall : **{best_model['Recall']}**

Model ini dipilih sebagai model utama pada sistem prediksi karena memiliki performa terbaik dibandingkan model lainnya.
""")