# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  5 - Identity Operators                                    ┃
# ┃                                                            ┃
# ┃  a) is     → Hər iki variable eyni olarsa True qaytarır    ┃
# ┃  b) is not → Hər iki variable eyni deyilsə True qaytarır   ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


x = ["apple", "banana"]
y = ["apple", "banana"]

z = x

print(x is z)      # True qayıdır, çünki x ilə z eynidir
print(x is not z)  # False qayıdır, çünki x ilə z eynidir