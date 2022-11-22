# FUNCTİONS

# f (x) = 2*x + 5   

# x = 3 
# f(x) = 7

import math


def fx() :  
    print( 2 + 5)

fx()

def f(x) :
    print ( 2 * x + 5 )

f(5)
f(25)
f(50)

def diksriminant ( a , b , c ) :
    print ( b*b - 4*a*c )

# 2*^ + 10x -9 = 0
diksriminant(2, 10, -9)

def iki_kati(x) :
    return 2 * x
    #return None 

print (iki_kati ( iki_kati (23) ) )
x = 5
def iki_kati ():
    #global x 
    return 2 * x 

x = 5
print( iki_kati () )
print (x) 

print( iki_kati()) 
print(x)

def ussunu_al (sayi,us) :
    return sayi**us

print ( ussunu_al(5,3) ) 
print ( ussunu_al (5) ) 
print ( ussunu_al () ) 
print ( ussunu_al (us=5) ) 

print()
print(1 , 5 , 7 )
print("4545", 333, "fdsa")

abc = iki_kati

print(abc() )

yazdir = print
yazdir ("Merhaba Dünya")

print("deneme")
ussunu_al(5,7)

def final_hesapla(vize) : 
    if vize < 50:
        final_icin_gerekli_not = (50 - 0,4 * vize) / 0.6
        print("Final için almanız gereken not:" , math.ceil(final_icin_gerekli_not))

    else:
        print("Final için almanız gerekn not: 50")

final_hesapla(35)   