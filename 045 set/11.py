# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  iki fergli set içinde eyni deyerler varsa fergli          ┃
# ┃  olanlarını tapmaq üçün difference() - metodundan          ┃
# ┃  istifadə edilir.                                          ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


meyve = {"alma", "banan", "pomidor"}
terevez = {"xiyar", "kartof", "pomidor"}

print( meyve.difference(terevez) )

# Output:
# {'alma', 'banan'}  vəya  {'banan', 'alma'}