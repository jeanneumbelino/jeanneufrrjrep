print('===== QUESTÃO 18 =====')
n1 = float(input('Nota da primeira avaliação: '))
n2 = float(input('Nota da segunda avaliação: '))
ro = str(input('Voce realizou a prova optiva [S/N]: '))
if ro == 's':
    o = int(input('Nota da Optativa: '))
    media = (n1 + n2 + o - (min(n1,n2,o))) / 2
    if media >= 6.0:
        print('MEDIA = {:.1f} \nAPROVADO'.format(media))
    if media < 3.0:
        print('MEDIA = {:.1f} \nREPROVADO'.format(media))
    if media >= 3.0 and media < 6.0:
        print('MEDIA = {:.1f} \nEXAME'.format(media))
if ro == 'n':
    print('-1')
    media2 = (n1 + n2) / 2
    if media2 >= 6.0:
        print('MEDIA = {:.1f} \nAPROVADO'.format(media2))
    if media2 < 3.0:
        print('MEDIA = {:.1f} \nREPROVADO'.format(media2))
    if media2 >= 3.0 and media2 < 6.0:
        print('MEDIA = {:.1f} \nEXAME'.format(media2))
