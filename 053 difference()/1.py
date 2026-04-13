# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  difference() - bir setdə olub, digərində olmayan          ┃
# ┃  elementləri tapmaq üçün istifadə olunur.                  ┃
# ┃                                                            ┃
# ┃  Yəni birinci setdən, ikinci setdə olanları çıxır.         ┃
# ┃                                                            ┃
# ┃  Nəticədə yalnız fərqli olanlar qalır.                     ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


meyveler = {"alma", "banan", "portağal"}
terevez = {"xiyar", "kartof", "alma"}

netice = meyveler.difference(terevez)

print(netice)

# Output:
# 'alma' hər ikisində olduğu üçün çıxarıldı
# qalanlar: 'banan', 'portağal'
# düzülüş yenə fərqli ola bilər