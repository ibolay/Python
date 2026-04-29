# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  Rekursiv funksiya öz-özünü çağırır.                       ┃
# ┃  Dayanma nöqtesi olmazsa sonsuz dövr yaranar.              ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


def say(n):
    if n == 0:      # Baza hal (dayanma nöqtəsi)
        return
    print(n)
    say(n - 1)      # Özünü çağırır

say(5)

# Output:
# 5
# 4
# 3
# 2
# 1