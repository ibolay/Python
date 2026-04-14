# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  find() - string (mətn) içində istədiyin sözü və ya        ┃
# ┃  hərfi tapmaq üçün istifadə olunur.                        ┃
# ┃                                                            ┃
# ┃  Tapdığı zaman həmin sözün başladığı index-i qaytarır.     ┃
# ┃                                                            ┃
# ┃  Əgər tapmasa -1 qaytarır (error vermir).                  ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


metn = "men python oyrenirəm"

print(metn.find("python"))
print(metn.find("java"))

# Output:
# 4
# -1