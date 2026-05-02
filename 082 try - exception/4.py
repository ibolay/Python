# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  else - xəta olmazsa işləyir :                             ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


try:
    x = int(input("Bir ədəd daxil et: "))
    netice = 10 / x
except:
    print("Xəta var")
else:
    print("Nəticə:", netice)

# Output:
# (əgər xəta olmazsa)
# Nəticə: 5.0