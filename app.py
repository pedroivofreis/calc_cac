import streamlit as st

st.set_page_config(page_title="Eskolare | Inteligência de Mercado", layout="wide")

# --- ESTILIZAÇÃO CUSTOMIZADA ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: GLOSSÁRIO E CRÉDITOS ---
with st.sidebar:
    st.image("https://via.placeholder.com/150x50?text=ESKOLARE", width=150)
    st.title("📖 Glossário de Apoio")
    
    with st.expander("O que é CAC?"):
        st.write("Custo de Aquisição de Cliente (Total Investido / Novos Contratos).")
        
    with st.expander("O que é LTV?"):
        st.write("Lifetime Value (Ticket Mensal x Meses de Retenção).")

    with st.expander("O que é Payback?"):
        st.write("Tempo necessário para a receita da escola cobrir o custo de aquisição.")
    
    st.divider()
    
    # --- SUA ASSINATURA AQUI ---
    st.markdown("### 👨‍💻 Créditos")
    st.info("**Desenvolvido por Pedro Reis**")
    st.caption("Inteligência de Mercado & Estratégia")
    
    st.divider()
    st.caption("⚠️ **Disclaimer:** Ferramenta de simulação baseada em dados históricos de 2026.")

# --- ÁREA PRINCIPAL ---
st.title("📊 Calculadora de Viabilidade Comercial")
st.markdown("Análise de eficiência para expansão nas regiões Norte e Nordeste.")

col_in1, col_in2 = st.columns(2)

with col_in1:
    st.subheader("🛠️ Custos da Operação (Mês)")
    mkt = st.number_input("Investimento em Marketing (R$)", value=5000.0)
    ops = st.number_input("Custos Operacionais (R$)", value=2000.0)
    time = st.number_input("Custo de Pessoal (R$)", value=15000.0)

with col_in2:
    st.subheader("🎯 Performance e Receita")
    novos = st.number_input("Novas Escolas Fechadas (Mês)", value=2, min_value=1)
    ticket = st.number_input("Ticket Médio Mensal (R$)", value=1200.0)
    meses = st.slider("Expectativa de Retenção (Meses)", 6, 120, 36)

st.divider()

# Cálculos
custo_total = mkt + ops + time
cac = custo_total / novos
ltv_total = ticket * meses
relacao = ltv_total / cac
payback = cac / ticket

# Métricas
c1, c2, c3, c4 = st.columns(4)
c1.metric("Investimento Total", f"R$ {custo_total:,.2f}")
c2.metric("CAC", f"R$ {cac:,.2f}")
c3.metric("LTV Estimado", f"R$ {ltv_total:,.2f}")
c4.metric("LTV / CAC", f"{relacao:.1f}x")

st.divider()

# Análise
if relacao >= 3:
    st.success(f"✅ **Operação Saudável:** Payback em {payback:.1f} meses.")
else:
    st.error(f"⚠️ **Atenção:** CAC alto. Payback em {payback:.1f} meses.")