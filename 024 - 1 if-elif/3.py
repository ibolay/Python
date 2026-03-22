# if və else-dən əlavə, bir neçə şərt yoxlamaq istədikdə elif istifadə olunur.

"""
if   → ilk şərti yoxlayir
elif → əlavə şərtləri yoxlayir
else → heç biri doğru olmazsa işləyir

"""

bal = 75

if bal >= 90:
    print("Əla")

elif bal >= 70:
    print("Yaxşi")
    
elif bal >= 50:
    print("Kafi")
    
else:
    print("Kəsildi")


