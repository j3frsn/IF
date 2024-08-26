"""
Script para extrair tabela Excel do Relatório de Depreciação Mensal gerado pelo SIGA-IF Baiano.
"""

from tabula import read_pdf, convert_into
import pandas as pd
import os

files = os.listdir(".")
filename = ""

for file in files:
    if file.endswith(".pdf"):
        filename = file.split(".")[0]
        break

filepath = os.path.join(os.getcwd(), filename + ".pdf")
outputpath = os.path.join(os.getcwd(), filename + ".xlsx")


dfs = read_pdf(filename + ".pdf", pages="all", encoding="latin-1")
df = pd.concat(dfs)
df.to_excel(outputpath)
print(df)

# convert_into(filepath, outputpath, output_format="xlsx")

# cols = dfs[0].columns.tolist()

# dict = {}

# for col in cols:
#    rows = dfs[dfs[0].]
#    print(rows)
#    break


# df = pd.DataFrame(dfs, columns=[""])
# df
# cols_idx_list = dfs[0].columns.tolist()
# tb = dfs[0]
