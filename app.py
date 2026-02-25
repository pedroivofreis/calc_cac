import streamlit as st

# Configuração da página
st.set_page_config(page_title="Eskolare | Calculadora de CAC e LTV", layout="wide")

# Remove apenas o rodapé padrão, sem mexer nas cores dos cards
st.markdown("""
    <style>
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.title("🚀 Navegação e Apoio")
    
    st.subheader("📖 Glossário de Indicadores")
    with st.expander("O que é CAC?"):
        st.write("Custo de Aquisição de Cliente. É o quanto você gasta (Marketing + Vendas) para trazer uma nova escola.")
    
    with st.expander("O que é LTV?"):
        st.write("Lifetime Value. O faturamento total bruto que uma escola gera durante todo o tempo de contrato.")
        
    with st.expander("O que é Payback?"):
        st.write("Tempo de Retorno. Quantos meses a escola precisa pagar para 'se pagar'.")

    st.divider()
    
    # --- DISCLAIMER LEGAL ---
    st.subheader("⚖️ Disclaimer")
    st.caption("""
    Os cálculos apresentados são estimativas baseadas em entradas manuais e médias de mercado de 2026. 
    Este relatório não constitui garantia de faturamento ou lucro futuro.
    """)

    st.divider()

    # --- SUA ASSINATURA ---
    st.markdown("### ✍️ Autoria")
    st.success("**Criado por Pedro Reis**")
    st.caption("Estrategista de Negócios | Eskolare 2026")

# --- CONTEÚDO PRINCIPAL ---
st.title("📊 Calculadora Comercial de CAC e LTV")
st.write("Utilize esta ferramenta para medir a viabilidade econômica das prospecções.")

# Divisão de Colunas para Inputs
col1, col2 = st.columns(2)

with col1:
    st.subheader("💰 Custos Mensais")
    mkt = st.number_input("Custo de Marketing (R$)", value=5000.0, help="Valor total gasto em anúncios e eventos no MÊS.")
    ops = st.number_input("Custo Operacional (R$)", value=2000.0, help="Softwares e ferramentas utilizadas pelo time no MÊS.")
    pessoal = st.number_input("Custo de Time (R$)", value=15000.0, help="Soma de salários e comissões do time de vendas no MÊS.")

with col2:
    st.subheader("📈 Performance")
    novas = st.number_input("Novas Escolas Fechadas", value=5, min_value=1, help="Total de contratos assinados no MÊS.")
    ticket = st.number_input("Ticket Médio Mensal (R$)", value=1200.0, help="Receita média mensal gerada por UMA escola.")
    retencao = st.slider("Meses de Retenção Estimados", 12, 120, 36, help="Tempo total que a escola deve ficar na base (ANUAL).")

# Cálculos Lógicos
investimento_total = mkt + ops + pessoal
cac = investimento_total / novas
ltv = ticket * retencao
relacao_ltv_cac = ltv / cac
payback = cac / ticket

st.divider()

# Exibição das Métricas Principais
m_col1, m_col2, m_col3, m_col4 = st.columns(4)

m_col1.metric("Investimento Total", f"R$ {investimento_total:,.2f}")
m_col2.metric("CAC", f"R$ {cac:,.2f}")
m_col3.metric("LTV Estimado", f"R$ {ltv:,.2f}")
m_col4.metric("LTV / CAC", f"{relacao_ltv_cac:.1f}x")

st.divider()

# Alerta de Viabilidade
if relacao_ltv_cac >= 3:
    st.success(f"🌟 **Excelente Saúde Financeira!** O retorno do cliente é de {relacao_ltv_cac:.1f}x o seu custo. O payback ocorre em aproximadamente {payback:.1f} meses.")
else:
    st.warning(f"⚠️ **Atenção:** O CAC está elevado. O payback de {payback:.1f} meses pode impactar o fluxo de caixa a curto prazo.")