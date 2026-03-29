# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  Break və Continue arasındakı fərq:                        ┃
# ┃                                                            ┃
# ┃  Break - döngünü tamamilə sonlandırır                      ┃
# ┃  Continue - həmin döngünü atlayıb növbətiyə keçir          ┃
# ┃                                                            ┃
# ┃  Həm break həm də continue nümunəsi:                       ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

for i in range(1, 10):
    if i % 2 == 0:
        continue
    if i > 5:
        break
    print("İşlənən sayi:", i)

# Output:
# ──> İşlənən sayi: 1
# ──> İşlənən sayi: 3
# ──> İşlənən sayi: 5
