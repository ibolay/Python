# Break və continue arasındaki fərq odurki :

# Break - ifadəsi döngüyü tamamilə sonlandırır.
# Continue - ifadəsi isə o döngünü sonlandırıb diğərinə atlamasıdır.
# Həm break həmdəki continue nin istifadəsi

for i in range( 1 , 10 ):
    if i % 2 == 0:
        continue
    if i > 5:
        break
    print("Islenen sayi: ", i )


"""

İşlenen sayi: 1
İşlenen sayi: 3
İşlenen sayi: 5

"""

