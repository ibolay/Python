# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  Birbaşa dəyəri yox, dəyərləri variable-ə yerləşdirib      ┃
# ┃  replace() metodunda istifadə etmək mümkündür.             ┃
# ┃                                                            ┃
# ┃  Qeyd: Böyük hərf və kiçik hərf arasında fərq var.         ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


cumle = 'Bay qara yasirir qara evde ve qara masina sahibdir'

renq = "qara"
evez = 'aq'

print(cumle.replace(renq, evez))


# Output:
# ──> Bay aq yasirir aq evde ve aq masina sahibdir