import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Customer Shopping Behaviour Analysis", layout="wide")

st.title("🛍️ Customer Shopping Behaviour Analysis")
st.markdown("**By Shabnoor Qureshi** | BCA (AI & Data Science), Graphic Era University")
st.markdown("---")

# ── Load Data ──────────────────────────────────────────────────────────────────
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

uploaded_file = st.sidebar.file_uploader("Upload your CSV dataset", type=["csv"])

if uploaded_file:
    df = load_data(uploaded_file)
else:
    # Generate sample data so the app works even without a file
    np.random.seed(42)
    n = 500
    df = pd.DataFrame({
        "Age": np.random.randint(18, 65, n),
        "Gender": np.random.choice(["Male", "Female"], n),
        "Purchase Amount (USD)": np.round(np.random.uniform(10, 500, n), 2),
        "Category": np.random.choice(["Clothing", "Electronics", "Footwear", "Accessories", "Beauty"], n),
    })
    st.sidebar.info("Using sample data. Upload your CSV to analyse your own dataset.")

# ── Sidebar Filters ────────────────────────────────────────────────────────────
st.sidebar.markdown("### Filters")
gender_filter = st.sidebar.multiselect("Gender", df["Gender"].unique(), default=list(df["Gender"].unique()))
category_filter = st.sidebar.multiselect("Category", df["Category"].unique(), default=list(df["Category"].unique()))
age_min, age_max = int(df["Age"].min()), int(df["Age"].max())
age_range = st.sidebar.slider("Age Range", age_min, age_max, (age_min, age_max))

filtered = df[
    (df["Gender"].isin(gender_filter)) &
    (df["Category"].isin(category_filter)) &
    (df["Age"] >= age_range[0]) &
    (df["Age"] <= age_range[1])
]

# ── KPI Cards ──────────────────────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Customers", len(filtered))
col2.metric("Avg Purchase (USD)", f"${filtered['Purchase Amount (USD)'].mean():.2f}")
col3.metric("Total Revenue (USD)", f"${filtered['Purchase Amount (USD)'].sum():,.0f}")
col4.metric("Top Category", filtered["Category"].mode()[0] if not filtered.empty else "N/A")

st.markdown("---")

# ── Charts ─────────────────────────────────────────────────────────────────────
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Purchases by Category")
    cat_counts = filtered["Category"].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.bar(cat_counts.index, cat_counts.values, color=["#4C72B0","#DD8452","#55A868","#C44E52","#8172B2"])
    ax1.set_xlabel("Category")
    ax1.set_ylabel("Number of Purchases")
    ax1.tick_params(axis='x', rotation=30)
    st.pyplot(fig1)

with col_b:
    st.subheader("Gender Distribution")
    gender_counts = filtered["Gender"].value_counts()
    fig2, ax2 = plt.subplots()
    ax2.pie(gender_counts.values, labels=gender_counts.index, autopct="%1.1f%%",
            colors=["#4C72B0","#DD8452"], startangle=90)
    ax2.axis("equal")
    st.pyplot(fig2)

col_c, col_d = st.columns(2)

with col_c:
    st.subheader("Avg Purchase Amount by Category")
    avg_purchase = filtered.groupby("Category")["Purchase Amount (USD)"].mean().sort_values(ascending=False)
    fig3, ax3 = plt.subplots()
    ax3.barh(avg_purchase.index, avg_purchase.values, color="#55A868")
    ax3.set_xlabel("Avg Purchase Amount (USD)")
    st.pyplot(fig3)

with col_d:
    st.subheader("Age Distribution of Customers")
    fig4, ax4 = plt.subplots()
    ax4.hist(filtered["Age"], bins=15, color="#C44E52", edgecolor="white")
    ax4.set_xlabel("Age")
    ax4.set_ylabel("Count")
    st.pyplot(fig4)

# ── Raw Data ───────────────────────────────────────────────────────────────────
st.markdown("---")
with st.expander("View Raw Data"):
    st.dataframe(filtered.reset_index(drop=True))
