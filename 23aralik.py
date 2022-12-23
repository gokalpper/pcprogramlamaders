from pickle import NONE


class Araba :
    fiyatı  = NONE
    def __init__(self , f) -> None:
        self.fiyati = f
        # operator overloading
        def __add__(self,diger) : 
            return self . fiyati + diger.fiyati
        def __gt__(self,diger) :
            return self . fiyati > diger.fiyati


a = Araba(5000)
b = Araba(7500)

print( a + b )

if ( a > b) :
    print("Birinci araba ??? büyük")

    