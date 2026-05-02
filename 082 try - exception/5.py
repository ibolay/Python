# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  finally - həmişə işləyir :                                ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


try:
    x = int(input("Bir ədəd daxil et: "))
    netice = 10 / x
except:
    print("Xəta var")
finally:
    print("Bu hissə həmişə işləyir")

# Output:
# (xəta olsa da, olmasa da)
# Bu hissə həmişə işləyir