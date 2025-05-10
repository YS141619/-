import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/사용자명/저장소명/브랜치명/seoul_population.csv"
    df = pd.read_csv(url)
    df = df.rename(columns={"자치구": "District", "인구수": "Population"})
    return df

df = load_data()

st.title("🏙️ 서울시 자치구별 인구수 시각화")
st.markdown("📊 서울시 자치구별 인구 데이터를 시각화한 대시보드입니다.")

fig_bar = px.bar(df, x="District", y="Population", title="자치구별 인구수", text="Population")
st.plotly_chart(fig_bar)

fig_pie = px.pie(df, names="District", values="Population", title="서울시 인구 분포 (파이차트)")
st.plotly_chart(fig_pie)
