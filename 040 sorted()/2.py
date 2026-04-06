# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  sorted() verilənləri sıralayır və nəticəni list kimi      ┃
# ┃  qaytarır. Tuple versək belə nəticə list olur.             ┃
# ┃  Əgər tuple kimi saxlamaq istəsək tuple() istifadə edirik. ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


meyve = ("alma", "heyva", "nar", "armud")
yeni_siralama = sorted(meyve)

for deyer in yeni_siralama:
    print(deyer)


print( type(meyve) )
print( type(yeni_siralama) )

# Output:
# alma
# armud
# heyva
# nar
# <class 'tuple'>
# <class 'list'>