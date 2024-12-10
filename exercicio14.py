# Exercício
"""
Você deve implementar uma leitura de um arquivo JSON chamado 'dados_ibge_ipca.json'. Este arquivo contém dados sobre o IPCA acumulado. Siga os passos abaixo:

1. Utilize o pacote json para carregar os dados desse arquivo.
2. Filtre os dados onde a chave 'D2C' é igual a 2265, que representa dados do IPCA acumulado para 12 meses.
3. O valor percentual do IPCA acumulado para 12 meses está na chave 'V'.
4. Crie uma função chamada get_maior_ipca que retorna o mês e o ano que tiveram o maior valor de IPCA acumulado para 12 meses.
5. Crie outra função chamada get_menor_ipca que retorna o mês e o ano que tiveram o menor valor de IPCA acumulado para 12 meses.

Certifique-se de que suas funções retornam os valores no formato "Mês/Ano" (por exemplo, "Janeiro/2023").
"""

import json
from datetime import datetime

def get_maior_ipca():
    try:
        with open('dados_ibge_ipca.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        
        dados_filtrados = [item for item in dados if item['D2C'] == 2265]
        
        maior_ipca = max(dados_filtrados, key=lambda x: float(x['V']))
        data_maior_ipca = datetime.strptime(maior_ipca['D1C'], '%Y%m')
        mes_ano_maior = data_maior_ipca.strftime('%B/%Y')

        return mes_ano_maior
    except FileNotFoundError:
        return "O arquivo 'dados_ibge_ipca.json' não foi encontrado."
    except Exception as e:
        return f"Ocorreu um erro: {e}"

def get_menor_ipca():
    try:
        with open('dados_ibge_ipca.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        
        dados_filtrados = [item for item in dados if item['D2C'] == 2265]
        
        menor_ipca = min(dados_filtrados, key=lambda x: float(x['V']))
        data_menor_ipca = datetime.strptime(menor_ipca['D1C'], '%Y%m')
        mes_ano_menor = data_menor_ipca.strftime('%B/%Y')

        return mes_ano_menor
    except FileNotFoundError:
        return "O arquivo 'dados_ibge_ipca.json' não foi encontrado."
    except Exception as e:
        return f"Ocorreu um erro: {e}"

def main():
    maior = get_maior_ipca()
    menor = get_menor_ipca()

    print(f"Maior IPCA acumulado para 12 meses: {maior}")
    print(f"Menor IPCA acumulado para 12 meses: {menor}")

if __name__ == "__main__":
    main()
