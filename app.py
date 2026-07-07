import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard Analítico - Red San Juan", layout="wide")

# Cargar datos
try:
    df = pd.read_csv("dataset_personal.csv")
except:
    st.error("Por favor, coloca el archivo 'dataset_personal.csv' en el mismo repositorio.")
    st.stop()

# Sidebar / Filtros (Igual al modelo)
st.sidebar.header("Filtros")
filtro_diabetes = st.sidebar.multiselect("Resultado Diabetes:", options=[0, 1], default=[0, 1])
df_filtrado = df[df['Resultado_Diabetes'].isin(filtro_diabetes)]

# Título Principal
st.title("📊 Dashboard Analítico - Predicción de Enfermedades (Diabetes)")

# KPIs Superiores
total_pacientes = len(df_filtrado)
casos_riesgo = int(df_filtrado['Resultado_Diabetes'].sum())
tasa_riesgo = (casos_riesgo / total_pacientes) * 100 if total_pacientes > 0 else 0

kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("Total Registros", total_pacientes)
kpi2.metric("Pacientes con Riesgo", casos_riesgo)
kpi3.metric("% Tasa de Riesgo", f"{tasa_riesgo:.2f}%")

st.write("---")

# Gráfico 1: Análisis Descriptivo
st.subheader("Pacientes según Nivel de Glucosa y Resultado Diagnóstico")
fig1, ax1 = plt.subplots(figsize=(10, 3.5))
sns.scatterplot(data=df_filtrado, x='Riesgo_Metabolico', y='Nivel_Glucosa', hue='Resultado_Diabetes', palette='coolwarm', ax=ax1)
st.pyplot(fig1)

# Gráfico 2: Distribución Histograma
st.subheader("Distribución del Indicador Derivado: Riesgo Metabólico")
fig2, ax2 = plt.subplots(figsize=(10, 3))
df_filtrado["Riesgo_Metabolico"].hist(bins=20, color="#1f77b4", edgecolor="white", ax=ax2)
st.pyplot(fig2)
