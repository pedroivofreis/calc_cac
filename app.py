import streamlit as st

# Configuração da página
st.set_page_config(page_title="Eskolare | Calculadora de CAC e LTV", layout="wide")

# CSS para esconder o rodapé nativo e dar destaque ao campo principal
st.markdown("""
    <style>
    footer {visibility: hidden;}
    /* Destaca sutilmente a caixa de texto principal */
    div[data-baseweb="input"] {
        border-radius: 6px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.title("🚀 Navegação e Apoio")
    
    st.subheader("📖 Glossário de Indicadores")
    with st.expander("O que é CAC?"):
        st.write("Custo de Aquisição de Cliente. É o quanto você gasta (Marketing + Vendas + Operação) para trazer uma nova escola.")
    
    with st.expander("O que é LTV?"):
        st.write("Lifetime Value. O faturamento total que UMA escola gera para a Eskolare (Transação + Mensalidade) durante todo o tempo de contrato.")
        
    with st.expander("O que é Payback?"):
        st.write("Tempo de Retorno. Quantos meses a escola precisa transacionar na plataforma para pagar o custo que tivemos para conquistá-la.")

    st.divider()
    
    st.subheader("⚖️ Disclaimer")
    st.caption("""
    Os cálculos apresentados são estimativas baseadas no modelo de negócio de Take Rate + SaaS. 
    Este relatório não constitui garantia de faturamento futuro.
    """)

    st.divider()

    st.markdown("### ✍️ Autoria")
    st.success("**Criado por Pedro Reis**")
    st.caption("Estrategista de Negócios | Eskolare 2026")

# --- CONTEÚDO PRINCIPAL ---
st.title("📊 Calculadora Comercial de CAC e LTV")
st.write("Meça a viabilidade econômica das prospecções baseada na receita real (Take Rate + Mensalidade).")

# Divisão de Colunas para Inputs
col1, col2 = st.columns(2)

with col1:
    st.subheader("💰 Custos da Operação")
    st.info("Preencha o que foi gasto **no mês** (Rateie custos anuais).")
    
    # Destaque visual para o Custo da Ação/Evento
    st.markdown("🎯 **Variável Principal de Marketing**")
    mkt = st.number_input("Custo da Ação ou Evento (Rateio Mensal - R$)", value=5000.0)
    
    st.markdown("---")
    ops = st.number_input("Custos Extras (Mensal em R$)", value=2000.0)
    pessoal = st.number_input("Custo do Time (Mensal em R$)", value=28000.0)

with col2:
    st.subheader("📈 Modelo de Receita (Por Escola)")
    st.info("Preencha os dados do contrato.")
    novas = st.number_input("Novas Escolas Fechadas (No Mês)", value=5, min_value=1)
    
    gmv_anual = st.number_input("GMV / Faturamento ANUAL da Escola (R$)", value=1000000.0, step=50000.0, help="Volume total transacionado pela escola no ano.")
    
    # Sub-colunas para as taxas
    c_taxa1, c_taxa2 = st.columns(2)
    with c_taxa1:
        take_rate = st.number_input("Take Rate Efetivo (%)", value=0.71, step=0.01, format="%.2f", help="Porcentagem que fica com a Eskolare.")
    with c_taxa2:
        mensalidade = st.number_input("Mensalidade Fixa (R$)", value=99.0, step=10.0, help="Assinatura mensal do sistema.")
        
    retencao = st.slider("Meses de Retenção Estimados (Total)", 12, 120, 24, help="Na dúvida, considere o tempo de contrato.")

# --- LÓGICA DE CÁLCULO (O MOTOR COM PRECISÃO MÁXIMA) ---
investimento_total = mkt + ops + pessoal
cac = investimento_total / novas

# 1. Receita de Transação (Take Rate)
receita_transacional_anual = gmv_anual * (take_rate / 100.0)

# 2. Receita de Mensalidade (SaaS)
receita_mensalidade_anual = mensalidade * 12.0

# 3. Receita Total da ESKOLARE por Escola
receita_total_anual_eskolare = receita_transacional_anual + receita_mensalidade_anual
receita_mensal_eskolare = receita_total_anual_eskolare / 12.0

ltv = receita_mensal_eskolare * retencao
relacao_ltv_cac = ltv / cac
payback = cac / receita_mensal_eskolare

st.divider()

# --- EXIBIÇÃO DAS MÉTRICAS (AGORA COM 5 CARDS) ---
st.subheader("📊 Resultados da Operação")
m_col1, m_col2, m_col3, m_col4, m_col5 = st.columns(5)

with m_col1:
    with st.container(border=True):
        st.metric("Invest. Total (Mensal)", f"R$ {investimento_total:,.2f}")

with m_col2:
    with st.container(border=True):
        st.metric("CAC (Por Escola)", f"R$ {cac:,.2f}")

with m_col3:
    with st.container(border=True):
        # Novo Card: MRR Estimado
        st.metric("MRR Estimado", f"R$ {receita_mensal_eskolare:,.2f}")

with m_col4:
    with st.container(border=True):
        st.metric("LTV (Por Escola)", f"R$ {ltv:,.2f}")

with m_col5:
    with st.container(border=True):
        status_texto = "Saudável" if relacao_ltv_cac >= 3 else "Risco"
        cor_status = "normal" if relacao_ltv_cac >= 3 else "inverse"
        st.metric("LTV / CAC", f"{relacao_ltv_cac:.2f}x", delta=status_texto, delta_color=cor_status)

st.divider()

# --- ALERTAS E INSIGHTS ---
if relacao_ltv_cac >= 3:
    st.success(f"🌟 **Excelente Saúde Financeira!** O retorno total do cliente é de {relacao_ltv_cac:.2f}x o custo de aquisição. O payback ocorre em aproximadamente {payback:.1f} meses.")
else:
    st.warning(f"⚠️ **Atenção:** A relação LTV/CAC está apertada. O payback de {payback:.1f} meses pode impactar o fluxo de caixa a curto prazo.")