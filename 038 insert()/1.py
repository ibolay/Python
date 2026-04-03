# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  insert() - listin içine deyer elave elemek üçün           ┃
# ┃  istifadə edilir.                                          ┃
# ┃                                                            ┃
# ┃  1 ci arqument hara elavə edəcəyimizi                      ┃
# ┃  2 ci arqument isə yeni deyeri bildirir                    ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


meyve = ["alma", "armud", "nar", "heyva"]
meyve.insert( 3 , "qarpiz" )

for deyer in meyve:
    print(deyer)

# Output:
# alma
# armud
# nar
# qarpiz
# heyva