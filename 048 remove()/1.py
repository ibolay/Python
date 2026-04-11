# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  remove() - setdən element silmək üçün istifadə olunur.    ┃
# ┃                                                            ┃
# ┃  Əgər silmək istədiyin dəyər setdə varsa, silinir.         ┃
# ┃                                                            ┃
# ┃  Əgər o dəyər setdə yoxdursa, xəta (error) verir.          ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


meyveler = {"alma", "banan", "portağal"}

meyveler.remove("banan")
# meyveler.remove("armud")  # bu xəta verər (çünki yoxdur)

print(meyveler)

# Output:
# 'banan' silindi
# düzülüş yenə fərqli ola bilər