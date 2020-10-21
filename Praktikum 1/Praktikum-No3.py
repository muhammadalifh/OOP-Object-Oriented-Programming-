import os
class Novel:
    
    def __init__(self, Judul, Nama_Pengarang, Tahun_Terbit, Deskripsi_Novel, Harga_Beli):
       #instance variable
       self.__judul = Judul
       self.__nama_penagarang = Nama_Pengarang
       self.__tahun_terbit = Tahun_Terbit
       self.__deskripsi_novel = Deskripsi_Novel
       self.__harga_beli = Harga_Beli
       self.__harga_jual = self.__harga_beli - 20/100 * self.__harga_beli 
   
    def GetJudul(self):
        return self.__judul

    def  GetNamaPengarang(self):
        return self.__nama_penagarang   

    def GetTahunTerbit(self):
        return self.__tahun_terbit

    def GetDeskripsi(self):
        return self.__deskripsi_novel

    def GetHargaBeli(self):
        return self.__harga_beli
    
    def GetHargaJual(self):
        if (self.__harga_beli >= 0):
            return self.__harga_jual
        

Novel1 = Novel(str(input('Masukkan Judul Novel     : '))
                    ,str(input('Masukkan Pengarang Novel : '))
                    ,int(input('Tahun Terbit Novel       : '))
                    ,str(input('Deskripsi Novel          : '))
                    ,int(input('Harga Beli Novel         : ')))
print("\n")
Novel2 = Novel(str(input('Masukkan Judul Novel     : '))
                    ,str(input('Masukkan Pengarang Novel : '))
                    ,int(input('Tahun Terbit Novel       : '))
                    ,str(input('Deskripsi Novel          : '))
                    ,int(input('Harga Beli Novel         : ')))
print("\n")
Novel3 = Novel(str(input('Masukkan Judul Novel     : '))
                    ,str(input('Masukkan Pengarang Novel : '))
                    ,int(input('Tahun Terbit Novel       : '))
                    ,str(input('Deskripsi Novel          : '))
                    ,int(input('Harga Beli Novel         : ')))
os.system('cls')
print("\n")
print("==============NOVEL (1)==============")
print('Judul Novel         : ', Novel1.GetJudul())
print('Pengarang           : ', Novel1.GetNamaPengarang())
print('Tahun Terbit        : ', Novel1.GetTahunTerbit())
print('Deskripsi Novel     : ', Novel1.GetDeskripsi())
print('Harga Beli          : ', Novel1.GetHargaBeli())
print('Harga Jual          : RP.', Novel1.GetHargaJual())
print('\n')

print("\n")
print("==============NOVEL (2)==============")
print('Judul Novel         : ', Novel2.GetJudul())
print('Pengarang           : ', Novel2.GetNamaPengarang())
print('Tahun Terbit        : ', Novel2.GetTahunTerbit())
print('Deskripsi Novel     : ', Novel2.GetDeskripsi())
print('Harga Beli          : ', Novel2.GetHargaBeli())
print('Harga Jual          : RP.', Novel2.GetHargaJual())
print('\n')

print("\n")
print("==============NOVEL (3)==============")
print('Judul Novel         : ', Novel3.GetJudul())
print('Pengarang           : ', Novel3.GetNamaPengarang())
print('Tahun Terbit        : ', Novel3.GetTahunTerbit())
print('Deskripsi Novel     : ', Novel3.GetDeskripsi())
print('Harga Beli          : ', Novel3.GetHargaBeli())
print('Harga Jual          : RP.', Novel3.GetHargaJual())
print('\n')

harga_total_beli =  Novel1.GetHargaBeli() +  Novel2.GetHargaBeli() +  Novel3.GetHargaBeli()
harga_total_jual =  Novel1.GetHargaJual() +  Novel2.GetHargaJual() +  Novel3.GetHargaJual()


print('Harga Total Beli Buku           : RP.', harga_total_beli)
print('Harga Total Jual Buku           : RP.', harga_total_jual)









