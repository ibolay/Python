# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  Əgər dırnaq içinə istər NUMBER istər STRING bir simvol    ┃
# ┃  yazsaq, nəticədə count("") metodu 2 qaytarır.             ┃
# ┃                                                            ┃
# ┃  İzah:                                                     ┃
# ┃  - İlk öncə bir boşluq yaradılır                           ┃
# ┃  - Sonra o boşluğa simvol əlavə edilir                     ┃
# ┃  Nəticə olaraq həmişə bir say artıq əldə edirik.           ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


ad = "1"
print(ad.count(""))


# Output:
# ──> 2