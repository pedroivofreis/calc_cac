import streamlit as st

st.set_page_config(page_title="Calculadora Eskolare: CAC & LTV", layout="wide")

st.title("📊 Calculadora de Viabilidade Comercial (CAC/LTV)")
st.markdown("---")

# Sidebar para Inputs
st.sidebar.header("📥 Parâmetros de Custo")
custo_marketing = st.sidebar.number_input("Custo de Marketing (R$)", value=10000)
custo_operacional = st.sidebar.number_input("Custo Operacional/Ferramentas (R$)", value=5000)
custo_time = st.sidebar.number_input("Custo do Time (Salários/Comissões) (R$)", value=25000)

st.sidebar.header("🎯 Resultados do Período")
novas_escolas = st.sidebar.number_input("Quantidade de Novas Escolas Fechadas", value=5, min_value=1)

st.sidebar.header("💰 Perfil da Escola (LTV)")
ticket_medio = st.sidebar.number_input("Ticket Médio Mensal por Escola (R$)", value=1000)
tempo_retencao = st.sidebar.slider("Tempo de Retenção Médio (Meses)", 1, 120, 36) # 36 meses = 3 anos

# Cálculos
custo_total = custo_marketing + custo_operacional + custo_time
cac = custo_total / novas_escolas
ltv = ticket_medio * tempo_retencao
relacao_ltv_cac = ltv / cac
payback = cac / ticket_medio

# Exibição dos Resultados
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("CAC (Custo por Escola)", f"R$ {cac:,.2f}")
    st.caption("Quanto custa conquistar UMA escola.")

with col2:
    st.metric("LTV (Valor do Cliente)", f"R$ {ltv:,.2f}")
    st.caption("Quanto essa escola traz de receita no ciclo total.")

with col3:
    color = "normal" if relacao_ltv_cac >= 3 else "inverse"
    st.metric("LTV / CAC", f"{relacao_ltv_cac:.2f}x", delta=None, delta_color=color)
    st.caption("Saúde do negócio (Ideal > 3x).")

st.markdown("---")

# Insights Estratégicos
st.subheader("💡 Análise de Viabilidade")
if payback <= 6:
    st.success(f"Excelente! Você recupera o investimento em {payback:.1f} meses.")
elif payback <= 12:
    st.warning(f"Atenção: O payback é de {payback:.1f} meses. Considere otimizar os custos de time.")
else:
    st.error(f"Risco: O payback de {payback:.1f} meses é muito longo para o mercado atual.")

st.info(f"O Custo Total da sua operação no período foi de R$ {custo_total:,.2f}")