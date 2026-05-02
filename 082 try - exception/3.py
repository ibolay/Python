# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  İstifadəçi səhv dəyər daxil edərsə və ya 0 yazarsa        ┃
# ┃  proqram çökməsin deyə xətaları tuturuq :                  ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


try:
    x = int(input("Bir ədəd daxil et: "))
    print(10 / x)
except ZeroDivisionError:
    print("0-a bölmək olmaz!")
except ValueError:
    print("Zəhmət olmasa düzgün ədəd daxil et!")

# Output (mümkün hallara görə):
# 1. Əgər istifadəçi 0 yazsa:
# 0-a bölmək olmaz!

# 2. Əgər istifadəçi "abc" kimi dəyər yazsa:
# Zəhmət olmasa düzgün ədəd daxil et!

# 3. Əgər düzgün ədəd yazsa (məs: 2):
# 5.0