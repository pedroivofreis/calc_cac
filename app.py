import streamlit as st

# Configuração da página
st.set_page_config(page_title="Eskolare | Calculadora de CAC e LTV", layout="wide")

# CSS apenas para esconder o rodapé, sem mexer em cores!
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
st.write("Utilize esta ferramenta para medir a viabilidade econômica das prospecções. **Todos os custos e entradas devem refletir o período de 1 MÊS.**")

# Divisão de Colunas para Inputs
col1, col2 = st.columns(2)

with col1:
    st.subheader("💰 Custos da Operação")
    st.info("Preencha o que foi gasto **no mês**.")
    mkt = st.number_input("Custo de Marketing (Mensal em R$)", value=5000.0, help="Valor gasto em anúncios, eventos, brindes, etc. durante 1 mês.")
    ops = st.number_input("Custo Operacional (Mensal em R$)", value=2000.0, help="Softwares, viagens e ferramentas utilizadas pelo time durante 1 mês.")
    pessoal = st.number_input("Custo do Time (Mensal em R$)", value=15000.0, help="Soma de salários e comissões do time de vendas pagos no mês.")

with col2:
    st.subheader("📈 Performance")
    st.info("Preencha os resultados **do mesmo mês**.")
    novas = st.number_input("Novas Escolas Fechadas (No Mês)", value=5, min_value=1, help="Total de contratos assinados neste mesmo mês.")
    ticket = st.number_input("Ticket Médio Mensal por Escola (R$)", value=1200.0, help="Receita média que UMA escola gera por mês.")
    retencao = st.slider("Meses de Retenção Estimados (Total)", 12, 120, 24, help="Tempo total que a escola deve ficar na base da Eskolare.")

# Cálculos Lógicos
investimento_total = mkt + ops + pessoal
cac = investimento_total / novas
ltv = ticket * retencao
relacao_ltv_cac = ltv / cac
payback = cac / ticket

st.divider()

# --- EXIBIÇÃO DAS MÉTRICAS COM BORDAS NATIVAS ---
st.subheader("📊 Resultados da Operação")
m_col1, m_col2, m_col3, m_col4 = st.columns(4)

# Usando st.container(border=True) para criar o card perfeito
with m_col1:
    with st.container(border=True):
        st.metric("Invest. Total (Mensal)", f"R$ {investimento_total:,.2f}")

with m_col2:
    with st.container(border=True):
        st.metric("CAC", f"R$ {cac:,.2f}")

with m_col3:
    with st.container(border=True):
        st.metric("LTV Estimado", f"R$ {ltv:,.2f}")

with m_col4:
    with st.container(border=True):
        # Usando a funcionalidade 'delta' para adicionar cor (Verde/Vermelho) de forma legível
        status_texto = "Saudável" if relacao_ltv_cac >= 3 else "Risco"
        cor_status = "normal" if relacao_ltv_cac >= 3 else "inverse"
        st.metric("LTV / CAC", f"{relacao_ltv_cac:.1f}x", delta=status_texto, delta_color=cor_status)

st.divider()

# Alerta de Viabilidade
if relacao_ltv_cac >= 3:
    st.success(f"🌟 **Excelente Saúde Financeira!** O retorno do cliente é de {relacao_ltv_cac:.1f}x o seu custo. O payback ocorre em aproximadamente {payback:.1f} meses.")
else:
    st.warning(f"⚠️ **Atenção:** O CAC está elevado. O payback de {payback:.1f} meses pode impactar o fluxo de caixa a curto prazo.")