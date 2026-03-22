# 4 - Logical Operators - Məntigi Operatorlar


# Logical Operators
   # a)   and   - Her iki teref doğrudursa "True" qaytarır.
   # b)   or    - ifadələrdən biri doğrudursa "True" qaytarır.
   # c)   not   - "True" olarsa tersine çevirerek "False" qaytarır, "False" olarsa "True" qaytarır.


x = 5

print( x < 10 and 2 < x )          # True
print( x < 10 or  2 > x )          # True
print( not( x < 10 and 2 < x ) )   # False

