# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  add() - setə yeni element əlavə etmək üçün istifadə       ┃
# ┃  olunur.                                                   ┃
# ┃                                                            ┃
# ┃  Əgər əlavə edilən dəyər artıq setdə varsa, təkrar         ┃
# ┃  əlavə olunmur. (çünki setdə təkrar olmur)                 ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


meyveler = {"alma", "banan", "portağal"}

meyveler.add("armud")
meyveler.add("alma")   # artıq var, əlavə olunmayacaq

print(meyveler)

# Output:
# 'armud' əlavə olundu
# 'alma' təkrar olunmadı
# düzülüş yenə fərqli ola bilər