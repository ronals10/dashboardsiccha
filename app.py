import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

# ======================
# CONFIGURACIÓN GENERAL
# ======================
st.set_page_config(
    page_title="Iris Dashboard",
    layout="wide",
    page_icon="🌸"
)

st.title("🌸 Dashboard Interactivo - Dataset Iris")
st.write("Visualización profesional del dataset Iris usando Streamlit + Plotly")

# ======================
# CARGA DE DATOS
# ======================
df = sns.load_dataset("iris")

# ======================
# SIDEBAR
# ======================
st.sidebar.header("⚙️ Filtros")

species = st.sidebar.multiselect(
    "Selecciona especie:",
    options=df["species"].unique(),
    default=df["species"].unique()
)

filtered_df = df[df["species"].isin(species)]

# ======================
# KPIs
# ======================
col1, col2, col3 = st.columns(3)

col1.metric("Total registros", len(filtered_df))
col2.metric("Especies seleccionadas", filtered_df["species"].nunique())
col3.metric("Promedio Petal Length", round(filtered_df["petal_length"].mean(), 2))

st.divider()

# ======================
# GRÁFICO 1 - SCATTER
# ======================
st.subheader("📊 Relación Sepal vs Petal")

fig1 = px.scatter(
    filtered_df,
    x="sepal_length",
    y="petal_length",
    color="species",
    color_continuous_scale="viridis",
    color_discrete_sequence=px.colors.sequential.Viridis,
    title="Sepal Length vs Petal Length"
)

st.plotly_chart(fig1, use_container_width=True)

# ======================
# GRÁFICO 2 - HISTOGRAMA
# ======================
st.subheader("📈 Distribución de variables")

variable = st.selectbox(
    "Selecciona variable:",
    ["sepal_length", "sepal_width", "petal_length", "petal_width"]
)

fig2 = px.histogram(
    filtered_df,
    x=variable,
    color="species",
    color_discrete_sequence=px.colors.sequential.Viridis,
    barmode="overlay"
)

st.plotly_chart(fig2, use_container_width=True)

# ======================
# GRÁFICO 3 - PAIRPLOT SIMPLIFICADO
# ======================
st.subheader("🔬 Vista multivariable")

fig3 = px.scatter_matrix(
    filtered_df,
    dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"],
    color="species",
    color_discrete_sequence=px.colors.sequential.Viridis
)

st.plotly_chart(fig3, use_container_width=True)

# ======================
# DATOS
# ======================
with st.expander("📄 Ver datos"):
    st.dataframe(filtered_df)
