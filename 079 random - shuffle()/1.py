# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  shuffle - listin içindeki deyerleri random qarıştırır.    ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


import random

meyve = [1, 5, 2, "alma", "armud", "nar", "heyva"]

random.shuffle(meyve)

print(meyve)

# Output:
# [2, 'alma', 'armud', 'nar', 5, 'heyva', 1]   <-- Misal