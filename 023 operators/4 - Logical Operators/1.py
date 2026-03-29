# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  4 - Logical Operators (Məntiqi Operatorlar)               ┃
# ┃                                                            ┃
# ┃  a) and → Hər iki tərəf doğru olarsa True qaytarır         ┃
# ┃  b) or  → İfadələrdən biri doğru olarsa True qaytarır      ┃
# ┃  c) not → True olarsa False, False olarsa True qaytarır    ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


x = 5

print(x < 10 and 2 < x)          # True
print(x < 10 or 2 > x)           # True
print(not(x < 10 and 2 < x))     # False