# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  Tuple dəyişməz olduğu üçün onun elementini birbaşa        ┃
# ┃  dəyişmək olmaz.                                           ┃
# ┃                                                            ┃
# ┃  Xeta mesajı almamaq üçün Tuple ni list ə çeviririk.       ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


def cem(*regemler):
    print("Əvvəl:", regemler)          # əvvəl tuple kimi gəlir

    regemler_list = list(regemler)     # list-ə çeviririk

    regemler_list[0] = 99              # ilk elementi dəyişək

    print("Dəyişdirilmiş list:", regemler_list)

    # cəmi hesablayırıq
    toplam = 0
    for i in regemler_list:
        toplam += i

    return toplam


netice = cem(1, 3, 5, 6)
print("Cem:", netice)

# Output:
# Əvvəl: (1, 3, 5, 6)
# Dəyişdirilmiş list: [99, 3, 5, 6]
# Cem: 113