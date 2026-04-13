# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  intersection() - iki setdə ortaq olan elementləri         ┃
# ┃  tapmaq üçün istifadə olunur.                              ┃
# ┃                                                            ┃
# ┃  Yəni hər iki setdə olan dəyərləri qaytarır.               ┃
# ┃                                                            ┃
# ┃  Ortak olmayanlar nəticəyə daxil edilmir.                  ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


meyveler = {"alma", "banan", "portağal"}
terevez = {"xiyar", "kartof", "alma"}

netice = meyveler.intersection(terevez)

print(netice)

# Output:
# yalnız ortaq olan: 'alma'
# düzülüş yenə fərqli ola bilər