# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  Faktoriyal rekursiv olaraq hesablanır.                    ┃
# ┃  n! = n * (n-1)!                                           ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


def faktoriyal(n):
    if n == 0 or n == 1:   # Baza hal
        return 1
    return n * faktoriyal(n - 1)   # Rekursiv hissə

print(faktoriyal(5))

# Output:
# 120