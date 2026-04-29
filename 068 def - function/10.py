# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  ** iki ulduz qoyduqda isə dict tipi olur                  ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


def siyahi(**telebe):
    for acar, deyer in telebe.items():
        print(acar, ":", deyer)

siyahi(ad="Ibrahim", soyad="Kerimov")

# Output:
# ad : Ibrahim
# soyad : Kerimov