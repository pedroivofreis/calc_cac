import streamlit as st

# Configuração da página
st.set_page_config(page_title="Eskolare | Calculadora de CAC e LTV", layout="wide")

# Estilos para melhorar a interface
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.title("🚀 Navegação e Apoio")
    
    st.subheader("📖 Glossário de Indicadores")
    with st.expander("O que é CAC?"):
        st.write("**Custo de Aquisição de Cliente.** É o quanto você gasta (Marketing + Operação + Vendas) para trazer uma nova escola.")
    
    with st.expander("O que é LTV?"):
        st.write("**Lifetime Value.** O faturamento total bruto que uma escola gera durante todo o tempo de contrato com a Eskolare.")
        
    with st.expander("O que é Payback?"):
        st.write("**Tempo de Retorno.** Quantos meses a escola precisa pagar de mensalidade para cobrir o que você gastou para conquistá-la.")

    st.divider()
    
    # --- DISCLAIMER LEGAL ---
    st.subheader("⚖️ Disclaimer")
    st.caption("""
    Os cálculos apresentados são estimativas baseadas em entradas manuais e médias de mercado da região Norte/Nordeste (2026). 
    Este relatório é uma simulação de viabilidade e não constitui garantia de faturamento futuro.
    """)

    st.divider()

    # --- SUA ASSINATURA ---
    st.markdown("### ✍️ Autoria")
    st.success("**Criado por Pedro Reis**")
    st.caption("Inteligência de Mercado & Estratégia | Eskolare")

# --- CONTEÚDO PRINCIPAL ---
st.title("📊 Calculadora Comercial de CAC e LTV")
st.write("Utilize esta ferramenta para medir a viabilidade econômica das prospecções. **Atenção: Preencha todos os dados considerando o período de 1 MÊS.**")

# Divisão de Colunas para Inputs
col1, col2 = st.columns(2)

with col1:
    st.subheader("💰 Custos da Operação (MENSAL)")
    mkt = st.number_input("Custo MENSAL de Marketing (R$)", value=5000.0, help="Gasto total no mês com anúncios, eventos e brindes.")
    ops = st.number_input("Custo MENSAL Operacional (R$)", value=2000.0, help="Gasto total no mês com softwares (CRM) e viagens do time.")
    pessoal = st.number_input("Custo MENSAL do Time (R$)", value=15000.0, help="Soma de salários, encargos e comissões do time de vendas no mês.")

with col2:
    st.subheader("📈 Performance (No mesmo MÊS)")
    novas = st.number_input("Novas Escolas Fechadas no Mês", value=5, min_value=1, help="Total de contratos assinados exatamente neste mês.")
    ticket = st.number_input("Ticket Médio MENSAL (R$)", value=1200.0, help="Receita média mensal gerada por UMA escola para a Eskolare.")
    retencao = st.slider("Meses de Retenção Estimados", 12, 120, 36, help="Tempo total estimado (em meses) que a escola deve ficar na base.")

# Cálculos Lógicos
investimento_total = mkt + ops + pessoal
cac = investimento_total / novas
ltv = ticket * retencao
relacao_ltv_cac = ltv / cac
payback = cac / ticket

st.divider()

# Exibição das Métricas Principais
m_col1, m_col2, m_col3, m_col4 = st.columns(4)

m_col1.metric("Investimento Total (Mês)", f"R$ {investimento_total:,.2f}")
m_col2.metric("CAC (Custo por Escola)", f"R$ {cac:,.2f}")
m_col3.metric("LTV Estimado (Por Escola)", f"R$ {ltv:,.2f}")
m_col4.metric("LTV / CAC", f"{relacao_ltv_cac:.1f}x")

st.divider()

# Alerta de Viabilidade
if relacao_ltv_cac >= 3:
    st.success(f"🌟 **Excelente Saúde Financeira!** O retorno do cliente é de {relacao_ltv_cac:.1f} vezes o seu custo de aquisição. O payback ocorre em aproximadamente {payback:.1f} meses.")
elif relacao_ltv_cac >= 1:
    st.warning(f"⚠️ **Atenção:** O LTV/CAC de {relacao_ltv_cac:.1f}x indica que a operação se paga, mas a margem é apertada. O payback é de {payback:.1f} meses.")
else:
    st.error(f"🚨 **Risco Crítico:** Você está gastando mais para trazer a escola do que ela gera de receita. LTV/CAC abaixo de 1x.")