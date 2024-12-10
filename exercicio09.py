# Exercicio
"""
Você deve criar uma função chamada ler_csv que recebe como argumentos o nome de um arquivo CSV e o separador (que deve ter como valor padrão ','). A primeira linha do arquivo deve ser considerada como cabeçalho, e a função deve retornar um dicionário onde cada chave é o nome da coluna e o valor é uma lista com os valores daquela coluna.

Caso o arquivo passado não exista, a função deve imprimir a mensagem "Arquivo não encontrado" e retornar None. Para isso, trate a exceção FileNotFoundError no seu código.

Exemplo da estrutura do CSV:
nome,idade,cidade
Alice,30,São Paulo
Bob,25,Rio de Janeiro

Retorno esperado:
{
    'nome': ['Alice', 'Bob'],
    'idade': [30, 25],
    'cidade': ['São Paulo', 'Rio de Janeiro']
}
"""

def ler_csv(nome_arquivo, separador=","):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            cabeçalho = linhas[0].strip().split(separador)
            dados = {chave: [] for chave in cabeçalho}
            
            for linha in linhas[1:]:
                valores = linha.strip().split(separador)
                for chave, valor in zip(cabeçalho, valores):
                    if valor.isdigit():
                        valor = int(valor)
                    dados[chave].append(valor)
        
        return dados
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return None

def main():
    # Testando a função
    resultado = ler_csv("dados/dados_09.csv")
    if resultado is not None:
        print(resultado)

if __name__ == "__main__":
    main()