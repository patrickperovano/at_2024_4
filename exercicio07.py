# Exercício
"""
Crie uma função chamada extrair_informacoes que recebe o nome de um arquivo de texto do 'The Project Gutenberg eBook' e retorna um dicionário com as informações contidas nas primeiras linhas do arquivo, incluindo o título da obra, o autor e a língua. O dicionário deve ter as chaves 'título', 'autor' e 'língua'. 
Não leia o arquivo inteiro para realizar a tarefa, pois o arquivo pode ser muito grande e essa informação está no início do arquivo.
"""

def extrair_informacoes(nome_arquivo):
    informacoes = {"título": "", "autor": "", "língua": ""}
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                if "Title:" in linha:
                    informacoes["título"] = linha.split("Title:")[1].strip()
                elif "Author:" in linha:
                    informacoes["autor"] = linha.split("Author:")[1].strip()
                elif "Language:" in linha:
                    informacoes["língua"] = linha.split("Language:")[1].strip()
                
                if all(informacoes.values()):
                    break
    except FileNotFoundError:
        return f"O arquivo {nome_arquivo} não foi encontrado."

    return informacoes

# Testando a função
def main():
    for nome_arquivo in ["dados/alice.txt", "dados/shakespeare.txt"]:
        informacoes = extrair_informacoes(nome_arquivo)
        print(informacoes)

if __name__ == "__main__":
    main()