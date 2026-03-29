# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  Daha əvvəl math modulunu görmüşdük, indi isə time         ┃
# ┃  modulu ilə işləyəcəyik                                    ┃
# ┃  sleep() - ilə vaxt təyin edirik.                          ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


import time

for saniye in range(10, 0, -1):
    print(saniye)
    time.sleep(1)

print('Film Başladi')

# Output:
# ──> 10
# ──> 9
# ──> 8
# ──> 7
# ──> 6
# ──> 5
# ──> 4
# ──> 3
# ──> 2
# ──> 1
# ──> Film Başladi