# Exercício
"""
Crie uma função chamada extrair_informacoes que recebe o nome de um arquivo de texto do 'The Project Gutenberg eBook' e retorna um dicionário com as informações contidas nas primeiras linhas do arquivo, incluindo o título da obra, o autor e a língua. O dicionário deve ter as chaves 'título', 'autor' e 'língua'. 
Não leia o arquivo inteiro para realizar a tarefa, pois o arquivo pode ser muito grande e essa informação está no início do arquivo.
"""


def extrair_informacoes(nome_arquivo):
    pass


# Testando a função
def main():
    for nome_arquivo in ["dados/alice.txt", "dados/shakespeare.txt"]:
        informacoes = extrair_informacoes(nome_arquivo)
        print(informacoes)


if __name__ == "__main__":
    main()
