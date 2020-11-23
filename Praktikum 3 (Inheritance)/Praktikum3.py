import time
import os
class Member:
   #representasi Member
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur


    def info(self):
        print('\n')
        print('=================')
        print("🌐 Cetak Info 🌐")
        print('=================')
        print ('Nama         : ' , self.nama,)
        print ('Umur         : ', self.umur)

# subclass
class Trainee(Member):
    #representasi Trainee
    def __init__(self, nama, umur, lamatrainee):
        Member.__init__(self, nama, umur)
        self.lamatrainee = lamatrainee


    def info(self):
        Member.info(self)
        print ('Lama Trainee : ' , self.lamatrainee)

# subclass
class Tim(Member):
    #representasi siswa
    def __init__(self, nama, umur, sebagai, lamatrainee):
        Member.__init__(self, nama, umur)
        self.sebagai = sebagai
        self.lamatrainee = lamatrainee

    def info(self):
        Member.info(self)
        print ('Sebagai      : ' , self.sebagai)
        print ('Lama Trainee : ' , self.lamatrainee)

print('\n')
print ('=======================')
print ('💪 Masukkan Trainee 💪')
print ('=======================')
time.sleep(2)
trainee = Trainee(str(input('Masukkan Nama : ')),
                  str(input('Masukkan Umur : ')),
                  str(input('Lama Trainee  : ')))

print('\n')
time.sleep(2)
print ('======================')
print ('👥 Masukkan Member 👥')
print ('======================')
tim = Tim(str(input('Masukkan Nama : ')),
          str(input('Masukkan Umur : ')),
          str(input('Sebagai       : ')),
          str(input('Lama Trainee  : ')))
time.sleep(2)
os.system('cls')
anggota = [trainee, tim]
for orang in anggota:
    orang.info()

print('\n')
