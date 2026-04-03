# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  sort() - tersine sıralamaq üçün reverse=True              ┃
# ┃  arqumentinden istifadə edilir.                            ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


meyve = ["alma", "heyva", "nar", "armud"]
meyve.sort(reverse=True)

for deyer in meyve:
    print(deyer)

# Output:
# nar
# heyva
# armud
# alma