"""
Script para extrair tabela Excel do Relatório de Movimentação de Almoxarifado (RMA) gerado pelo SIGA-IF Baiano.
"""

from tabula.io import read_pdf
import pandas as pd
import os

filename = "rma_siga"

filepath = os.path.join(os.getcwd(), filename + ".pdf")
outputpath = os.path.join(os.getcwd(), filename + ".xlsx")

dfs = read_pdf(filename + ".pdf", pages="all", encoding="latin-1")
df = pd.concat(dfs)
df.to_excel(outputpath)
print(df)
