'''
 ERROS E EXCEÇÕES
try: tentar um comando
except: se der erro, qual mensagem sera exibida
else: caso nao haja erros, qual o resultado exibir
finally: sempre aonctece independente de sucesso ou erro
exeception: exibe a causa do erro
'''
try:
    a = int(input('Numerado: '))
    b = int(input('Denominador: '))
    r = a / b

except Exception as erro:
    print('Infelizmente tivemos um problema :( ')
    print(f'O erro encontrado foi {erro.__class__}')

except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados digitados ')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero')
except KeyboardInterrupt:
    print('O usuario preferiu nao informar os dados')
except Exception as erro:
    print(f'O erro encontradoi foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}.')
finally:
    print('Volte sempre! Muito obrigado!')