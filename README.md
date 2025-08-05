# df-trabalhos — Tradução e normalização de salários (PT-BR)

Pipeline em **Python + Pandas** que lê o `salaries.csv` original, traduz colunas/categorias para PT-BR e exporta `salaries_pt.csv` pronto para **Power BI**.

## Como executar
```bash
python script.py
# saída: salaries_pt.csv

Decisões de modelagem (resumo)
• Base de análise: salario_usd; BRL apenas para exibição.
• Traduções via dicionários; valores não mapeados são preservados.
• Categorias ordenadas: nível (Jr→Pl→Sr→Dir), modalidade (Pres→Híb→Rem), porte (P→M→G).

Estrutura esperada
• salaries.csv — arquivo original (fonte GitHub: https://raw.githubusercontent.com/FelipeBNogueira/df-trabalhos/refs/heads/main/salaries.csv)
• script.py — transformação e tradução
• salaries_pt.csv — saída final (UTF-8-SIG)

Ideias de análise
• Ranking salarial por cargo × senioridade (mediana, p25–p75)
• Prêmio remoto vs presencial por cargo/país
• Benchmark por país (mediana + contagem)
• Bandas por cargo/nível: P10–P25–P50–P75–P90 + % fora da banda (under/overpay).
• Gap de progressão: diferença % Sênior vs Pleno (por cargo e país).
• Prêmio remoto detalhado: Remoto x Presencial por cargo × país × nível.
• Heatmap cargo × país: mediana USD pra achar “onde contratar”.
• Efeito do porte: diferença % entre Grande vs Média vs Pequena por cargo.
• Tipo de contrato: FT vs CT vs FL — prêmio/penalidade e dispersão.
• Tendência YoY: inflação salarial por área (Dados, ML, BI, Eng. Soft).
• Cargos quentes: scatter mediana vs contagem (tamanho = IQR/CV).
• Risco/volatilidade: IQR e coeficiente de variação por cargo/país.
• Mix de senioridade: distribuição Jr/Pl/Sr/Dir por cargo (onde faltam Sêniores).
• Probabilidade de faixa: % de registros > US$X por cargo/país (thresholds).
• Mapa de oportunidades: países mediana baixa + muita oferta (otimizar custo).
• Simulador de squad: custo anual de time (ex.: 1 PM, 2 Eng. Dados, 1 DS, 1 DA) por país.
• Pareto de funções: top 20% cargos cobrem 80% dos registros?
• Qualidade de dados: títulos anômalos (ex.: “Data Analist”), países não mapeados, moedas raras.
• Bandas recomendadas por país: bandas por cargo ajustadas ao país (P50 ± IQR).
• Outliers fortes: top/bottom 1% por cargo (auditar possíveis erros).
• Elasticidade por modalidade: quanto muda a mediana ao trocar Presencial→Remoto.
• Clusters de remuneração: agrupar cargos por perfil salarial (baixa/média/alta).
• Storytelling executivo: KPIs (mediana global, top 5 cargos, prêmio remoto, país mais caro/barato).
