# Análise de Retenção de Hóspedes

Análise exploratória do comportamento de retorno de hóspedes de um hotel resort, com foco em construção de indicadores de retenção e recorrência para suporte à tomada de decisão em CRM.

---

## Objetivo

Entender quantos hóspedes retornam, com que frequência e como a retenção evolui ao longo do tempo — transformando dados brutos de check-in em métricas acionáveis para estratégias de relacionamento.

---

##  Estrutura do Projeto

```
Retencao_HN/
├── data/
│   └── hospedes_anonimizado.csv   # Base de check-ins (dados anonimizados, LGPD)
├── exports/
│   ├── grafico_retencao_por_ano.png
│   ├── grafico_distribuicao_visitas.png
│   └── grafico_evolucao_mensal.png
└── Notebooks/
    └── analise_retencao_final.ipynb
```

---

##  O que foi feito

**Limpeza e padronização**
- Normalização de emails (chave de identificação do hóspede)
- Conversão e validação de datas de check-in
- Remoção de registros sem data (10 linhas)

**Indicadores construídos**
- Taxa de retenção geral da base
- Taxa de retenção por ano
- Taxa de retenção — janela de 12 meses
- Distribuição de hóspedes por faixa de frequência de visitas
- Evolução mensal de check-ins

---

## Principais Resultados

| Indicador | Valor |
|---|---|
| Total de registros analisados | 29.989 |
| Hóspedes únicos identificados | 10.128 |
| Taxa de retenção geral | 6,2% |
| Taxa de retenção (últimos 12 meses) | 65,8% |
| Hóspedes recorrentes | 626 |

**Achados principais:**
- ~94% dos hóspedes realizou apenas uma visita — padrão esperado para resorts
- A taxa de retenção nos últimos 12 meses (65,8%) é expressivamente maior que a geral, indicando crescimento recente na fidelização
- Hóspedes recorrentes representam base estratégica para ações de CRM e programas de relacionamento

---

## Ferramentas

- Python 3.12
- Pandas
- NumPy
- Matplotlib

---

## Privacidade dos Dados

Os dados originais contêm informações pessoais de hóspedes reais e não foram publicados neste repositório. A base disponível (`hospedes_anonimizado.csv`) foi gerada com nomes e emails fictícios, mantendo a estrutura e as datas originais para fins de análise.

---

## 👩‍💻 Autora

**Talita Lima das Mercês**  
[LinkedIn](https://www.linkedin.com/in/talita-merces-a75b9b103)