# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  Rəqəmlərə aid metodlar:                                   ┃
# ┃                                                            ┃
# ┃  - bit_length()  : say ədədi neçə bit ilə ifadə olunur     ┃
# ┃  - real          : ədədin real hissəsini göstərir          ┃
# ┃  - conjugate()   : kompleks ədəd üçün konjugatını qaytarır ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


say = 16

print(say.bit_length())
print(say.real)
print(say.conjugate())

print(type(say))


# Output:
# ──> 5
# ──> 16
# ──> 16
# ──> <class 'int'>