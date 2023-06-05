from urllib.request import urlopen

try:
    acesso = urlopen("http://www.pudim.com.br")
    print('O site esta disponivel!')
except:
    print("Ocorreu um erro ao abrir o site.")
