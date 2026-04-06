# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  tuple ilə list arasındaki ferq odurki, liste yeni deyer   ┃
# ┃  elave etmek mümkündür lakin tuple`a yeni deyer            ┃
# ┃  elave etmek və ya evez etmek mümkün deyildir.             ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


meyveler = ("alma", "banan", "portağal") 

meyveler[0] = "armud"
meyveler[3] = "armud"

# Output:
# xeta mesajı :
# 'tuple' object does not support item assignment