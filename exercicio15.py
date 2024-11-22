# Exercicio
"""
Crie uma função chamada adicionar_tarefa que deve receber um nome de arquivo e uma string que representa uma tarefa a ser realizada (uma 'todo-list'). 
Caso o arquivo não exista, crie o arquivo com esse nome. Caso exista, adicione a tarefa no final do arquivo.
"""


def adicionar_tarefa(nome_arquivo, tarefa):
    pass  # Implementar a função


def main():
    # Exemplo de uso
    nome_arquivo = "todo_list.txt"
    tarefa = "Comprar leite"
    adicionar_tarefa(nome_arquivo, tarefa)

    tarefa = "Fazer exercícios"
    adicionar_tarefa(nome_arquivo, tarefa)


if __name__ == "__main__":
    main()
