# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  update() - setə birdən çox element əlavə etmək üçün       ┃
# ┃  istifadə olunur.                                          ┃
# ┃                                                            ┃
# ┃  Əgər əlavə olunan dəyərlər artıq mövcuddursa, təkrar      ┃
# ┃  əlavə olunmur.                                            ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


meyveler = {"alma", "banan"}

yeni = ["portağal", "alma", "armud"]

meyveler.update(yeni)

print(meyveler)

# Output:
# 'portağal' və 'armud' əlavə olundu
# 'alma' təkrar olunmadı
# düzülüş yenə fərqli ola bilər