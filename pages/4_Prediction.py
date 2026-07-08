import streamlit as st
import pandas as pd
import joblib

# =========================
# HEADER
# =========================

st.title("🎯 Purchase Prediction System")

st.markdown("""
Prediksi kemungkinan pengunjung website melakukan pembelian berdasarkan
perilaku browsing menggunakan algoritma Machine Learning.
""")

st.info("""
🤖 Model yang tersedia:
- Decision Tree
- KNN
- SVM
- Neural Network

🏆 Model terbaik: Decision Tree (Accuracy 87.79%)
""")

st.divider()

# =========================
# MODEL SELECTION
# =========================

st.subheader("⚙️ Model Selection")

model_option = st.selectbox(
    "Pilih Algoritma",
    ["Decision Tree", "KNN", "SVM", "Neural Network"]
)

st.divider()

# =========================
# INPUT SECTION
# =========================

st.subheader("📝 Input Session Information")

col1, col2 = st.columns(2)

with col1:

    Administrative = st.number_input(
        "Administrative",
        min_value=0,
        value=0
    )

    Administrative_Duration = st.number_input(
        "Administrative Duration",
        min_value=0.0,
        value=0.0
    )

    Informational = st.number_input(
        "Informational",
        min_value=0,
        value=0
    )

    Informational_Duration = st.number_input(
        "Informational Duration",
        min_value=0.0,
        value=0.0
    )

    ProductRelated = st.number_input(
        "Product Related",
        min_value=0,
        value=0
    )

    ProductRelated_Duration = st.number_input(
        "Product Related Duration",
        min_value=0.0,
        value=0.0
    )

    BounceRates = st.number_input(
        "Bounce Rates",
        min_value=0.0,
        value=0.0
    )

    ExitRates = st.number_input(
        "Exit Rates",
        min_value=0.0,
        value=0.0
    )

with col2:

    PageValues = st.number_input(
        "Page Values",
        min_value=0.0,
        value=0.0
    )

    SpecialDay = st.number_input(
        "Special Day",
        min_value=0.0,
        value=0.0
    )

    Month = st.selectbox(
        "Month",
        ["Feb", "Mar", "May", "June", "Jul", "Sep", "Oct", "Nov", "Dec"]
    )

    OperatingSystems = st.number_input(
        "Operating Systems",
        min_value=1,
        value=1
    )

    Browser = st.number_input(
        "Browser",
        min_value=1,
        value=1
    )

    Region = st.number_input(
        "Region",
        min_value=1,
        value=1
    )

    TrafficType = st.number_input(
        "Traffic Type",
        min_value=1,
        value=1
    )

    VisitorType = st.selectbox(
        "Visitor Type",
        ["Returning_Visitor", "Other"]
    )

    Weekend = st.selectbox(
        "Weekend",
        [False, True]
    )

st.divider()

# =========================
# BUTTON
# =========================

predict_button = st.button(
    "🚀 Predict Purchase Intention",
    use_container_width=True
)

# =========================
# PREDICTION
# =========================

if predict_button:

    try:

        if model_option == "Decision Tree":
            model = joblib.load("models/model_dcc3.joblib")
            scaler = joblib.load("scalers/scaler_dcc3.joblib")

        elif model_option == "KNN":
            model = joblib.load("models/model_knn.joblib")
            scaler = joblib.load("scalers/scaler_knn.joblib")

        elif model_option == "SVM":
            model = joblib.load("models/model_svm.joblib")
            scaler = joblib.load("scalers/scaler_svm.joblib")

        else:
            model = joblib.load("models/model_nn.joblib")
            scaler = joblib.load("scalers/scaler_nn.joblib")

        input_data = pd.DataFrame([{
            "Administrative": Administrative,
            "Administrative_Duration": Administrative_Duration,
            "Informational": Informational,
            "Informational_Duration": Informational_Duration,
            "ProductRelated": ProductRelated,
            "ProductRelated_Duration": ProductRelated_Duration,
            "BounceRates": BounceRates,
            "ExitRates": ExitRates,
            "PageValues": PageValues,
            "SpecialDay": SpecialDay,
            "OperatingSystems": OperatingSystems,
            "Browser": Browser,
            "Region": Region,
            "TrafficType": TrafficType,
            "Weekend": int(Weekend),

            "Month_Dec": 1 if Month == "Dec" else 0,
            "Month_Feb": 1 if Month == "Feb" else 0,
            "Month_Jul": 1 if Month == "Jul" else 0,
            "Month_June": 1 if Month == "June" else 0,
            "Month_Mar": 1 if Month == "Mar" else 0,
            "Month_May": 1 if Month == "May" else 0,
            "Month_Nov": 1 if Month == "Nov" else 0,
            "Month_Oct": 1 if Month == "Oct" else 0,
            "Month_Sep": 1 if Month == "Sep" else 0,

            "VisitorType_Other": 1 if VisitorType == "Other" else 0,
            "VisitorType_Returning_Visitor": 1 if VisitorType == "Returning_Visitor" else 0
        }])

        input_data = input_data.reindex(
            columns=scaler.feature_names_in_,
            fill_value=0
        )

        input_scaled = scaler.transform(input_data)

        prediction = model.predict(input_scaled)

        st.divider()
        st.subheader("📊 Prediction Result")

        if prediction[0] == 1:

            st.success("""
### 🟢 PURCHASE

Pelanggan memiliki kemungkinan tinggi untuk melakukan pembelian.
""")

            st.info("""
📌 Insight

Pengunjung menunjukkan karakteristik yang mirip dengan pelanggan yang
berhasil melakukan transaksi pada data historis.
""")

        else:

            st.error("""
### 🔴 NO PURCHASE

Pelanggan memiliki kemungkinan rendah untuk melakukan pembelian.
""")

            st.warning("""
📌 Insight

Perilaku pengunjung masih belum cukup kuat untuk mengindikasikan
terjadinya transaksi pembelian.
""")

        st.divider()

        st.subheader("📋 Session Summary")

        summary = pd.DataFrame({
            "Feature": input_data.columns,
            "Value": input_data.iloc[0].values
        })

        st.dataframe(
            summary,
            use_container_width=True
        )

    except Exception as e:
        st.error(f"Terjadi error: {e}")