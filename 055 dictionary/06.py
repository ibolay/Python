# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  dict içindeki deyerleri elde etmek üçün de eyni           ┃
# ┃  şekilde for - in döngüsünden istifadə edirik.             ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


telebe = {
    "ad"    : "Mehman",
    "yas"   : 20,
    "seher" : "Gəncə"
}

for i in telebe:
    print( telebe [ i ] )

# Output:
# Mehman
# 20
# Gəncə