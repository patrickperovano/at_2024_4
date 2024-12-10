# Exercicio
"""
Criar uma função chamada dividir que recebe dois números como parâmetros e retorna o resultado da divisão do primeiro número pelo segundo. 
Se o segundo número for zero, a função deve retornar a mensagem "Não é possível dividir por zero". 
Utilize um bloco try-except para tratar a exceção de divisão por zero.
"""

def dividir(num1, num2):
    try:
        resultado = num1 / num2
        return resultado
    except ZeroDivisionError:
        return "Não é possível dividir por zero"

def main():
    num1 = 10
    num2 = 0

    resultado = dividir(num1, num2)
    print("Resultado:", resultado)

    num1 = 10
    num2 = 2

    resultado = dividir(num1, num2)
    print("Resultado:", resultado)

if __name__ == "__main__":
    main()
