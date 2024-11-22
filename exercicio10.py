# Exercicio
"""
Utilizando a função da questão anterior através do "import exercicio10" ou "from exercicio10 import ler_csv" leia o arquivo dados_anac_2024.csv. Este arquivo contém dados de cancelamentos e atrasos de voos no Brasil.
Crie as funções abaixo para responder as perguntas:

a) Qual o voo que foi percentualmente mais cancelado?
b) Liste as companhias aéreas presentes no arquivo.
c) Qual o número do voo entre Fortaleza (SBFZ) e Galeão (SBGL) que mais teve atrasos maiores que 60 minutos percentualmente?
"""

from exercicio09 import ler_csv


def voo_mais_cancelado(dados):
    return None


def listar_companhias(dados):
    return None


def voo_mais_atrasado(dados):
    return None


def main():
    dados = ler_csv("dados_anac_2024.csv")
    print("Voo percentualmente mais cancelado:", voo_mais_cancelado(dados))
    print("Companhias aéreas presentes:", listar_companhias(dados))
    print("Número do voo entre Fortaleza e Galeão com mais atrasos:", voo_mais_atrasado(dados))


if __name__ == "__main__":
    main()
