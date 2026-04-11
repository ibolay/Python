# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  update() metodu ile yeni variable yaratmadan bir set e    ┃
# ┃  başka set elave etmek mümkündür.                          ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


meyveler = { "alma", "banan", "portağal" }
regemler = { 2 , 4 , 1 , 10 }

meyveler.update(regemler)

print(meyveler)

# Output:
# deyerlerin düzülüşü deyişir.