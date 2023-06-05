from time import sleep
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # opção de listar o conteudo do arquivo
        lerarquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('≥≥≥ Saindo do Sistema ≤≤≤')
        break
    else:
        print('\033[31mErro! Digite uma opção válida.\033[m')
    sleep(1)
