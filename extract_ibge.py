from typing import List

import pandas as pd
import numpy as np
import requests
import datetime


def listar_anos_desde_2018():
    ano_atual = datetime.datetime.now().year
    lista_anos: list[str] = [str(year) for year in range(2018, ano_atual + 1)]
    return lista_anos


def get_ibge_data(ano=None):
    if ano is None:
        ano = listar_anos_desde_2018()

    pureData = requests.get(f'https://apisidra.ibge.gov.br/values/t/5457/n6/all/v/214/p/{ano}/c782/40124?formato=json')
    return pureData.json()


def format_ibge_data():
    data_json = pd.json_normalize(get_ibge_data(), max_level=0)
    data_json.columns = data_json.values[0]
    data_json[['Município', 'Estado']] = data_json['Município'].str.split(' - ', n=1, expand=True)
    data_json = data_json.iloc[1:]
    print(data_json)


def main():
    print(get_ibge_data())
