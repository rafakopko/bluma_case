# README - Popular Banco de Dados bluma_case

## 📋 Visão Geral

Este documento fornece instruções detalhadas para criar um script Python que popula o banco de dados `bluma_case` com dados fictícios realistas para um case de Analista de Growth com foco em Mídia Paga.

## 🎯 Objetivo

Gerar dados sintéticos que simulem um marketplace de beleza e bem-estar (similar à Bluma) com:
- 50.000 usuários
- ~150.000 pedidos
- 120 campanhas de mídia paga
- Performance diária de campanhas
- Criativos e suas métricas
- Eventos de usuários
- Análise de cohorts

## 🗄️ Estrutura do Banco de Dados

### Tabelas a Popular

1. **users**
   - `user_id`: UUID único
   - `created_at`: Timestamp de criação
   - `acquisition_channel`: Canal de aquisição (Meta Ads, Google Ads, TikTok Ads, Organic, Referral)
   - `acquisition_campaign`: Campanha específica
   - `first_order_date`: Data do primeiro pedido (pode ser NULL)
   - `city`: Cidade do usuário
   - `state`: Estado (sigla)
   - `age_group`: Faixa etária
   - `gender`: Gênero

2. **orders**
   - `order_id`: UUID único
   - `user_id`: FK para users
   - `order_date`: Data do pedido
   - `order_value`: Valor do pedido
   - `service_type`: Tipo de serviço
   - `status`: Status (completed/cancelled)
   - `payment_method`: Método de pagamento
   - `discount_amount`: Valor do desconto

3. **paid_media_campaigns**
   - `campaign_id`: ID único da campanha
   - `platform`: Plataforma (Meta, Google, TikTok)
   - `campaign_name`: Nome descritivo
   - `campaign_type`: Tipo (Prospecting, Retargeting, etc.)
   - `start_date`: Data de início
   - `end_date`: Data de fim
   - `daily_budget`: Budget diário
   - `objective`: Objetivo da campanha

4. **daily_performance**
   - `date`: Data
   - `campaign_id`: FK para campaigns
   - `impressions`: Impressões
   - `clicks`: Cliques
   - `spend`: Gasto
   - `conversions`: Conversões
   - `conversion_value`: Valor das conversões
   - `new_users`: Novos usuários
   - `cpm`: Custo por mil impressões
   - `cpc`: Custo por clique
   - `ctr`: Taxa de clique

5. **ad_creatives**
   - `creative_id`: ID único
   - `campaign_id`: FK para campaigns
   - `creative_type`: Tipo (UGC, Carousel, Video, etc.)
   - `creative_name`: Nome do criativo
   - `launched_date`: Data de lançamento
   - `status`: Status (active/paused)

6. **creative_performance**
   - `date`: Data
   - `creative_id`: FK para creatives
   - `impressions`: Impressões
   - `clicks`: Cliques
   - `spend`: Gasto
   - `conversions`: Conversões
   - `engagement_rate`: Taxa de engajamento

7. **user_events**
   - `event_id`: UUID único
   - `user_id`: FK para users
   - `event_timestamp`: Timestamp do evento
   - `event_type`: Tipo de evento
   - `platform`: Plataforma (iOS/Android/Web)
   - `session_id`: ID da sessão

8. **user_cohorts**
   - `cohort_month`: Mês do cohort
   - `user_id`: FK para users
   - `m0_revenue`: Receita mês 0
   - `m1_revenue`: Receita mês 1
   - `m2_revenue`: Receita mês 2
   - `m3_revenue`: Receita mês 3
   - `m0_orders`: Pedidos mês 0
   - `m1_orders`: Pedidos mês 1
   - `m2_orders`: Pedidos mês 2
   - `m3_orders`: Pedidos mês 3

9. **budget_allocation**
   - `month`: Mês
   - `channel`: Canal
   - `planned_budget`: Budget planejado
   - `actual_spend`: Gasto real
   - `target_cac`: CAC objetivo
   - `actual_cac`: CAC real

## 📊 Parâmetros de Negócio

### Canais de Aquisição
```
Meta Ads: 45% do volume, CAC base R$85, taxa ativação 7.8%
Google Ads: 25% do volume, CAC base R$95, taxa ativação 9.2%
TikTok Ads: 10% do volume, CAC base R$75, taxa ativação 6.5%
Organic: 15% do volume, CAC base R$0, taxa ativação 15%
Referral: 5% do volume, CAC base R$30, taxa ativação 25%
```

### Serviços Oferecidos
```
Manicure: 35% dos pedidos, ticket médio R$65, frequência 2.5x/mês
Massagem: 20% dos pedidos, ticket médio R$120, frequência 1.2x/mês
Limpeza de Pele: 15% dos pedidos, ticket médio R$95, frequência 1.5x/mês
Design Sobrancelhas: 15% dos pedidos, ticket médio R$55, frequência 2.0x/mês
Depilação: 15% dos pedidos, ticket médio R$80, frequência 1.8x/mês
```

### Cidades de Operação
```
São Paulo: 30%
Rio de Janeiro: 20%
Belo Horizonte: 10%
Brasília: 8%
Curitiba: 7%
Porto Alegre: 5%
Salvador: 5%
Fortaleza: 5%
Recife: 5%
Campinas: 5%
```

### Tipos de Criativos
```
UGC: CTR 2.8%, CVR 1.2%
Carousel: CTR 1.9%, CVR 1.0%
Video: CTR 2.2%, CVR 1.1%
Static: CTR 1.5%, CVR 0.8%
ASMR: CTR 3.1%, CVR 0.9%
```

## 🔧 Requisitos Técnicos

### Bibliotecas Python Necessárias
- pandas
- numpy
- faker (usar Faker('pt_BR'))
- mysql-connector-python
- datetime
- random
- uuid

### Configuração de Conexão
```python
DB_CONFIG = {
    'host': '95.111.240.159',
    'database': 'bluma_case',
    'user': 'root',
    'password': 'rafa906996'
}
```

## 📝 Instruções de Implementação

### 1. Estrutura Geral do Script

O script deve ter as seguintes funções principais:

#### a) `create_connection()`
- Estabelecer conexão com MySQL
- Validar conexão
- Retornar objeto de conexão

#### b) `truncate_tables(connection)`
- Limpar todas as tabelas antes de popular
- Desabilitar foreign keys temporariamente
- Re-habilitar foreign keys após limpeza

#### c) `batch_insert(connection, table_name, data, batch_size=1000)`
- Inserir dados em lotes para performance
- Tratar conversão de tipos (datetime, NULL values)
- Commit a cada batch
- Mostrar progresso

### 2. Funções de Geração de Dados

#### a) `generate_users()`
**Lógica:**
- Distribuir criação de usuários ao longo do período (beta distribution)
- Mais usuários em meses recentes (simular crescimento)
- Atribuir canal de aquisição com pesos definidos
- Calcular first_order_date baseado na taxa de ativação do canal
- Demografia: 85% feminino, faixa 25-34 anos predominante

**Detalhes importantes:**
- Gerar 50.000 usuários
- Período: Janeiro 2024 a Janeiro 2025
- Tempo médio até primeira compra: 4 dias (gamma distribution)
- Ajuste sazonal: +30% ativação em maio, novembro e dezembro

#### b) `generate_orders(users)`
**Lógica:**
- Apenas usuários com first_order_date geram pedidos
- Distribuição de pedidos por usuário:
  - 30%: apenas 1 pedido
  - 30%: 2-3 pedidos
  - 25%: 4-7 pedidos
  - 15%: 8+ pedidos (power users)
- Tendência a repetir o mesmo serviço (60% de chance)
- Taxa de cancelamento: 12% novos usuários, 8% recorrentes

**Detalhes importantes:**
- Desconto primeiro pedido: 40% chance, 15-25% desconto
- Pagamento: Pix crescendo (25% em 2024 → 35% em 2025)
- Intervalo entre pedidos baseado na frequência do serviço

#### c) `generate_campaigns()`
**Lógica:**
- 120 campanhas total
- Distribuição por plataforma: Meta 50%, Google 35%, TikTok 15%
- Tipos de campanha por plataforma:
  - Meta: Prospecting, Retargeting, Lookalike, Brand
  - Google: Search, Shopping, PMax, Brand
  - TikTok: Prospecting, Retargeting, Brand
- Duração: 7 a 90 dias
- Budget diário varia por tipo de campanha

#### d) `generate_daily_performance(campaigns)`
**Lógica:**
- Para cada dia de cada campanha ativa
- Learning phase: performance melhora nos primeiros 7 dias
- Fatores de ajuste:
  - Dia da semana: -20% fins de semana, +15% sextas
  - Sazonal: +50% dia das mães, +80% black friday
  - Variação diária: ±20% no spend
- Cálculo de métricas em cascata: spend → impressions → clicks → conversions

**Fórmulas:**
- Impressions = (Spend / CPM) * 1000
- Clicks = Impressions * CTR
- Conversions = Clicks * CVR
- New Users = Conversions * 0.7 (média)

#### e) `generate_creatives(campaigns)`
**Lógica:**
- 3-10 criativos por campanha
- Distribuição de tipos com pesos definidos
- 20% dos criativos são pausados após teste
- Criativos lançados em ondas (não todos no dia 1)

#### f) `generate_creative_performance(creatives, daily_performance)`
**Lógica:**
- Distribuir performance da campanha entre criativos ativos
- Cada criativo tem quality score (0.7 a 1.3)
- Performance proporcional ao tipo de criativo
- Criativos pausados param de gerar dados após 7 dias

#### g) `generate_events(users, orders)`
**Lógica:**
- Sample de 10.000 usuários ativos
- 3-20 eventos por sessão
- Tipos de eventos e probabilidades:
  - app_open: 30%
  - view_service: 25%
  - view_professional: 15%
  - add_to_cart: 12%
  - search: 10%
  - start_checkout: 5%
  - complete_order: 3%
- Plataformas: iOS 45%, Android 40%, Web 15%

#### h) `generate_cohorts(users, orders)`
**Lógica:**
- Agrupar usuários por mês de primeira compra
- Calcular receita e pedidos para M0, M1, M2, M3
- Apenas usuários ativados entram nos cohorts
- Considerar apenas pedidos completed

#### i) `generate_budget_allocation(campaigns, daily_performance)`
**Lógica:**
- Agregar spend mensal por canal
- Budget planejado = spend real * 1.1-1.3
- Calcular CAC real vs target
- Target CAC baseado nos parâmetros de canal

### 3. Padrões de Dados Realistas

#### Crescimento Temporal
- Use beta distribution (2, 5) para simular crescimento
- Mais dados nos meses recentes

#### Sazonalidade
- Maio (dia das mães): +50% performance
- Black Friday (nov 20+): +80% performance  
- Dezembro (até 25): +40% performance
- Fins de semana: -20% performance

#### Learning Phase
- Campanhas melhoram performance nos primeiros 7 dias
- Use fator multiplicativo crescente de 0.7 a 1.0

#### Variações Realistas
- Todos os valores devem ter ruído gaussiano
- CPM: ±10%
- CTR: ±20%
- CVR: ±30%
- Order Value: ±15%

### 4. Validações e Constraints

- user_id deve ser UUID v4
- Datas não podem ser futuras
- first_order_date >= created_at
- order_date >= first_order_date
- campaign end_date >= start_date
- Valores monetários com 2 casas decimais
- Percentuais entre 0 e 100
- IDs de campanha no formato: Platform_Type_Number

### 5. Performance e Otimização

- Use batch insert (1000 registros por vez)
- Desabilite foreign keys durante inserção
- Mostre progresso a cada batch
- Commit após cada tabela completa
- Tempo estimado de execução: 5-10 minutos

### 6. Output Esperado

Ao final, mostrar resumo:
```
Total de usuários: 50,000
Usuários ativados: 4,200 (8.4%)
Total de pedidos: 152,340
GMV Total: R$ 14,472,300.00
Total de campanhas: 120
Registros de performance: 3,652
```

## 🔍 Verificações Finais

O script deve incluir queries de validação:

1. Taxa de ativação por canal
2. Ticket médio por serviço
3. CAC por plataforma
4. Distribuição temporal dos dados
5. Integridade referencial

## 💡 Dicas Importantes

- Use numpy para distribuições estatísticas
- Faker('pt_BR') para nomes e cidades brasileiras
- Mantenha seed para reproducibilidade (opcional)
- Trate exceções de conexão e inserção
- Log de progresso é essencial para debugging

## 🚀 Execução

1. Configurar credenciais do banco
2. Executar script Python
3. Verificar dados com queries de validação
4. Banco estará pronto para o case

---

**Nota**: Este README serve como especificação completa para implementação do script de população do banco de dados.