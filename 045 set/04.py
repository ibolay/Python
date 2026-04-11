# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  set - ə birden çox deyer elave etmek üçün update()        ┃
# ┃  metodundan istifade etmek lazımdır.                       ┃
# ┃                                                            ┃
# ┃  add() - bir metod, update() - birden çox metod elave      ┃
# ┃  etmek üçündür.                                            ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


meyveler = {"alma", "banan", "portağal"}
meyveler.update(  [ "çilek", "heyva", "nar" ]  )

print(meyveler)

# Output:
# deyerlerin düzülüşü deyişir.