from datetime import date

def voto(n):
    idade = date.today().year - n
    if 18 <= idade <= 65:
        return f'Com {idade} anos, o voto é obrigadorio.'
    if 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos, o voto é facultativo.'
    if idade < 16:
        return f'Com {idade} anos, voce ainda nao tem o direito de votar.'


# Programa Principal
nasc = int(input('Em que anos voce nasceu? '))
print(voto(nasc))
