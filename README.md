<p>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-green.svg"></a>
  <img alt="Python 3.10+" src="https://img.shields.io/badge/Python-3.10%2B-blue.svg">
  <img alt="Pandas 2.x" src="https://img.shields.io/badge/Pandas-2.x-006d5b.svg">
</p>


# df-trabalhos — Tradução e normalização de salários (PT-BR)

Pipeline em **Python + Pandas** que lê o `salaries.csv` original, traduz colunas/categorias para PT-BR e exporta `salaries_pt.csv` pronto para **Power BI**.

## Dados
- `salaries.csv` — arquivo original (fonte GitHub: [Clique aqui](https://raw.githubusercontent.com/FelipeBNogueira/df-trabalhos/main/salaries.csv))

## Como executar
```bash
python script.py
# saída: salaries_pt.csv

Decisões de modelagem (resumo)
• Base de análise: salario_usd; BRL apenas para exibição (opcional salario_brl).
• Traduções via dicionários; valores não mapeados são preservados.
• Categorias ordenadas: nível (Jr→Pl→Sr→Dir), modalidade (Pres→Híb→Rem), porte (P→M→G).
```
Esquema (antes → depois)
| Original             | PT-BR                    | Tipo/Notas                   |
| -------------------- | ------------------------ | ---------------------------- |
| `work_year`          | `ano`                    | `inteiro`                      |
| `experience_level`   | `nivel_experiencia`      | `Jr/Pl/Sr/Dir`                 |
| `employment_type`    | `tipo_contrato`          | `FT/PT/CT/FL → traduzido`      |
| `job_title`          | `cargo`                  | `traduzido quando possível`    |
| `salary`             | `salario`                | `numérico`                     |
| `salary_currency`    | `moeda`                  | `símbolo/código`               |
| `salary_in_usd`      | `salario_usd`            | `referência de comparação`     |
| `employee_residence` | `residencia_funcionario` | `país em PT-BR`                |
| `remote_ratio`       | `Modalidade`             | `Presencial/Híbrido/Remoto`    |
| `company_location`   | `local_empresa`          | `país em PT-BR`                |
| `company_size`       | `porte_empresa`          | `Pequena/Média/Grande`         |


## Ideias de Análises
```
• Ranking salarial por cargo × senioridade (mediana; p25–p75)
• Prêmio remoto vs presencial por cargo/país
• Benchmark por país (mediana + contagem)
• Efeito do porte (S/M/L) por cargo
• Tendência YoY por área (Dados/ML/BI/Eng.)
• Bandas P10–P25–P50–P75–P90 e % fora da banda
```
## Licença
Este projeto está licenciado sob a **MIT License** — veja o arquivo [LICENSE](LICENSE).

## Contato
[<img src="https://cdn.simpleicons.org/instagram/E4405F" alt="Instagram" width="28" height="28">](https://www.instagram.com/felipebnogueira/)
&nbsp;
[<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/128px-LinkedIn_logo_initials.png" alt="LinkedIn" width="28" height="28">](https://www.linkedin.com/in/cfbn-adm/)

Felipe Nogueira — [Clique aqui para acessar o meu site](https://potionsolutions.com)




