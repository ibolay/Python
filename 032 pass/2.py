# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  Pass - müəyyən şərt yerinə yetirildikdə heç nə etmə       ┃
# ┃                                                            ┃
# ┃  Burada i = 6 olduqda heç bir əməliyyat yerinə yetirilmir  ┃
# ┃  və döngü davam edir.                                      ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

for i in range(10):
    if i == 6:
        pass
    print(i)

# Output:
# ──> 0
# ──> 1
# ──> 2
# ──> 3
# ──> 4
# ──> 5
# ──> 6
# ──> 7
# ──> 8
# ──> 9