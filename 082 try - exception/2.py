# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  try-except — proqramda yaranan xətaları (error)           ┃
# ┃  tutmaq və proqramın dayanmasının qarşısını almaq          ┃
# ┃  üçün istifadə olunur.                                     ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


try:
    x = int(input("Bir ədəd daxil et: "))
    print(10 / x)
except:
    print("Xəta baş verdi!")

# Output:
# Bir ədəd daxil et: 0 
# Xəta baş verdi!