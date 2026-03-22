# 011 dersdinde input haqqında yazmıştıq ama tam izah etmedik 
# input() ilə istifadəçidən dəyər alıb, if şərti ilə yoxlayaraq nəticəni ekrana çap edə bilərik.

# int(input()) istifadəçidən daxil edilən mətni ədədə çevirərək proqramda istifadə etməyə imkan verir.

eded = int(input("Ədəd daxil et: "))

if eded > 0:
    print("Müsbət ədəddir")
else:
    print("Mənfi və ya 0-dir")