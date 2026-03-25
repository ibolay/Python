# Bəlli bir sayıya çatdığında döngü sonlansın :
# və döngüye vaxt verek sleep ilə

import time

for i in range(10, 0, -1):
    print(i)
    if i == 5:
        break
    time.sleep(1)

print("son")
