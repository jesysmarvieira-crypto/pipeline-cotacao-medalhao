# This is a sample Python script.
from gettext import install
from os import name


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import requests
import pandas as pd
from datetime import datetime

# 1. EXTRAÇÃO (E) - Buscando dados da API
url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
response = requests.get(url)

if response.status_code == 200:
    dados = response.json()

    # 2. TRANSFORMAÇÃO (T) - Organizando os dados para a tabela
    info = dados['USDBRL']

    # Criamos um dicionário com o que queremos salvar
    dados_organizados = {
        'Moeda': [info['name']],
        'Valor_Compra': [float(info['bid'])],
        'Valor_Venda': [float(info['ask'])],
        'Data_Consulta': [datetime.now().strftime('%d/%m/%Y %H:%M:%S')]
    }

    # Transformando em um DataFrame (Tabela do Pandas)
    df = pd.DataFrame(dados_organizados)

    # --- CARGA (L) - Estrutura Medalhão ---

    # 1. Salvando na Bronze (Dado como veio da API)
    # Se quiser salvar o csv bruto:
    df.to_csv('data/bronze/cotação_bruta.csv', index=False)

    # 2. Salvando na Silver (Dado processado que você já tem)
    # Aqui é onde os dados estão limpos e porntos para uso técnico
    df.to_csv('data/silver/cotação_limpa.csv', index=False)

    # 3. Salvando na Gold (O seu arquivo excel final)
    # A Gold é para o usúario final ou dashboards
    df.to_csv('data/gold/cotacao_final.csv', index=False)

    print("-----------------------------------------------")
    print('Arquivos gerados nas camadas Bronze, Silver e Gold!')
    print(df)
    print("-----------------------------------------------")

