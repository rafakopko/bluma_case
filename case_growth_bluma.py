import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Configuração da página
st.set_page_config(
    page_title="Case Analista Growth - Bluma",
    page_icon="💅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {
        color: #FF1493;
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 2rem;
    }
    
    .metric-card {
        background-color: #FFF0F5;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #FF1493;
        margin: 0.5rem 0;
    }
    
    .challenge-box {
        background-color: #FF69B4;
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        font-weight: bold;
        font-size: 1.2rem;
        margin: 1rem 0;
    }
    
    .success-box {
        background-color: #90EE90;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #228B22;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding-left: 20px;
        padding-right: 20px;
    }
    
    footer {
        text-align: center;
        color: #666;
        margin-top: 3rem;
        padding: 2rem;
        border-top: 1px solid #eee;
    }
</style>
""", unsafe_allow_html=True)

# Header principal
st.markdown('<h1 class="main-header">💅 Case: Analista de Growth - Mídia Paga</h1>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 🌸 BLUMA BEAUTY")
    st.markdown("*Marketplace de Beleza e Bem-estar*")
    
    # Credenciais do banco
    with st.expander("🗄️ Credenciais do Banco", expanded=False):
        st.code("""
Host: 95.111.240.159
Port: 3306
Database: bluma_case
Username: candidato
Password: bluma123
        """)
    
    st.markdown("---")
    
    # Métricas-alvo
    st.markdown("### 🎯 Métricas-Alvo")
    st.metric("LTV/CARC Atual", "2.33x", delta="Meta: 3.03x (+30%)")
    st.markdown("**Prazo:** 3 meses")
    
    st.markdown("---")
    
    # Informações adicionais
    st.markdown("### 📊 Dados Disponíveis")
    st.markdown("""
    - 50.000 usuários
    - ~150.000 pedidos
    - 120 campanhas
    - Performance diária
    - Eventos de usuário
    - Análise de cohorts
    """)

# Conteúdo principal em tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📋 Contexto do Negócio", 
    "🗄️ Estrutura de Dados", 
    "📊 Queries de Exemplo", 
    "🎯 Orientações"
])

with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🏢 Sobre a Bluma")
        st.markdown("""
        A **Bluma** é um marketplace de beleza e bem-estar que conecta profissionais 
        qualificados com clientes em busca de serviços de qualidade. Atuamos nas 
        principais cidades do Brasil, oferecendo uma plataforma completa para 
        agendamentos de serviços como manicure, massagem, limpeza de pele e muito mais.
        """)
        
        st.markdown("### 🚨 Situação Atual e Desafios")
        st.markdown("""
        **Contexto:** Nos últimos 3 meses, observamos uma deterioração nas métricas 
        principais de aquisição e retenção:
        
        - 📈 **CAC aumentou 35%** (de R$ 67 para R$ 90)
        - 📉 **Taxa de ativação caiu** de 12% para 8% (-4pp)
        - ⚖️ **LTV/CARC atual:** 2.33x (abaixo da meta histórica de 3.0x)
        - 🎯 **Meta:** Aumentar LTV/CARC para 3.03x (+30%) em 3 meses
        - 💰 **Restrição:** Budget de mídia não pode aumentar mais de 10%
        """)
        
        # Gráficos
        st.markdown("### 📊 Visão Geral do Negócio")
        
        # Criar 3 colunas para os gráficos
        graph_col1, graph_col2, graph_col3 = st.columns(3)
        
        with graph_col1:
            # Gráfico de pizza - Canais de aquisição
            channels_data = {
                'Canal': ['Meta Ads', 'Google Ads', 'TikTok Ads', 'Organic', 'Referral'],
                'Participação': [45, 25, 10, 15, 5]
            }
            fig_channels = px.pie(
                values=channels_data['Participação'], 
                names=channels_data['Canal'],
                title="Distribuição de Canais",
                color_discrete_sequence=px.colors.sequential.RdPu_r
            )
            fig_channels.update_layout(height=300, margin=dict(t=40, b=20, l=20, r=20))
            st.plotly_chart(fig_channels, use_container_width=True)
        
        with graph_col2:
            # Gráfico de barras - Serviços
            services_data = {
                'Serviço': ['Manicure', 'Massagem', 'Limpeza Pele', 'Sobrancelhas', 'Depilação'],
                'Ticket Médio': [65, 120, 95, 55, 80],
                'Share': [35, 20, 15, 15, 15]
            }
            fig_services = px.bar(
                x=services_data['Serviço'], 
                y=services_data['Ticket Médio'],
                title="Ticket Médio por Serviço",
                color=services_data['Share'],
                color_continuous_scale='RdPu'
            )
            fig_services.update_layout(height=300, margin=dict(t=40, b=20, l=20, r=20))
            fig_services.update_xaxes(tickangle=45)
            st.plotly_chart(fig_services, use_container_width=True)
        
        with graph_col3:
            # Treemap - Cidades
            cities_data = {
                'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília', 
                          'Curitiba', 'Porto Alegre', 'Salvador', 'Outras'],
                'Participação': [30, 20, 10, 8, 7, 5, 5, 15]
            }
            fig_cities = px.treemap(
                names=cities_data['Cidade'],
                values=cities_data['Participação'],
                title="Distribuição por Cidades",
                color=cities_data['Participação'],
                color_continuous_scale='RdPu'
            )
            fig_cities.update_layout(height=300, margin=dict(t=40, b=20, l=20, r=20))
            st.plotly_chart(fig_cities, use_container_width=True)
    
    with col2:
        st.markdown("### 📈 KPIs Atuais")
        
        # Cards de métricas
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("LTV/CARC", "2.33x", delta="-0.67x (-23%)", delta_color="inverse")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("CAC Médio", "R$ 90", delta="+R$ 23 (+35%)", delta_color="inverse")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Taxa de Ativação", "8%", delta="-4pp", delta_color="inverse")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("AOV", "R$ 95", delta="+R$ 5 (+5%)", delta_color="normal")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Retenção M1", "22%", delta="-3pp", delta_color="inverse")
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown("### 🗄️ Estrutura do Banco de Dados")
    
    # Diagrama ER usando Mermaid
    st.markdown("#### Relacionamentos entre Tabelas")
    mermaid_diagram = """
    graph TD
        A[users<br/>50k registros] --> B[orders<br/>150k registros]
        A --> C[user_events<br/>300k registros]
        A --> D[user_cohorts<br/>4k registros]
        E[paid_media_campaigns<br/>120 registros] --> F[daily_performance<br/>3.6k registros]
        E --> G[ad_creatives<br/>600 registros]
        G --> H[creative_performance<br/>18k registros]
        I[budget_allocation<br/>60 registros] --> E
        
        style A fill:#FFB6C1
        style E fill:#FF69B4
        style B fill:#FFF0F5
        style F fill:#FFF0F5
    """
    
    st.markdown(f"```mermaid\n{mermaid_diagram}\n```")
    
    st.markdown("#### Descrição Detalhada das Tabelas")
    
    # Organizar em 3 colunas
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.expander("👥 users (50.000 registros)"):
            st.markdown("""
            **Dados dos usuários cadastrados**
            - user_id (PK)
            - created_at
            - acquisition_channel
            - acquisition_campaign
            - first_order_date
            - city, state
            - age_group, gender
            """)
        
        with st.expander("🛒 orders (~150.000 registros)"):
            st.markdown("""
            **Pedidos realizados pelos usuários**
            - order_id (PK)
            - user_id (FK)
            - order_date
            - order_value
            - service_type
            - status
            - payment_method
            - discount_amount
            """)
        
        with st.expander("📱 user_events (~300.000 registros)"):
            st.markdown("""
            **Eventos de interação dos usuários**
            - event_id (PK)
            - user_id (FK)
            - event_timestamp
            - event_type
            - platform
            - session_id
            """)
    
    with col2:
        with st.expander("📢 paid_media_campaigns (120 registros)"):
            st.markdown("""
            **Campanhas de mídia paga**
            - campaign_id (PK)
            - platform
            - campaign_name
            - campaign_type
            - start_date, end_date
            - daily_budget
            - objective
            """)
        
        with st.expander("📊 daily_performance (~3.600 registros)"):
            st.markdown("""
            **Performance diária das campanhas**
            - date, campaign_id (PK)
            - impressions, clicks
            - spend, conversions
            - conversion_value
            - new_users
            - cpm, cpc, ctr
            """)
        
        with st.expander("🎨 ad_creatives (~600 registros)"):
            st.markdown("""
            **Criativos das campanhas**
            - creative_id (PK)
            - campaign_id (FK)
            - creative_type
            - creative_name
            - launched_date
            - status
            """)
    
    with col3:
        with st.expander("📈 creative_performance (~18.000 registros)"):
            st.markdown("""
            **Performance dos criativos**
            - date, creative_id (PK)
            - impressions, clicks
            - spend, conversions
            - engagement_rate
            """)
        
        with st.expander("👥 user_cohorts (~4.000 registros)"):
            st.markdown("""
            **Análise de cohorts de usuários**
            - cohort_month, user_id (PK)
            - m0_revenue, m1_revenue
            - m2_revenue, m3_revenue
            - m0_orders, m1_orders
            - m2_orders, m3_orders
            """)
        
        with st.expander("💰 budget_allocation (~60 registros)"):
            st.markdown("""
            **Alocação mensal de budget**
            - month, channel (PK)
            - planned_budget
            - actual_spend
            - target_cac, actual_cac
            """)

with tab3:
    st.markdown("### 📊 Queries de Exemplo")
    
    # Sub-tabs para categorias
    subtab1, subtab2, subtab3 = st.tabs(["Análises Básicas", "CAC e LTV", "Análise de Cohorts"])
    
    with subtab1:
        st.markdown("#### Overview Geral")
        st.code("""
-- Visão geral dos usuários e ativação
SELECT 
    acquisition_channel,
    COUNT(*) as total_users,
    COUNT(first_order_date) as activated_users,
    ROUND(COUNT(first_order_date) * 100.0 / COUNT(*), 2) as activation_rate,
    ROUND(AVG(DATEDIFF(first_order_date, created_at)), 1) as avg_days_to_first_order
FROM users 
GROUP BY acquisition_channel
ORDER BY total_users DESC;
        """, language="sql")
        
        st.markdown("#### Performance por Canal")
        st.code("""
-- Performance consolidada por canal de mídia paga
SELECT 
    c.platform,
    COUNT(DISTINCT c.campaign_id) as total_campaigns,
    SUM(dp.spend) as total_spend,
    SUM(dp.impressions) as total_impressions,
    SUM(dp.clicks) as total_clicks,
    SUM(dp.conversions) as total_conversions,
    ROUND(SUM(dp.spend) / SUM(dp.conversions), 2) as cac,
    ROUND(SUM(dp.clicks) * 100.0 / SUM(dp.impressions), 2) as ctr,
    ROUND(SUM(dp.conversions) * 100.0 / SUM(dp.clicks), 2) as cvr
FROM paid_media_campaigns c
JOIN daily_performance dp ON c.campaign_id = dp.campaign_id
GROUP BY c.platform
ORDER BY total_spend DESC;
        """, language="sql")
    
    with subtab2:
        st.markdown("#### CAC por Canal (30 dias)")
        st.code("""
-- CAC por canal nos últimos 30 dias
SELECT 
    c.platform,
    SUM(dp.spend) as spend_30d,
    SUM(dp.new_users) as new_users_30d,
    ROUND(SUM(dp.spend) / NULLIF(SUM(dp.new_users), 0), 2) as cac_30d
FROM paid_media_campaigns c
JOIN daily_performance dp ON c.campaign_id = dp.campaign_id
WHERE dp.date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
GROUP BY c.platform
ORDER BY cac_30d ASC;
        """, language="sql")
        
        st.markdown("#### LTV por Canal (90 dias)")
        st.code("""
-- LTV dos usuários adquiridos por canal (90 dias)
SELECT 
    u.acquisition_channel,
    COUNT(DISTINCT u.user_id) as users,
    COUNT(o.order_id) as total_orders,
    ROUND(SUM(o.order_value), 2) as total_revenue,
    ROUND(AVG(o.order_value), 2) as avg_order_value,
    ROUND(SUM(o.order_value) / COUNT(DISTINCT u.user_id), 2) as ltv_90d
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id 
    AND o.status = 'completed'
    AND o.order_date <= DATE_ADD(u.first_order_date, INTERVAL 90 DAY)
WHERE u.first_order_date IS NOT NULL
    AND u.first_order_date >= DATE_SUB(CURDATE(), INTERVAL 120 DAY)
GROUP BY u.acquisition_channel
ORDER BY ltv_90d DESC;
        """, language="sql")
    
    with subtab3:
        st.markdown("#### Retenção por Cohort Mensal")
        st.code("""
-- Análise de retenção por cohort mensal
SELECT 
    cohort_month,
    COUNT(*) as cohort_size,
    ROUND(AVG(m0_revenue), 2) as avg_m0_revenue,
    ROUND(AVG(m1_revenue), 2) as avg_m1_revenue,
    ROUND(AVG(m2_revenue), 2) as avg_m2_revenue,
    ROUND(AVG(m3_revenue), 2) as avg_m3_revenue,
    ROUND(SUM(CASE WHEN m1_revenue > 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as retention_m1,
    ROUND(SUM(CASE WHEN m2_revenue > 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as retention_m2,
    ROUND(SUM(CASE WHEN m3_revenue > 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as retention_m3
FROM user_cohorts
GROUP BY cohort_month
ORDER BY cohort_month DESC
LIMIT 12;
        """, language="sql")

with tab4:
    st.markdown("### 🎯 Orientações para o Case")
    
    # Box de destaque com a missão
    st.markdown("""
    <div class="challenge-box">
        🎯 MISSÃO PRINCIPAL<br>
        Desenvolver estratégia para aumentar LTV/CARC em 30%<br>
        (de 2.33x para 3.03x) em 3 meses
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🔍 Contexto do Desafio")
        st.markdown("""
        - **Prazo:** 3 meses para implementação completa
        - **Meta:** LTV/CARC de 3.03x (aumento de 30%)
        - **Restrição:** Budget de mídia paga não pode aumentar mais de 10%
        - **Foco:** Eficiência e otimização, não crescimento de volume
        """)
        
        st.markdown("#### 📋 Abordagem Sugerida")
        st.markdown("""
        1. **Explorar e entender os dados**
           - Validar qualidade dos dados
           - Identificar padrões e tendências
        
        2. **Identificar problemas e oportunidades**
           - Diagnosticar causas da queda do LTV/CARC
           - Mapear pontos de melhoria
        
        3. **Desenvolver hipóteses testáveis**
           - Formular hipóteses baseadas em dados
           - Priorizar por impacto potencial
        
        4. **Propor soluções baseadas em dados**
           - Estratégias acionáveis e mensuráveis
           - Roadmap de implementação
        
        5. **Quantificar impacto esperado**
           - Projeções de resultados
           - Métricas de acompanhamento
        """)
    
    with col2:
        st.markdown("#### ✅ O que Esperamos")
        st.markdown("""
        **Profundidade Analítica:**
        - Análise exploratória completa
        - Uso adequado de técnicas estatísticas
        - Insights baseados em evidências
        
        **Pensamento Estratégico:**
        - Visão holística do problema
        - Priorização por impacto
        - Consideração de trade-offs
        
        **Foco em Métricas de Negócio:**
        - Conexão clara entre ações e resultados
        - KPIs relevantes para o objetivo
        - ROI das iniciativas propostas
        
        **Recomendações Acionáveis:**
        - Soluções práticas e implementáveis
        - Timeline realista
        - Recursos necessários
        
        **Clareza na Comunicação:**
        - Narrativa lógica e estruturada
        - Visualizações efetivas
        - Conclusões objetivas
        """)

# Footer
st.markdown("---")
st.markdown("""
<footer>
    <p>Case desenvolvido para avaliar habilidades de Growth Analytics | Bluma © 2024</p>
    <p>Em caso de dúvidas técnicas, entre em contato com o time de recrutamento</p>
</footer>
""", unsafe_allow_html=True)
