def voto(ano):
    from datetime import date
    atual = date.today().year - ano
    print(f'Com {atual} anos: ', end='')
    if atual < 16:
        return f'Com {atual} anos: NÃO VOTA'
    elif 18 > atual >= 16 or atual >= 65:
        return f'Com {atual} anos: VOTO OPCIONAL.'
    if 65 > atual >= 18:
        return f'Com {atual} anos: VOTO OBRIGATÓRIO.'


ano = int(input('Em que ano vc naceu? '))
print(voto(ano))
