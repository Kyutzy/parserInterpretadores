"""Nome: Cesar Cunha Ziobro"""
"""Para obter os pontos relativos a este trabalho, você deverá fazer um programa, usando a
linguagem de programação que desejar, que seja capaz de validar expressões de lógica propisicional
escritas em latex e definir se são expressões gramaticalmente corretas. Você validará apenas a forma
da expressão (sintaxe).
A entrada será fornecida por um arquivo de textos que será carregado em linha de comando,
com a seguinte formatação:
1. Na primeira linha deste arquivo existe um número inteiro que informa quantas expressões
lógicas estão no arquivo.
2. Cada uma das linhas seguintes contém uma expressão lógica que deve ser validada.
A saída do seu programa será no terminal padrão do sistema e constituirá de uma linha de saída
para cada expressão lógica de entrada contendo ou a palavra valida ou a palavra inválida e nada mais.
Gramática:
Formula=Constante|Proposicao|FormulaUnaria|FormulaBinaria.
Constante="T"|"F".
Proposicao=[a−z0−9]+
FormulaUnaria=AbreParen OperadorUnario Formula FechaParen
FormulaBinaria=AbreParen OperatorBinario Formula Formula FechaParen
AbreParen="("
FechaParen=")"
OperatorUnario="¬"
OperatorBinario="∨"|"∧"|"→"|"↔"
Cada expressão lógica avaliada pode ter qualquer combinação das operações de negação,
conjunção, disjunção, implicação e bi-implicação sem limites na combiação de preposições e operações.
Os valores lógicos True e False estão representados na gramática e, como tal, podem ser usados em
qualquer expressão de entrada.
Para validar seu trabalho, você deve incluir no repl.it, no mínimo três arquivos contendo
números diferentes de expressões proposicionais. O professor irá incluir um arquivo de testes extra
para validar seu trabalho. Para isso, caberá ao professor incluir o arquivo no seu repl.it e rodar o seu
programa carregando o arquivo de testes"""
import re
import os

tokens = []
TokenInfo = []
Logica = []

def readfile(file):
    with open(file, "r") as f:
        return f.read().split("\n")

def add(regex, token):
    TokenInfo.append((regex, token))

def Tokenize(s:str):
    houve_match = False
    s = s.replace(" ", "")
    tokens.clear()

    while s != "":
        houve_match = False
        for i in TokenInfo:
            igualdade = re.match(i[0], s)
            if igualdade != None:
                houve_match = True
                s = re.sub(i[0], "", s, 1)
                tokens.append((i[1], igualdade.group()))
                break
        if not houve_match:
            tokens.clear()
            return False
    return tokens

def FormulaUnaria(a):
    lista = [["AbreParen", "Unario", "Formula", "FechaParen"],
    ["AbreParen", "Unario", "Constante", "FechaParen"]]
    if a in lista:
        return True
    return False

def FormulaBinaria(a):
    lista = [
    ["AbreParen", "Formula", "Binario", "Formula", "FechaParen"],
    ["AbreParen", "Constante", "Binario", "Constante", "FechaParen"],
    ["AbreParen", "Formula", "Binario", "Constante", "FechaParen"],
    ["AbreParen", "Constante", "Binario", "Formula", "FechaParen"]
    ]
    if a in lista:
        return True
    return False

def Constante(a):
    lista = [["Constante"]]
    if a in lista:
        return True
    return False

def Proposicao(a):
    lista = [["Formula"]]
    if a in lista:
        return True
    return False

def classificar(a):
    if FormulaBinaria(a) or FormulaUnaria(a) or Constante(a) or Proposicao(a):
        return True
    return False

if __name__ == "__main__":
    add(r'\(', "AbreParen")
    add(r'\)', "FechaParen")
    add(r"T|F", "Constante")
    add(r'[a-z0-9]+', "Formula")
    add(r'\\neg', "Unario")
    add(r'\\\\lor|\\\\land|\\\\rightarrow|\\\\leftrightarrow', "Binario")
    
    for file in os.listdir("./"):
            if file.endswith(".txt"):
                d = readfile(file)
                tamanho = int(d[0])
                
                for i in range(1, tamanho+1):
                    Tokenize(d[i])
                    for j in range(len(tokens)):
                        Logica.append(tokens[j][0])
                    print("válida") if classificar(Logica) == True else print("inválida")
                    Logica.clear()


