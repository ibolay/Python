# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  sorted() - isə tipinden asılı olmadan hem list hemde      ┃
# ┃  tuple ile iş görür                                        ┃
# ┃                                                            ┃
# ┃  və "sort" dan fergli olaraq yeni siyahı yaradır.          ┃
# ┃  Yani yeni variable yaradıb onun içinde yazırıq.           ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


meyve = ["alma", "heyva", "nar", "armud"]
yeni_siralama = sorted(meyve)

for deyer in yeni_siralama:
    print(deyer)

# Output:
# alma
# armud
# heyva
# nar