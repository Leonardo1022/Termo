import pandas as pd
from Extrair_palavras import lista_termo
import matplotlib.pyplot as plt

alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

vogais = ["a", "e", "i", "o", "u"]

consoantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
             "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

alfabeto_vlr_total = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0,
                      "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0,
                      "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0,
                      "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

alfabeto_vlr_presenca = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0,
                      "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0,
                      "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0,
                      "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

alfabeto_vlr_posicao = {"a": [0, 0, 0, 0, 0], "b": [0, 0, 0, 0, 0], "c": [0, 0, 0, 0, 0],
                        "d": [0, 0, 0, 0, 0], "e": [0, 0, 0, 0, 0], "f": [0, 0, 0, 0, 0],
                        "g": [0, 0, 0, 0, 0], "h": [0, 0, 0, 0, 0], "i": [0, 0, 0, 0, 0],
                        "j": [0, 0, 0, 0, 0], "k": [0, 0, 0, 0, 0], "l": [0, 0, 0, 0, 0],
                        "m": [0, 0, 0, 0, 0], "n": [0, 0, 0, 0, 0], "o": [0, 0, 0, 0, 0],
                        "p": [0, 0, 0, 0, 0], "q": [0, 0, 0, 0, 0], "r": [0, 0, 0, 0, 0],
                        "s": [0, 0, 0, 0, 0], "t": [0, 0, 0, 0, 0], "u": [0, 0, 0, 0, 0],
                        "v": [0, 0, 0, 0, 0], "w": [0, 0, 0, 0, 0], "x": [0, 0, 0, 0, 0],
                        "y": [0, 0, 0, 0, 0], "z": [0, 0, 0, 0, 0]}

#Calcula quantas vezes cada letra do alfabeto aparece nas palavras no total
def contar_vlr_total():
    for palavra in lista_termo:
        for letra in palavra:
                alfabeto_vlr_total[letra] += 1
    print(alfabeto_vlr_total)
    return alfabeto_vlr_total

#Calcula em quantas palavras cada letra do alfabeto aparece
def contar_vlr_presenca():
    for letra in alfabeto:
        for palavra in lista_termo:
            letras = list(palavra)
            if letra in letras:
                alfabeto_vlr_presenca[letra] += 1
    print(alfabeto_vlr_presenca)
    return alfabeto_vlr_presenca

#Cria um dicionário com a combinação de vogal + consoante
def contar_duas_letras():
    dicionario_vogais_consoantes = {}
    for vogal in vogais:
        for consoante in consoantes:
            dicionario_vogais_consoantes[vogal + consoante] = 0

    #Cria um dicionário com a combinação de consoante + vogal
    dicionario_consoantes_vogais = {}
    for consoante in consoantes:
        for vogal in vogais:
            dicionario_consoantes_vogais[consoante + vogal] = 0

    #Calcula quantas vezes cada combinação de vogal + consoante e consoante + vogal aparece nas palavras
    for palavra in lista_termo:
        for i in range(len(palavra) - 1):
            if palavra[i] in vogais and palavra[i + 1] in consoantes:
                dicionario_vogais_consoantes[palavra[i] + palavra[i + 1]] += 1
            if palavra[i] in consoantes and palavra[i + 1] in vogais:
                dicionario_consoantes_vogais[palavra[i] + palavra[i + 1]] += 1

    duasLetras_vlr_total = dicionario_vogais_consoantes | dicionario_consoantes_vogais
    print(duasLetras_vlr_total)
    return duasLetras_vlr_total

#Calcula em qual posição cada letra do alfabeto aparece nas palavras
def contar_vlr_posicao():
    for palavra in lista_termo:
        for i in range(len(palavra)):
            letra = palavra[i]
            if letra in alfabeto_vlr_posicao:
                alfabeto_vlr_posicao[letra][i] += 1
    print(alfabeto_vlr_posicao)
    return alfabeto_vlr_posicao

def mostrar_qtd(x):
    for p in ax.patches:
        ax.annotate(
            str(p.get_height()),                 # valor (altura da barra)
            (p.get_x() + p.get_width() / 2, p.get_height()),  # posição
            ha='center', va='bottom'             # centralizar horizontal, alinhar embaixo
        )

resposta = input("Qual info deseja ver?(1, 2, 3 ou 4)")

if resposta == "1":
    # contar_vlr_total()
    df = pd.DataFrame(alfabeto_vlr_total.items(), columns=["Letra", "Quantidade"])
    # df.to_csv("vlr_total.csv", index=False)
    vlr_total = pd.read_csv("vlr_total.csv")
    ax = vlr_total.plot(x="Letra", y="Quantidade", kind="bar", legend=True)
    mostrar_qtd(ax)
    plt.show()

elif resposta == "2":
    contar_vlr_presenca()
    df = pd.DataFrame(alfabeto_vlr_presenca.items(), columns=["Letra", "Quantidade"])
    ax = df.plot(x="Letra", y="Quantidade", kind="bar", legend=True)
    mostrar_qtd(ax)
    plt.show()
elif resposta == "3":
    df = pd.DataFrame(contar_duas_letras().items(), columns=["Letras","Quantidade"])
    df = df.sort_values(by="Quantidade", ascending=False)
    #df = df.dropna(subset=["Quantidade"])
    ax = df.set_index("Letras")["Quantidade"].plot(kind="barh")
    #ax = df.plot(x="Letra", y="Quantidade", kind="pie", legend=True)
    # mostrar_qtd(ax)
    plt.show()
elif resposta == "4":
    contar_vlr_posicao()




    
                 
        

# Lê o arquivo .txt e transforma numa tabela (cada linha vira um registro)
# df = pd.DataFrame(alfabeto_vlr_total)

# Salva em Excel
#df.to_excel("Termo.xlsx", index=False)
#print("Arquivo Excel criado com sucesso!")

print("Feito")