"""
Script para extrair o histórico da conta 12.311.03.03 dos Relatórios de 
Movimentação de Bens do Campus Itaberaba para posterior análise.
"""

from tabula import read_pdf
import pandas as pd


COL_CONTAS = 0
COL_SALDO_ANTERIOR = 2
COL_ENTRADA = 3
COL_SAIDA = 4
COL_SALDO_ATUAL = 5
MOBILIARIO_EM_GERAL = 5

dfs = read_pdf("rmb_atual.pdf", pages=2, encoding="latin-1")
cols_idx_list = dfs[0].columns.tolist()
tb = dfs[0]

conta = tb[cols_idx_list[COL_CONTAS]][MOBILIARIO_EM_GERAL]
saldo_anterior = tb[cols_idx_list[COL_SALDO_ANTERIOR]][MOBILIARIO_EM_GERAL]
entrada = tb[cols_idx_list[COL_ENTRADA]][MOBILIARIO_EM_GERAL]
saida = tb[cols_idx_list[COL_SAIDA]][MOBILIARIO_EM_GERAL]
saldo_atual = tb[cols_idx_list[COL_SALDO_ATUAL]][MOBILIARIO_EM_GERAL]

df2 = pd.DataFrame(
    {
        "Conta": [conta],
        "Saldo anterior": [saldo_anterior],
        "Entrada": [entrada],
        "Saida": [saida],
        "Saldo Atual": [saldo_atual],
    }
)
print(df2)
