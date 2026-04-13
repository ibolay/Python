# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  union() - iki seti birləşdirmək üçün istifadə olunur.     ┃
# ┃                                                            ┃
# ┃  Hər iki setdə olan bütün elementləri bir araya gətirir.   ┃
# ┃                                                            ┃
# ┃  Təkrar dəyərlər avtomatik silinir (set qaydasına görə).   ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


meyveler = {"alma", "banan", "portağal"}
terevez = {"xiyar", "kartof", "alma"}

yeni_set = meyveler.union(terevez)

print(yeni_set)

# Output:
# bütün elementlər birləşdi
# 'alma' təkrar olunmadı
# düzülüş yenə fərqli ola bilər