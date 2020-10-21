class Deret:

    def __init__(self, pilihan):
        self.__pilihan = pilihan
    
    def Getpilihan(self):
        batas = int(input("Masukkan Jumlah Kemunculan Deret (Beda Angka Genap) : "))
        for x in range (2,batas,1):
            if x % 2 == 0:
                print(x)
        array = []
        total = 0
        for x in range(2,batas,1):
            array.append(x)
            print("\nHasil nilai total adalah : {}".format(sum(array)))
            print("Hasil rata-rata adalah : {}".format(sum(array)/batas))


Deret1 = Deret ('')
Deret1.Getpilihan()