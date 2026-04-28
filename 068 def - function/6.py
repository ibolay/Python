# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  Funksiyanı tuple a çevirmek üçün parametrden              ┃
# ┃  evvel * qoyulur.                                          ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


def test(*adlar):
    print( type(adlar) )
    print( adlar )

test("Ali", "Veli", "Ayşe")

# Output:
# <class 'tuple'>
# ('Ali', 'Veli', 'Ayşe')