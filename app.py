import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Dashboard Financeiro", layout="wide")

st.title("📊 Painel de Análise Financeira")
st.write("Análise rápida de performance e fluxos de caixa.")

# Criando dados financeiros fictícios
df = pd.DataFrame({
    'Mes': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    'Receita': [5000, 6200, 5800, 7100, 6500, 8000],
    'Despesas': [3000, 3200, 3100, 3500, 3400, 4000]
})

# Filtro lateral
st.sidebar.header("Filtros")
mes_selecionado = st.sidebar.multiselect("Selecione os meses:", df['Mes'], default=df['Mes'])

# Filtrando dados
df_filtrado = df[df['Mes'].isin(mes_selecionado)]

# Exibindo métricas
col1, col2 = st.columns(2)
col1.metric("Receita Total", f"R$ {df_filtrado['Receita'].sum()}")
col2.metric("Despesas Total", f"R$ {df_filtrado['Despesas'].sum()}")

# Gráfico
st.line_chart(df_filtrado.set_index('Mes'))

st.write("Dados brutos:", df_filtrado)