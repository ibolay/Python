# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  discard() - setdən element silmək üçün istifadə olunur.   ┃
# ┃                                                            ┃
# ┃  Əgər silmək istədiyin dəyər setdə varsa, silinir.         ┃
# ┃                                                            ┃
# ┃  Əgər o dəyər setdə yoxdursa, xəta (error) vermir.         ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


meyveler = {"alma", "banan", "portağal"}

meyveler.discard("banan")
meyveler.discard("armud")  # ❌ yoxdur, amma error vermir

print(meyveler)

# Output:
# 'banan' silindi
# 'armud' olmadığı üçün heç nə dəyişmədi
# düzülüş yenə fərqli ola bilər