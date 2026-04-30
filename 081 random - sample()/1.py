# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  sample - teyin etdiyimiz sayıda ededi qaytarır.           ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


import random

meyve = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ]

Eded = random.sample(meyve, 2)

print(Eded)

# Output:
# [2, 5]   <-- Misal