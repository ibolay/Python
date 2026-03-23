# Öncəliklə inputa eded daxil edirik, daxil edilen ededi çeviririk int tipini
# Çünkü İnputa daxil edilen eded String kimi sayılır biz onu int e çeviririk

# Vurma Cedveli


eded = int( input("Bir Eded Daxil Edin: ") )

for i in range(1, 9+1):
    print( eded, "*" , i , "=" , eded * i )


# "" - içinde olanlar arifmetik operator değil.