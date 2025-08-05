#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
df-trabalhos — Tradução e normalização do dataset de salários (PT-BR)

- Lê o salaries.csv (local) ou baixa do raw do GitHub se não existir
- Renomeia colunas
- Traduz categorias (nível, contrato, modalidade, porte, país, cargo)
- (Opcional) cria salario_brl a partir de salario_usd
- Exporta salaries_pt.csv (UTF-8-SIG)
"""

import os
import pandas as pd

# -----------------------------
# Config
# -----------------------------
RAW_URL = "https://raw.githubusercontent.com/FelipeBNogueira/df-trabalhos/main/salaries.csv"
OUTPUT = "salaries_pt.csv"
USD_BRL = None  # defina ex.: 5.50 para criar salario_brl

# -----------------------------
# Dicionários (resumo)
# -----------------------------
RENAME = {
    "work_year": "ano",
    "experience_level": "nivel_experiencia",
    "employment_type": "tipo_contrato",
    "job_title": "cargo",
    "salary": "salario",
    "salary_currency": "moeda",
    "salary_in_usd": "salario_usd",
    "employee_residence": "residencia_funcionario",
    "remote_ratio": "Modalidade",
    "company_location": "local_empresa",
    "company_size": "porte_empresa",
}

exp_map   = {"EN": "Júnior", "MI": "Pleno", "SE": "Sênior", "EX": "Diretoria"}
emp_map   = {"FT": "Tempo integral", "PT": "Meio período", "CT": "Contrato", "FL": "Freelancer"}
remote_map= {0: "Presencial", 50: "Híbrido", 100: "Remoto"}
size_map  = {"S": "Pequena", "M": "Média", "L": "Grande"}

currency_map = {"USD":"US$","EUR":"€","GBP":"£","BRL":"R$","CAD":"C$","AUD":"A$","MXN":"MXN","PHP":"PHP",
                "PLN":"PLN","JPY":"JPY","INR":"INR","SGD":"SGD","HUF":"HUF","CHF":"CHF","TWD":"TWD","NOK":"NOK",
                "CZK":"CZK","ZAR":"ZAR","DKK":"DKK","ILS":"ILS","TRY":"TRY","SEK":"SEK","NZD":"NZD","HKD":"HKD","THB":"THB","CLP":"CLP"}

country_map = {
    # América
    "US":"EUA","CA":"Canadá","BR":"Brasil","MX":"México","AR":"Argentina","CL":"Chile","CO":"Colômbia","PE":"Peru","UY":"Uruguai","PY":"Paraguai",
    "BO":"Bolívia","EC":"Equador","VE":"Venezuela","CR":"Costa Rica","PA":"Panamá","DO":"República Dominicana","PR":"Porto Rico","AS":"Samoa Americana",
    "JM":"Jamaica","SV":"El Salvador","HN":"Honduras","BM":"Bermudas",
    # Europa
    "GB":"Reino Unido","IE":"Irlanda","PT":"Portugal","ES":"Espanha","FR":"França","DE":"Alemanha","NL":"Países Baixos","BE":"Bélgica","CH":"Suíça","AT":"Áustria",
    "IT":"Itália","PL":"Polônia","CZ":"Tchéquia","SK":"Eslováquia","HU":"Hungria","RO":"Romênia","BG":"Bulgária","GR":"Grécia","SE":"Suécia","NO":"Noruega",
    "DK":"Dinamarca","FI":"Finlândia","EE":"Estônia","LV":"Letônia","LT":"Lituânia","UA":"Ucrânia","RU":"Rússia","SI":"Eslovênia","HR":"Croácia","RS":"Sérvia",
    "JE":"Jersey","MT":"Malta","MK":"Macedônia do Norte","LU":"Luxemburgo","AD":"Andorra","MD":"Moldávia","BA":"Bósnia e Herzegovina","XK":"Kosovo",
    "CY":"Chipre","TR":"Turquia","GE":"Geórgia",
    # Ásia e Oceania
    "IN":"Índia","CN":"China","JP":"Japão","SG":"Singapura","HK":"Hong Kong","TW":"Taiwan","KR":"Coreia do Sul","TH":"Tailândia","PH":"Filipinas","MY":"Malásia",
    "ID":"Indonésia","VN":"Vietnã","PK":"Paquistão","BD":"Bangladesh","AE":"Emirados Árabes Unidos","QA":"Catar","KW":"Kuwait","SA":"Arábia Saudita","OM":"Omã",
    "BH":"Bahrein","IL":"Israel","IQ":"Iraque","IR":"Irã","JO":"Jordânia","LB":"Líbano","AM":"Armênia","UZ":"Uzbequistão","AU":"Austrália","NZ":"Nova Zelândia",
    # África
    "ZA":"África do Sul","EG":"Egito","MA":"Marrocos","TN":"Tunísia","DZ":"Argélia","NG":"Nigéria","KE":"Quênia","LS":"Lesoto",
    "CD":"República Democrática do Congo","ZM":"Zâmbia","RW":"Ruanda","UG":"Uganda","MU":"Maurício","GH":"Gana","CF":"República Centro-Africana",
}

# Apenas exemplos — cole seu JOB_MAP completo abaixo se quiser
job_map = {
    "Solutions Engineer": "Engenheiro de Soluções",
    "Data Engineer": "Engenheiro de Dados",
    "Data Scientist": "Cientista de Dados",
    "Data Analyst": "Analista de Dados",
    "Machine Learning Engineer": "Engenheiro de Machine Learning",
    # ... (adicione o restante do seu job_map aqui)
}

CATEGORY_ORDERS = {
    "nivel_experiencia": ["Júnior", "Pleno", "Sênior", "Diretoria"],
    "Modalidade": ["Presencial", "Híbrido", "Remoto"],
    "porte_empresa": ["Pequena", "Média", "Grande"],
}

# -----------------------------
# Funções
# -----------------------------
def load_data() -> pd.DataFrame:
    """Lê salaries.csv local; se não existir, baixa do RAW do GitHub."""
    if os.path.exists("salaries.csv"):
        return pd.read_csv("salaries.csv")
    df = pd.read_csv(RAW_URL)
    df.to_csv("salaries.csv", index=False)  # cache local
    return df

def apply_maps(df: pd.DataFrame) -> pd.DataFrame:
    """Aplica renome e traduções. Mantém original quando não houver mapeamento."""
    df = df.rename(columns=RENAME).copy()

    # limpeza leve
    for col in ["residencia_funcionario", "local_empresa", "moeda", "cargo"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()

    # mapas simples
    if "nivel_experiencia" in df: df["nivel_experiencia"] = df["nivel_experiencia"].replace(exp_map)
    if "tipo_contrato" in df:     df["tipo_contrato"]     = df["tipo_contrato"].replace(emp_map)
    if "porte_empresa" in df:     df["porte_empresa"]     = df["porte_empresa"].replace(size_map)
    if "moeda" in df:             df["moeda"]             = df["moeda"].replace(currency_map)

    # modalidade: garantir numérico 0/50/100
    if "Modalidade" in df:
        df["Modalidade"] = pd.to_numeric(df["Modalidade"], errors="ignore").replace(remote_map)

    # países (mapear somente códigos; se já estiver PT-BR, mantém)
    for col in ["residencia_funcionario", "local_empresa"]:
        if col in df:
            mapped = df[col].str.upper().replace(country_map)
            df[col] = mapped

    # cargos (grande — manter replace)
    if "cargo" in df:
        df["cargo"] = df["cargo"].replace(job_map)

    # setar ordem categórica
    for col, order in CATEGORY_ORDERS.items():
        if col in df.columns:
            df[col] = pd.Categorical(df[col], categories=order, ordered=True)

    # tipos
    for col in ["ano", "salario", "salario_usd"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

def add_brl(df: pd.DataFrame, usd_brl: float | None) -> pd.DataFrame:
    """Cria salario_brl se a taxa for informada."""
    if usd_brl and "salario_usd" in df:
        df["salario_brl"] = (df["salario_usd"] * float(usd_brl)).round(0)
    return df

def report_unmapped(df: pd.DataFrame):
    """Mostra valores possivelmente não mapeados (país/cargo)."""
    def missing(series, mapping):
        s = series.dropna().astype(str).str.strip()
        return sorted(set(s.unique()) - set(mapping.keys()) - set(mapping.values()))
    if "residencia_funcionario" in df: print("País (resid.):", missing(df["residencia_funcionario"], country_map)[:20])
    if "local_empresa" in df:          print("País (empresa):", missing(df["local_empresa"], country_map)[:20])
    if "cargo" in df:
        cargos = df["cargo"].dropna().unique()
        not_done = sorted(set(cargos) - set(job_map.keys()) - set(job_map.values()))
        print("Cargos possivelmente não mapeados:", not_done[:20])

# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    df = load_data()
    df = apply_maps(df)
    df = add_brl(df, USD_BRL)  # defina USD_BRL acima se quiser BRL
    report_unmapped(df)        # opcional
    df.to_csv(OUTPUT, index=False, encoding="utf-8-sig")
    print(f"{OUTPUT} gerado ✅")
