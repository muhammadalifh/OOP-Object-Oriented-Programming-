import os
class Bilangan:

    def __init__(self, PositifGenap, NegatifGenap, PositifGanjil, NegatifGanjil):
        self.__positif_genap = PositifGenap
        self.__negatif_genap = NegatifGenap
        self.__positif_ganjil = PositifGanjil
        self.__negatif_ganjil = NegatifGanjil
    
    def GetpositifGenap(self):
        if self.__positif_genap > 0:
            if self.__positif_genap % 2 == 0:
                print('Bilangan dibawah ini merupakan Positif Genap')
        else :
            print('Bilangan dibawah ini bukan Positif Genap')
        return self.__positif_genap
    
    def GetNegatifGenap(self):
        if self.__negatif_genap < 0:
            if self.__negatif_genap % 2 == 0:
                print('Bilangan dibawah ini merupakan Negatif Genap')
        else :
            print('Bilangan dibawah ini bukan Negatif Genap')
        return self.__negatif_genap 

    def GetPositifGanjil(self):
        if self.__positif_ganjil > 0:
            if self.__positif_ganjil % 2 != 0:
                print('Bilangan dibawah ini merupakan Positif Ganjil')
        else :
            print('Bilangan dibawah ini bukan Positif Ganjil')
        return self.__positif_ganjil 

    def GetNegatifGanjil(self):
        if self.__negatif_ganjil < 0:
            if self.__negatif_ganjil % 2 != 0:
                print('Bilangan dibawah ini merupakan Negatif Ganjil')
        else :
            print('Bilangan dibawah ini bukan Negatif Ganjil')
        return self.__negatif_ganjil 


Bilangan1 = Bilangan(int(input('Masukkan Bilangan Positif Genap  : ')),
                        int(input('Masukkan Bilangan Negatif Genap  : ')),
                        int(input('Masukkan Bilangan Positif Ganjil : ')),
                        int(input('Masukkan Bilangan Negatif Ganjil : ')))
os.system('cls')
print('\n')
print(Bilangan1.GetpositifGenap())
print(Bilangan1.GetNegatifGenap())
print(Bilangan1.GetPositifGanjil())
print(Bilangan1.GetNegatifGanjil())
print('\n')
