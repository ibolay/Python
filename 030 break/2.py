# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  Bəlli bir sayıya çatdığında döngü sonlansın               ┃
# ┃  Döngüyə vaxt verək time.sleep() ilə                       ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

import time

for i in range(10, 0, -1):
    print(i)
    if i == 5:
        break
    time.sleep(1)

print("son")

# Output:
# ──> 10
# ──> 9
# ──> 8
# ──> 7
# ──> 6
# ──> 5
# ──> son