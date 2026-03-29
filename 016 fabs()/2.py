# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  abs() və math.fabs() arasındakı fərq:                     ┃
# ┃  - abs()  --> nəticə int və ya float ola bilər             ┃
# ┃  - math.fabs() --> nəticə həmişə float olur                ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


import math

print(abs(-5))        # 5
print(math.fabs(-5))  # 5.0