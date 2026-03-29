# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  Bu kodun qısaldılmış halıdır.                             ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


ededler = [5, 12, 18, 25, 30, 7]

yeni_siyahi = [eded      for eded in ededler     if eded % 2 == 0]

print(yeni_siyahi)

# Output:
# ──> [12, 18, 30]