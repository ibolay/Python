# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  copy() - dictionary-nin KOPYASINI yaratmaq üçün           ┃
# ┃  istifadə olunur.                                          ┃
# ┃                                                            ┃
# ┃  Orijinal dictionary dəyişmədən yeni bir nüsxə yaradır.    ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


telebe = {"ad": "Ali", "yas": 20}

yeni = telebe.copy()

yeni["ad"] = "Veli"

print(telebe)
print(yeni)

# Output:
# {'ad': 'Ali', 'yas': 20}
# {'ad': 'Veli', 'yas': 20}