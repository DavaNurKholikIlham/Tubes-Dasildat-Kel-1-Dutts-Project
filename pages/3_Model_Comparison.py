import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# DATA MODEL
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

st.title("🤖 Model Comparison")

st.markdown("""
Perbandingan performa beberapa algoritma klasifikasi yang digunakan
untuk memprediksi kemungkinan pengunjung melakukan pembelian.
""")

st.divider()

# =========================
# BEST MODEL
# =========================

best_model = df.loc[df["Accuracy"].idxmax()]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🥇 Best Model",
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

st.subheader("📋 Hasil Evaluasi Model")

st.dataframe(
    df,
    use_container_width=True
)

st.divider()

# =========================
# ACCURACY CHART
# =========================

st.subheader("📊 Perbandingan Accuracy")

fig, ax = plt.subplots(figsize=(8,4))

bars = ax.bar(
    df["Model"],
    df["Accuracy"]
)

ax.set_ylabel("Accuracy (%)")
ax.set_title("Accuracy Comparison")

for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f"{height:.2f}",
        ha="center"
    )

st.pyplot(fig)

st.info("""
Accuracy menunjukkan seberapa banyak prediksi yang benar dibandingkan
seluruh data yang diuji.
""")

st.divider()

# =========================
# PRECISION CHART
# =========================

st.subheader("🎯 Precision Comparison")

fig2, ax2 = plt.subplots(figsize=(8,4))

bars = ax2.bar(
    df["Model"],
    df["Precision"]
)

ax2.set_ylabel("Precision")

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
Precision mengukur ketepatan model ketika memprediksi kelas Purchase.
""")

st.divider()

# =========================
# RECALL CHART
# =========================

st.subheader("📈 Recall Comparison")

fig3, ax3 = plt.subplots(figsize=(8,4))

bars = ax3.bar(
    df["Model"],
    df["Recall"]
)

ax3.set_ylabel("Recall")

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

ax4.set_ylabel("F1-Score")

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
F1-Score merupakan kombinasi antara Precision dan Recall.
Semakin tinggi nilainya maka semakin seimbang performa model.
""")

st.divider()

# =========================
# RANKING
# =========================

st.subheader("🏆 Ranking Model")

ranking = df.sort_values(
    by="Accuracy",
    ascending=False
).reset_index(drop=True)

ranking.index += 1

st.dataframe(
    ranking,
    use_container_width=True
)

st.success(f"""
### Kesimpulan

Model terbaik berdasarkan Accuracy adalah **{best_model['Model']}**
dengan nilai Accuracy sebesar **{best_model['Accuracy']}%**.

Model ini dipilih sebagai model utama pada fitur Prediction karena
memberikan performa paling baik dibandingkan model lainnya.
""")