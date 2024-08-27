"""
Script para extrair tabela Excel do RAZAO da conta 123810100 - Depreciação acumulada de bens móveis 
do SIAFI, reorganizando a disposição das contas e respectivos saldos de acordo com o Relatório de 
Depreciação mensal gerado pelo SIGA.
"""

import os
from tabula.io import read_pdf
import pandas as pd
import pdfplumber

FILENAME = "depre_siafi"
FILEPATH = os.path.join(os.getcwd(), FILENAME + ".pdf")
OUTPUT_FILE_PATH = os.path.join(os.getcwd(), FILENAME + ".xlsx")


def _filter_list(list_to_filter):
    filtered_list = []

    for line in list_to_filter:
        if line.startswith("P "):
            filtered_list.append(line)
    return filtered_list


def _extract_siafi_accts():
    accts_dict = {"Conta": [], "Saldo": []}
    with pdfplumber.open(FILEPATH) as pdf:
        page1 = pdf.pages[0]
        page2 = pdf.pages[1]

        page1_txt = page1.extract_text()
        page2_txt = page2.extract_text()

        page1_list = page1_txt.split("\n")
        page2_list = page2_txt.split("\n")

        filteded_page1_list = _filter_list(page1_list)
        filteded_page2_list = _filter_list(page2_list)
        final_list = filteded_page1_list + filteded_page2_list

        for line in final_list:
            split_line = line.split(" ")
            accts_dict["Conta"].append(split_line[1])
            accts_dict["Saldo"].append(split_line[2])

        return accts_dict


def _extract_siga_accts():
    dfs = read_pdf("depre_rmb.pdf", pages="all", encoding="latin-1")
    df = pd.concat(dfs)
    accts_list = []
    col_list = df.columns.tolist()
    col_accounts = col_list[0]

    for acc in df[col_accounts]:
        accts_list.append(acc[0:12])

    return accts_list


def _remove_accts_field_mask(acct):
    return acct.replace(".", "")


def _align_accts_with_siga():
    aligned_accts = {"Conta": [], "Saldo": []}
    siga_accts = _extract_siga_accts()
    siafi_accts = _extract_siafi_accts()

    # Ordering accordint to SIGA RMA report
    for siga_acct in siga_accts:
        siga_acct_clean = _remove_accts_field_mask(siga_acct)
        acct_index = siafi_accts["Conta"].index(siga_acct_clean)
        value = siafi_accts["Saldo"][acct_index]

        aligned_accts["Conta"].append(siga_acct_clean)
        aligned_accts["Saldo"].append(value)

    return aligned_accts


def get_siafi_accts():
    """
    Just a getter...
    """
    return _align_accts_with_siga()


def main():
    """
    Just a main function...
    """
    df = pd.DataFrame.from_dict(get_siafi_accts())
    print(df)
    df.to_excel(OUTPUT_FILE_PATH)


main()
