# Exercicio
"""
Você recebeu um arquivo de texto chamado 'entrada13.txt' que contém várias linhas. Seu objetivo é criar um programa que 
remova todas as linhas duplicadas desse arquivo e escreva cada linha única em um novo arquivo chamado 'saida.txt'. 
Siga as instruções abaixo:

1. Leia o conteúdo do arquivo 'entrada.txt'.
2. Remova as linhas duplicadas.
3. Escreva as linhas únicas no arquivo 'saida.txt'.

Certifique-se de que o arquivo 'saida.txt' seja criado e que cada linha única apareça apenas uma vez.
"""

def remover_linhas_duplicadas(entrada, saida):
    try:
        with open(entrada, 'r', encoding='utf-8') as arquivo_entrada:
            linhas = arquivo_entrada.readlines()
        
        linhas_unicas = list(set(linhas))
        
        with open(saida, 'w', encoding='utf-8') as arquivo_saida:
            for linha in linhas_unicas:
                arquivo_saida.write(linha)
    except FileNotFoundError:
        print(f"O arquivo {entrada} não foi encontrado.")

def main():
    # Chame a função com os nomes dos arquivos
    remover_linhas_duplicadas("dados/entrada13.txt", "saida_duplicadas.txt")

if __name__ == "__main__":
    main()
