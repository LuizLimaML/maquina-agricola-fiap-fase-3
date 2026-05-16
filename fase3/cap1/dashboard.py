import streamlit as st
import pandas as pd
import plotly.express as px

st.title("FarmTech - Dashboard de Sensores")

df = pd.read_csv('../../fase2/sensores.csv')
df['data_hora'] = pd.to_datetime(df['data_hora'])

# filtro de cultura
culturas = ['Todas'] + sorted(df['cultura'].unique().tolist())
escolha = st.sidebar.selectbox("Cultura", culturas)

if escolha != 'Todas':
    df = df[df['cultura'] == escolha]

# metricas
col1, col2, col3, col4 = st.columns(4)
col1.metric("Umidade media", f"{df['umidade'].mean():.2f}")
col2.metric("pH medio", f"{df['ph'].mean():.2f}")
col3.metric("Temp media", f"{df['temperatura'].mean():.2f}")
col4.metric("Irrigacoes", int(df['irrigacao'].sum()))

# grafico de linha
st.subheader("Umidade ao longo do tempo")
fig1 = px.line(df.sort_values('data_hora'), x='data_hora', y='umidade')
st.plotly_chart(fig1)

# grafico de barras
st.subheader("Media de pH, fosforo e potassio por cultura")
df_full = pd.read_csv('../../fase2/sensores.csv')
media_cultura = df_full.groupby('cultura')[['ph', 'fosforo', 'potassio']].mean().reset_index()
fig2 = px.bar(media_cultura, x='cultura', y=['ph', 'fosforo', 'potassio'], barmode='group')
st.plotly_chart(fig2)

# scatter
st.subheader("Temperatura vs Umidade")
fig3 = px.scatter(df, x='temperatura', y='umidade', color='cultura')
st.plotly_chart(fig3)

# tabela
st.subheader("Dados")
st.dataframe(df)

# alertas
st.subheader("Alertas - umidade baixa (< 40)")
alertas = df[df['umidade'] < 40]
if len(alertas) > 0:
    st.warning(f"{len(alertas)} registros com umidade baixa!")
    st.dataframe(alertas)
else:
    st.success("Nenhum alerta.")
