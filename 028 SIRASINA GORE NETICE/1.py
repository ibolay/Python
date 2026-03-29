# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  İki dərəcəli for döngüsü ilə istədiyimiz simvolu          ┃
# ┃  təkrar-təkrar çap edə bilərik.                            ┃
# ┃                                                            ┃
# ┃  say1 → neçə sətir çap olunacaq                            ┃
# ┃  say2 → hər sətirdə neçə simvol olacaq                     ┃
# ┃  simvol → çap olunacaq simvol                              ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


say1 = int(input('Nece defe? '))
say2 = int(input('Nece defe? '))
simvol = input('Hansi simvol? ')

for i in range(say1):

    for x in range(say2):

        print(simvol)

    print()