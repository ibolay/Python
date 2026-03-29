# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  Logical Operators ilə if                                  ┃
# ┃                                                            ┃
# ┃  - and → hər iki tərəf True olmalıdır ki, şərt doğru olsun ┃
# ┃  - or  → hər hansı biri True olsa şərt doğru olar          ┃
# ┃  - not → True → False, False → True                        ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


x = 10

if x > 29 and x < 11:
    print("Şərt ödənmədi")
elif x > 3 and x < 30:
    print("Şərt ödənildi")