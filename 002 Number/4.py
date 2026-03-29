# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  Python-da string ilə number birbaşa toplana bilməz.       ┃
# ┃  Ona görə number əvvəl string tipinə çevrilməlidir.        ┃
# ┃  Misal: str() funksiyasından istifadə olunur.              ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


age = 20
age += 1

print("Menim " + str(age) + " yasim var")


# Output:
# ──> Menim 21 yasim var