# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  hem açar sözleri hemde deyerleri elde etmek üçün          ┃
# ┃  items() metodundan istifadə edirik.                       ┃
# ┃                                                            ┃
# ┃  avtomatik olaraq x`e açar sözler y`e deyerler verilir.    ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


telebe = {
    "ad"    : "Mehman",
    "yas"   : 20,
    "seher" : "Gəncə"
}

for x, y in telebe.items():
    print(x , y)

# Output:
# ad Mehman
# yas 20
# seher Gəncə