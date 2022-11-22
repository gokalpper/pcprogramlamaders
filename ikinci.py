
# if a > b :
#     print ("a b 'den büyük")
        # print( " a'nın değeri : " , a , "b 'nin değeri" , b)
# if b > a :
#     print(" a b 'den küçük")
# if == b :    
#     print("a b ye eşit")


# else : 
#     print( "a b'den küçük")
# elif b > a :
#     print("b a 'dan büyük")
# elif a == b :
#     print("a b' ye eşit") 

# blok nesnesi başladı ise kesinlikle altında girinti bekler. 
# if 4 < 1 :
#     pass
# if 4 > 1 :
#     print("bu doğru bir durum!")

# değişken_adı = 5 
# int - integer - tam sayı tipli bir değişken 
# print( type ( değişken_adı) ) 

# kesir = 3 / 7 
# float - kesir tipli değişken.
# ondalık olarak nokta (.) işareti kullanılır!
# kesir = 3.14159265
# print ( type (kesir) , kesir) 

# metin = "metin tipinde"
# str - string metin tipinde bir değişken. 
# print( type ( metin) )

# x = "5" # str 
# y = 5 # int 
# z = 5.0 # float 

# print ( x==y )
# x == y ? eşit değildir.   print (type (x) == type (y) )
# x== z  ? eşit

# t = False 
# t = True 
# bool - boolean / Doğru - Yanlış tipli değişken.
# Doğru True 
# Yanlış False 
# print ( type ( t ) )





# Doğru yanlış tipi değeri ilk harfi büyük yazılır.
# True = 5 anahtar kelime olduğu için değişken olamaz.

# true =  değişken olabilir.

# a = 100.0 
# b = " bir daha yaramazlık yapmayacağım ! / n"
# print ( a * b)

# a = "merhaba "
# b = "dünya "
# c = str(a) + b
# print(c)

# z = "55.2"
# x = "23"

# print(int(x) + float(z) )

# t = "False"
# print( bool (t) ) 

# t = 0 
# print( t == False)
# t = 1 
# print ( t == True)

# import random 

# rastgele = random.randrange (1,10)

# input("1 ve 10 arası rastegele sayı giriniz.") 

# kul_veri = input ("1 ve 10 arası rastgele sayı giriniz.")

# if kul_veri == rastgele : 
#     print ("Tebrikler Sayıyı Buldunuz")
# else: 
#     print("bilgisayarın  tuttuğu sayı: ", rastgele)
#     print("Sizin girdiğiniz sayı :" , kul_veri)
#     print("Lutfen Yeniden Deneyiniz.")

# iç içe if durumları 
# a , b , c = 1 , 2 , 3 

# if 3 > 1 :
#     print("3 bir rakamından büyük ")
#     if 3 > 2 :
#         print("2 rakamından da büyük")
#         if 3==3 : 
#             print (" bu değerler birbirlerine eşit")
#             else :
#                 print("eşit değil")
#                     print("bu kimin altında ?")
#                     print (bu kimin altında?)
        
# else : 
#     print("3 rakamından büyük değil.")


# bir den fazla şart bulunan durumlar 

# if 3 > 2 and 2 > 1
#     print("iki şart da doğru")

# bazı eşit değildir operatörü <>
# if 3 >= 2 and 3 <= 4 and 3 < and 3!= 4 :
#     print("Tüm şartlar doğru.")


# print(True and False)
# print(1 and 1)
# print(False and False)
# print(0 and 0 )
# print(True and False)
# print(1 and 0)
# print(False and True)
# print(0 and 1)

# print( True or False)
# print( False or True)
# print( False or False)

# if (True and False) or (False or True): 
# if ((True and False() or False) or True: 
# if True and ((False or False) or True): 

# if True and ((False or False) or True):   
#     print(" Çalışır mı?") 

# import math
# vize = int ( input ("vize sonucunu giriniz:") )

# final_için_gerekli_not = (50-0.4*vize) / 0.6

# print("Final için almanız gereken not :") , math.ceil(final_için_gerekli_not)

