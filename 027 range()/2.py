# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  Öncəliklə inputa ədəd daxil edirik,                       ┃
# ┃  daxil edilən ədədi int tipinə çeviririk.                  ┃
# ┃  Çünki inputa daxil edilən ədəd String kimi sayılır.       ┃
# ┃                                                            ┃
# ┃  Vurma Cədvəli                                             ┃
# ┃                                                            ┃
# ┃  "" içində olanlar arifmetik operator deyil,               ┃
# ┃  sadəcə ekrana çap üçün istifadə olunur.                   ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


eded = int(input("Bir ədəd daxil edin: "))

for i in range(1, 9 + 1):
    print(eded, "*", i, "=", eded * i)