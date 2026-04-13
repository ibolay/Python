# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  birbaşa deyerleri elde etmek üçün dict in values()        ┃
# ┃  metodundan istifadə edirik.                               ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


telebe = {
    "ad"    : "Mehman",
    "yas"   : 20,
    "seher" : "Gəncə"
}

for i in telebe.values():
    print(i)

# Output:
# Mehman
# 20
# Gəncə