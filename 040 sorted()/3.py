# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  sorted() - tersine sıralamaq üçün reverse=True            ┃
# ┃  arqumentinden istifadə edilir. sorted() yeni list         ┃
# ┃  qaytarır və original list dəyişmir.                       ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


meyve = ["alma", "heyva", "nar", "armud"]

yeni_siralama = sorted(meyve, reverse=True)

for deyer in yeni_siralama:
    print(deyer)

# Output:
# nar
# heyva
# armud
# alma