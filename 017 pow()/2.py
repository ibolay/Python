# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  Əgər import math etsək, pow() funksiyası ilə math.pow()   ┃
# ┃  arasında fərq olacaq:                                     ┃
# ┃                                                            ┃
# ┃  - pow()       --> nəticə int və ya float ola bilər        ┃
# ┃  - math.pow()  --> nəticə həmişə float olur                ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


import math
eded = 2

print(pow(eded, 5))       # 32
print(math.pow(eded, 5))  # 32.0