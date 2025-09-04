import unicodedata
#Extrai apenas as palavras de 5 letras de um arquivo
lista_termo = []
#Lê o arquivo especificado e extrai as palavras de 5 letras, removendo acentos e normalizando-as
with open("lexico.txt", "r", encoding="utf-8") as lexico_arq:
    lexico = lexico_arq.read()
    for palavras in lexico.split():
        if len(palavras) == 5:
            plavra_norm = unicodedata.normalize('NFD', palavras)
            palavra_tratada = ''.join(
                c for c in plavra_norm
                if unicodedata.category(c) != 'Mn'
            )
            lista_termo.append(palavra_tratada)

print("pronto")

# Escreve as palavras tratadas em um novo arquivo se necessário   
#with open("termo_tratado.txt", "w", encoding="") as termo_arq:
#    for item in lista_termo:
#        termo_arq.write(item + "\n")