# Exercício
"""
O código abaixo apresenta um problema relacionado ao tratamento de exceções em Python. Analise o seguinte código e responda à pergunta:
"""

def main():
    # Uma função genérica qualquer
    pass

if __name__ == "__main__":
    try:
        main()
    except:
        print("O código não funcionou corretamente")

""""
Por que esse código pode ser considerado uma má prática quando se trata de tratamento de exceções? Que problemas podem surgir ao utilizar um bloco `except` sem especificar o tipo de exceção?
"""

# Resposta:

"""
Ocultação de erros, comportamento imprevisível, perda de especificidade e dificuldade na depuração.
"""