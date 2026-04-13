# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  get() - dictionary-dən (sözlükdən) dəyər almaq üçün       ┃
# ┃  istifadə olunur.                                          ┃
# ┃                                                            ┃
# ┃  Açar (key) mövcuddursa, onun dəyərini qaytarır.           ┃
# ┃                                                            ┃
# ┃  Əgər açar yoxdursa, xəta vermir, None qaytarır.           ┃
# ┃  (və ya öz verdiyin başqa dəyəri qaytara bilər)            ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


telebe = {
    "ad": "Ali",
    "yas": 20
}

print(telebe.get("ad"))
print(telebe.get("soyad"))        # yoxdur
print(telebe.get("soyad", "yoxdur"))

# Output:
# Ali
# None
# yoxdur