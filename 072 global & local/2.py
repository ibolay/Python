# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  global istifadə etsək, global dəyişən dəyişir.            ┃
# ┃  Funksiya içində edilən dəyişiklik çöldə də qalır.         ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


ad = "Semed"

def test():
    global ad
    ad = "Bextiyar"
    print(ad)

test()
print(ad)

# Output:
# Bextiyar
# Bextiyar