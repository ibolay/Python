# pass - Müəyyən bir şərt yerinə yetirildikdə heç nə etmə 
# Burada i = 6 olduqda heç bir şey olmayacaq və döngü dəvam edəcək.

for i in range(10):
    if i == 6:
        pass
    print(i)

