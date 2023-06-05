resp = {}


def notas(*num, sit=False):
    """
    -> Função para analisar a situacao de varios alunos.
    :param num: uma ou mais notas dos alunos (aceita varios)
    :param sit:valor opcional, indicando se deve ou nao adicionar a situacao
    :return: dicionário com várias informacoes sobre a situacao da turma.
    """
    resp['qnt'] = len(num)
    resp['Maior'] = max(num)
    resp['menor'] = min(num)
    resp['media'] = sum(num) / len(num)
    if sit:
        if resp['media'] >= 7:
            resp['situação']= 'BOA'
        elif resp['media'] >= 5:
            resp['situação']= 'RAZOAVEL'
        else:
            resp['situação']= 'RUIM'
    return resp


notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
