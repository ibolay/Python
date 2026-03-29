# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  Bu kodun uzun halıdır.                                    ┃
# ┃  Kodda ededler əğər cütdürsə                               ┃
# ┃  onları append ilə yeni_siyahi ya yazdırırıq               ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


ededler = [5, 12, 18, 25, 30, 7]
yeni_siyahi = []

for eded in ededler:
    if eded % 2 == 0:
        yeni_siyahi.append(eded)

print(yeni_siyahi)

# Output:
# ──> [12, 18, 30]