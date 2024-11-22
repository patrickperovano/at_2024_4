# Exercicio
"""
Escreva uma função chamada filtrar_linhas que recebe três argumentos: o nome de um arquivo de entrada, o nome de um arquivo de saída e uma palavra. A função deve ler o arquivo de entrada e escrever no arquivo de saída todas as linhas que contêm a palavra especificada. Se o arquivo de entrada não existir, a função deve exibir uma mensagem de erro apropriada.

Siga os passos abaixo:

1. Crie a função filtrar_linhas que recebe os três parâmetros.
2. Abra o arquivo de entrada em modo de leitura.
3. Para cada linha no arquivo de entrada, verifique se a palavra está presente.
4. Se a linha contiver a palavra, escreva essa linha no arquivo de saída.
5. Trate a exceção caso o arquivo de entrada não exista.

# Exemplo de uso da função:
filtrar_linhas('entrada.txt', 'saida.txt', 'palavra')
"""


def filtrar_linhas(entrada, saida, palavra):
    pass


def main():
    filtrar_linhas("alice.txt", "alice_saida.txt", "Alice")


if __name__ == "__main__":
    main()
