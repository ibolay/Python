# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  elif - Əlavə şərt yoxlamaq üçün istifadə olunur           ┃
# ┃                                                            ┃
# ┃  - if → ilk şərti yoxlayır                                 ┃
# ┃  - elif → əlavə şərtləri yoxlayır                          ┃
# ┃  - else → heç biri doğru olmazsa işləyir                   ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


bal = 75

if bal >= 90:
    print("Əla")
elif bal >= 70:
    print("Yaxşi")
elif bal >= 50:
    print("Kafi")
else:
    print("Kəsildi")