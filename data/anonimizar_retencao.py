"""
anonimizar_retencao.py
-----------------------
Anonimiza o arquivo hospedes.csv para uso público no GitHub.
Substitui nome e email por dados fictícios, mantendo a estrutura
e as datas originais (necessárias para a análise de retenção).

Execute na pasta onde está o hospedes.csv:
    python anonimizar_retencao.py
"""

import pandas as pd
import numpy as np
import random

random.seed(42)
np.random.seed(42)

# ─── DADOS FICTÍCIOS ────────────────────────────────────────────────────────

NOMES = [
    "Ana Silva", "Carlos Souza", "Mariana Costa", "Pedro Oliveira",
    "Fernanda Lima", "Rafael Alves", "Juliana Pereira", "Bruno Santos",
    "Camila Rocha", "Diego Martins", "Larissa Ferreira", "Thiago Carvalho",
    "Priscila Gomes", "Leonardo Ribeiro", "Amanda Nunes", "Gustavo Araujo",
    "Vanessa Mendes", "Rodrigo Teixeira", "Patrícia Moreira", "Henrique Dias",
    "Isabela Cardoso", "Marcelo Barbosa", "Tatiane Monteiro", "Felipe Ramos",
    "Aline Castro", "Eduardo Cunha", "Renata Freitas", "Vinícius Pinto",
    "Luciana Melo", "André Correia", "Débora Lopes", "Fábio Nascimento",
    "Simone Azevedo", "Leandro Vieira", "Cristina Batista", "Marcos Cavalcanti",
    "Natália Campos", "Paulo Figueiredo", "Eliane Duarte", "Roberto Macedo"
]

DOMINIOS = ["gmail.com", "hotmail.com", "yahoo.com.br", "outlook.com", "uol.com.br"]


def gerar_email(nome):
    partes = nome.lower().split()
    variacao = random.randint(0, 2)
    if variacao == 0:
        base = f"{partes[0]}.{partes[-1]}"
    elif variacao == 1:
        base = f"{partes[0]}{random.randint(1, 999)}"
    else:
        base = f"{partes[0][0]}{partes[-1]}"
    return f"{base}@{random.choice(DOMINIOS)}"


# ─── EXECUÇÃO ───────────────────────────────────────────────────────────────

print("=" * 50)
print("  Anonimizando hospedes.csv...")
print("=" * 50)

df = pd.read_csv("hospedes.csv", sep=";", engine="python")
print(f"  {len(df):,} linhas carregadas")
print(f"  Colunas: {df.columns.tolist()}")

n = len(df)

# Gera pool menor de nomes para simular hóspedes recorrentes
pool_nomes = [random.choice(NOMES) for _ in range(n // 3 + 1)]
nomes_col = [random.choice(pool_nomes) for _ in range(n)]

if "Hospede" in df.columns:
    df["Hospede"] = nomes_col

if "Email" in df.columns:
    df["Email"] = [gerar_email(nome) for nome in nomes_col]

if "Reserva" in df.columns:
    base = 400000
    df["Reserva"] = [base + i + random.randint(0, 500) for i in range(n)]

df.to_csv("hospedes_anonimizado.csv", sep=";", index=False, encoding="utf-8-sig")

print(f"\n  ✅ Arquivo gerado: hospedes_anonimizado.csv")
print(f"  ⚠️  Nunca suba o hospedes.csv original no GitHub.")
print("=" * 50)
