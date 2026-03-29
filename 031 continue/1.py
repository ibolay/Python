# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  continue - Ötür deməkdir                                  ┃
# ┃  Döngü içində müəyyən şərtə çatdıqda həmin iterasiyanı     ┃
# ┃  atlayır və növbəti iterasiyaya keçir                      ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

telefon_nomre = "122-3223-4232"

for qutu in telefon_nomre:

    if qutu == "-":

        continue

    print(qutu, end="")

# Output:
# ──> 12232234232