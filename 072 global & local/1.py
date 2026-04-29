# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  Local dəyişən yalnız funksiyanın içində işləyir.          ┃
# ┃  Global dəyişən isə hər yerdən görünür.                    ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


ad = "Semed"

def test():
    ad = "Bextiyar"
    print(ad)

test()

print(ad)

# Output:
# Bextiyar
# Semed