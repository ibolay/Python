# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  olmayan bir deyeri silmek isdedikde xeta mesajı alırıq.   ┃
# ┃  eğer xeta mesajı almaq istemirikse discard() - metodundan ┃
# ┃  istifade etmeliyik.                                       ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


meyveler = {"alma", "banan", "portağal"}
meyveler.discard("armud")

print(meyveler)

# Output:
# deyerlerin düzülüşü deyişir.