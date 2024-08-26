"""
Script para extrair tabela Excel do Relatório de Depreciação Mensal gerado pelo SIGA-IF Baiano.
"""

import pandas as pd
import pdfplumber
import os

files = os.listdir(".")
filename = ""

for file in files:
    if file.endswith(".pdf"):
        filename = file.split(".")[0]
        break

filepath = os.path.join(os.getcwd(), filename + ".pdf")
accounts_dict = {"Conta": [], "Saldo": []}


def filter_list(list):
    filtered_list = []
    for line in list:
        if line.startswith("P "):
            filtered_list.append(line)
    return filtered_list


with pdfplumber.open(filepath) as pdf:
    page1 = pdf.pages[0]
    page2 = pdf.pages[1]
    page1_txt = page1.extract_text()
    page2_txt = page2.extract_text()

    page1_list = page1_txt.split("\n")
    page2_list = page2_txt.split("\n")

    filteded_page1_list = filter_list(page1_list)
    filteded_page2_list = filter_list(page2_list)

    final_list = filteded_page1_list + filteded_page2_list

    for line in final_list:
        split_line = line.split(" ")
        accounts_dict["Conta"].append(split_line[1])
        accounts_dict["Saldo"].append(split_line[2])

print(accounts_dict)

outputpath = os.path.join(os.getcwd(), filename + ".xlsx")

df = pd.DataFrame.from_dict(accounts_dict)
df.to_excel(outputpath)
