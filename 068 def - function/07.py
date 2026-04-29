# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  * istifadə edəndə verilən bütün dəyərlər bir parametrdə   ┃
# ┃  toplanır və for ilə üzərindən keçib cəm hesablanır.       ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


def cem(*regemler):
    toplam = 0
    for i in regemler:
        toplam += i
    print(toplam)

cem(1, 3, 5, 6)

# Output:
# 15