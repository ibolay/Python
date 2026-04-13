# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  copy() - metodundan istifade ederek 1 ci dict'in          ┃
# ┃  içindeki melumaları kopyalıyırıq                          ┃
# ┃  yeniMelumatlar variable-ına.                              ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


telebe = {
    "ad"    : "Mehman",
    "yas"   : 20,
    "seher" : "Gəncə"
}

yeniMelumatlar = telebe.copy()

yeniMelumatlar["yas"] = 24

print( telebe )
print( yeniMelumatlar )

# Output:
# {'ad': 'Mehman', 'yas': 20, 'seher': 'Gəncə'}
# {'ad': 'Mehman', 'yas': 24, 'seher': 'Gəncə'}