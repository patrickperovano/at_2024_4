# Exercicio
"""
Utilizando a função da questão anterior através do "import exercicio09" ou "from exercicio09 import ler_csv" leia o arquivo dados_anac_2024.csv. Este arquivo contém dados de cancelamentos e atrasos de voos no Brasil.
Crie as funções abaixo para responder as perguntas:

a) Qual o voo que foi percentualmente mais cancelado?
b) Liste as companhias aéreas presentes no arquivo.
c) Qual o número do voo entre Fortaleza (SBFZ) e Galeão (SBGL) que mais teve atrasos maiores que 60 minutos percentualmente?
"""


"""
voo_mais_cancelado
"""

def voo_mais_cancelado(dados):
    max_cancelado = -1
    voo_cancelado = None
    for i in range(len(dados['N_Voo'])):
        cancelamento = float(dados['Percentuais_de_Cancelamentos'][i].replace(',', '.'))
        if cancelamento > max_cancelado:
            max_cancelado = cancelamento
            voo_cancelado = dados['N_Voo'][i]
    return voo_cancelado

"""
listar_companhias
"""

def listar_companhias(dados):
    return list(set(dados['Empresa_Aerea']))

"""
voo_mais_atrasado
"""

def voo_mais_atrasado(dados):
    max_atraso = -1
    voo_atrasado = None
    for i in range(len(dados['N_Voo'])):
        if dados['Aeroporto_Origem_Designador_OACI'][i] == 'SBFZ' and dados['Aeroporto_Destino_Designador_OACI'][i] == 'SBGL':
            atraso = float(dados['Percentuais_de_Atrasos_superiores_a_60_minutos'][i].replace(',', '.'))
            if atraso > max_atraso:
                max_atraso = atraso
                voo_atrasado = dados['N_Voo'][i]
    return voo_atrasado

"""
main
"""

from exercicio09 import ler_csv

def main():
    dados = ler_csv("dados/dados_anac_2024.csv", separador=";")
    if dados:
        print("Voo percentualmente mais cancelado:", voo_mais_cancelado(dados))
        print("Companhias aéreas presentes:", listar_companhias(dados))
        print("Número do voo entre Fortaleza e Galeão com mais atrasos:", voo_mais_atrasado(dados))

if __name__ == "__main__":
    main()