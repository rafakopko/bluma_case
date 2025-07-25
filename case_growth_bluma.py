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
    "🎯 Orientações",
    "📋 Contexto do Negócio", 
    "🗄️ Estrutura de Dados", 
    "📊 Queries de Exemplo"
])

with tab1:
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
    
    with col2:
        st.markdown("#### ✅ O que Esperamos")
        st.markdown("""
        **Profundidade Analítica:**
        - Análise dos dados
        - Insights baseados em evidências
        
        **Pensamento Estratégico:**
        - Visão holística do problema
        - Priorização por impacto
        - Consideração de trade-offs
        
        **Foco em Métricas de Negócio:**
        - Conexão clara entre ações e resultados
        - KPIs relevantes para o objetivo
        
        **Recomendações Acionáveis:**
        - Soluções práticas e implementáveis
        - Timeline realista
        - Recursos necessários

        """)

with tab2:
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

with tab3:
    st.markdown("### 🗄️ Estrutura do Banco de Dados")
        
    # Seção de conexão simplificada
    st.markdown("#### � Como Conectar ao Banco")
    
    st.markdown("**📋 Informações de Conexão:**")
    
    conn_info_col1, conn_info_col2 = st.columns([1, 1])
    
    with conn_info_col1:
        st.info("""
        **🏠 Servidor:** 95.111.240.159  
        **🗄️ Banco:** bluma_case  
        **👤 Usuário:** candidato  
        **🔑 Senha:** bluma123  
        **🚪 Porta:** 3306
        """)
    
    with conn_info_col2:
        st.markdown("**� Como usar os dados:**")
        st.markdown("""
        1. **Conecte no banco** usando as credenciais da sidebar
        2. **Explore as tabelas** com SELECT simples
        3. **Analise os relacionamentos** entre usuários e pedidos
        4. **Calcule métricas** como CAC e LTV
        """)
    
    st.markdown("---")
    
    # Fluxo visual dos dados
    st.markdown("#### � Como os Dados se Relacionam")
    
    flow_col1, flow_col2, flow_col3 = st.columns(3)
    
    with flow_col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FF69B4, #FF1493); color: white; padding: 1.5rem; border-radius: 15px; text-align: center; margin: 1rem 0;">
            <h3>📢 1. CAMPANHAS</h3>
            <p><strong>paid_media_campaigns</strong></p>
            <p>120 campanhas ativas<br>Meta, Google, TikTok</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**O que contém:**")
        st.markdown("""
        - Nome das campanhas
        - Plataforma (Meta/Google/TikTok)  
        - Budget diário
        - Período de atividade
        - Tipo de campanha
        """)
    
    with flow_col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FFB6C1, #FF69B4); color: white; padding: 1.5rem; border-radius: 15px; text-align: center; margin: 1rem 0;">
            <h3>👥 2. USUÁRIOS</h3>
            <p><strong>users</strong></p>
            <p>50.000 usuários<br>4.955 ativados (9.9%)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**O que contém:**")
        st.markdown("""
        - Canal de aquisição
        - Data de cadastro
        - Primeira compra
        - Cidade e idade
        - Demografia
        """)
    
    with flow_col3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FFF0F5, #FFB6C1); color: #333; padding: 1.5rem; border-radius: 15px; text-align: center; margin: 1rem 0;">
            <h3>🛒 3. PEDIDOS</h3>
            <p><strong>orders</strong></p>
            <p>19.683 pedidos<br>R$ 1.4M em GMV</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**O que contém:**")
        st.markdown("""
        - Valor do pedido
        - Tipo de serviço
        - Data da compra
        - Status (completo/cancelado)
        - Método de pagamento
        """)
    
    # Setas conectoras
    st.markdown("""
    <div style="text-align: center; margin: 1rem 0;">
        <span style="font-size: 2rem;">📢 → 👥 → 🛒</span><br>
        <strong>Campanhas atraem Usuários que fazem Pedidos</strong>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Performance tracking
    st.markdown("#### � Acompanhamento de Performance")
    
    perf_col1, perf_col2 = st.columns(2)
    
    with perf_col1:
        st.markdown("""
        <div style="background-color: #FFF0F5; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #FF1493;">
            <h4>📈 Performance Diária</h4>
            <p><strong>daily_performance</strong> - 5.837 registros</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**📊 Métricas por dia:**")
        st.markdown("""
        - **Spend:** Quanto gastamos
        - **Impressões:** Quantas pessoas viram os anúncios  
        - **Clicks:** Quantas pessoas clicaram
        - **Conversões:** Quantas pessoas compraram
        - **New Users:** Novos usuários adquiridos
        """)
        
        st.markdown("**💡 Para que serve:**")
        st.markdown("""
        - Calcular **CAC** (custo por usuário)
        - Ver **tendências** ao longo do tempo
        - Identificar **campanhas** com melhor performance
        """)
    
    with perf_col2:
        st.markdown("""
        <div style="background-color: #FFF0F5; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #FF1493;">
            <h4>🎨 Criativos</h4>
            <p><strong>ad_creatives</strong> - 755 criativos</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**🎭 Tipos de criativo:**")
        st.markdown("""
        - **UGC:** Conteúdo de usuários
        - **Carousel:** Várias imagens
        - **Video:** Vídeos promocionais
        - **Static:** Imagem única
        - **ASMR:** Conteúdo relaxante
        """)
        
        st.markdown("**💡 Para que serve:**")
        st.markdown("""
        - Ver quais **formatos** funcionam melhor
        - Identificar **fadiga criativa**
        - Otimizar **mix de criativos**
        """)
    
    st.markdown("---")
    
    # Tabelas auxiliares
    st.markdown("#### 📋 Tabelas Auxiliares")
    
    aux_col1, aux_col2 = st.columns(2)
    
    with aux_col1:
        with st.expander("📱 user_events - Eventos de Interação"):
            st.markdown("""
            **O que é:** Registro de ações dos usuários no app/site
            
            **Principais eventos:**
            - app_open (abrir app)
            - view_service (ver serviço)
            - add_to_cart (adicionar ao carrinho)
            - search (buscar)
            
            **Para que serve:**
            - Analisar funil de conversão
            - Identificar pontos de abandono
            - Otimizar experiência do usuário
            
            **💡 Dica:** Útil para entender comportamento antes da compra
            """)
        
        with st.expander("� budget_allocation - Planejamento"):
            st.markdown("""
            **O que é:** Budget planejado vs real por mês e canal
            
            **Informações:**
            - Budget planejado mensal
            - Gasto real
            - CAC objetivo vs real
            
            **Para que serve:**
            - Controle orçamentário
            - Identificar desvios
            - Planejar próximos meses
            
            **💡 Dica:** Compare planned vs actual para ver eficiência
            """)
    
    with aux_col2:
        with st.expander("👥 user_cohorts - Análise de Retenção"):
            st.markdown("""
            **O que é:** Receita dos usuários agrupados por mês de aquisição
            
            **Dados por usuário:**
            - M0: Receita no mês da aquisição
            - M1: Receita no mês seguinte  
            - M2: Receita no 2º mês
            - M3: Receita no 3º mês
            
            **Para que serve:**
            - Calcular LTV por período
            - Analisar retenção
            - Projetar receita futura
            
            **💡 Dica:** Dados já calculados, pronto para usar!
            """)
        
        with st.expander("� creative_performance - Performance de Criativos"):
            st.markdown("""
            **O que é:** Performance detalhada de cada criativo
            
            **Métricas por criativo:**
            - Impressões e clicks
            - Spend alocado
            - Conversões atribuídas
            - Taxa de engajamento
            
            **Para que serve:**
            - Identificar melhores criativos
            - Analisar fadiga criativa
            - Otimizar budget entre criativos
            
            **💡 Dica:** Compare performance por tipo de criativo
            """)
    
        
    st.markdown("---")
    
    # Call to action final
    st.markdown("""
    <div style="background: linear-gradient(135deg, #FF69B4, #FF1493); color: white; padding: 2rem; border-radius: 15px; text-align: center; margin: 2rem 0;">
        <h3>🎯 Objetivo do Case</h3>
        <p style="font-size: 1.2rem; margin: 1rem 0;">
            <strong>Aumentar LTV/CAC de 2.33x para 3.03x (+30%) em 3 meses</strong>
        </p>
        <p>Use estes dados para identificar oportunidades e propor estratégias de otimização!</p>
        <p style="margin-top: 1rem;">
            🔗 <strong>Credenciais na sidebar</strong> | 📊 <strong>Queries de exemplo na próxima aba</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)
with tab4:
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

# Footer
st.markdown("---")
st.markdown("""
<footer>
    <p>Case desenvolvido para avaliar habilidades de Growth Analytics | Bluma © 2024</p>
    <p>Em caso de dúvidas técnicas, entre em contato com o time de recrutamento</p>
</footer>
""", unsafe_allow_html=True)
