print("|{:>10}|".format("Ali"))          # sağa düzləndirir, 10 yer ayırır
print("|{:>10}|".format("Ibrahim"))      # sağa düzləndirir, uzun söz boşluğa sığır
print("|{:>10}|".format("Python"))       # sağa düzləndirir
print("|{:>10}|".format("Azerbaijan"))   # tam 10 yerə yerləşdirir
print("|{:>10}|".format("10"))           # ədəd kimi string, sağa düzlənir


# |       Ali|
# |   Ibrahim|
# |    Python|
# |Azerbaijan|
# |        10|

#____________________________________________________________________________________#

print("|{:<10}|".format("Ali"))          # sola düzləndirir, sağa boşluq verir
print("|{:<10}|".format("Ibrahim"))      # sola düzlənir
print("|{:<10}|".format("Python"))       # sola düzlənir
print("|{:<10}|".format("Azerbaijan"))   # sola düzlənir
print("|{:<10}|".format("10"))           # sola düzlənir


# |Ali       |
# |Ibrahim   |
# |Python    |
# |Azerbaijan|
# |10        |

#____________________________________________________________________________________#

print("|{:^10}|".format("Ali"))          # ortalayır, hər iki tərəfə boşluq verir
print("|{:^10}|".format("Ibrahim"))      # mərkəzə yerləşdirir
print("|{:^10}|".format("Python"))       # mərkəz
print("|{:^10}|".format("Azerbaijan"))   # mərkəz
print("|{:^10}|".format("10"))           # mərkəz


# |   Ali    |
# | Ibrahim  |
# |  Python  |
# |Azerbaijan|
# |    10    |

#____________________________________________________________________________________#

print("{:0>5}".format(7))     # soldan 0 ilə doldurur → 00007
print("{:0>5}".format(45))                            # 00045
print("{:0>5}".format(999))                           # 00999
print("{:0>5}".format(1234))                          # 01234

#____________________________________________________________________________________#

print("{:.2f}".format(5.6789))   # 2 onluq mərtəbəyə qədər yuvarlaqlaşdırır
print("{:.2f}".format(10))       # tam ədəd olsa da .00 əlavə edir
print("{:.2f}".format(3.1))      # 3.10 kimi göstərir
print("{:.2f}".format(99.999))   # 100.00 olur (yuvarlaqlaşdırma)


# Output:
# 5.68
# 10.00
# 3.10
# 100.00

#____________________________________________________________________________________#

print("{:,}".format(1000))       # minlikləri vergüllə ayırır
print("{:,}".format(1000000))    # milyon
print("{:,}".format(123456789))  # böyük ədəd


# Output:
# 1,000
# 1,000,000
# 123,456,789

#____________________________________________________________________________________#
