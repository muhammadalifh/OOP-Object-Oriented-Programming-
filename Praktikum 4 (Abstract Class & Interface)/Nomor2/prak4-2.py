from abc import ABC,abstractmethod
import os
import time

class Permainan(ABC):

	def __init__(self,set_nama,set_levelPemain,set_hit):
		self.__nama = set_nama
		self.__levelPemain = set_levelPemain
		self.__hit = set_hit
		self.level = self.__levelPemain
		self.skorhitArcade = self.__hit * 3 
		self.skormissArcade = self.__hit * 1
		self.jumlahskorArcade = self.skorhitArcade - self.skormissArcade
		self.jumlahskorStrategy = self.__hit * 5
	
	def Getnama(self): 	
		return self.__nama
	
	def Getlevel(self):
		return self.level

	def Getlevelpemain(self):
		if int(self.__levelPemain) > 1 and int(self.__levelPemain) < 20:
			print("Level Pemain    : Normal")
		elif int(self.__levelPemain) > 21 and int(self.__levelPemain) < 80:
			print("Level Pemain    : Medium")
		elif int(self.__levelPemain) > 81 and int(self.__levelPemain) < 100 and int(self.__levelPemain) == 100:
			print("Level Pemain    :  Hard")
		elif int(self.__levelPemain) < 1 or int(self.__levelPemain) > 100:
			print("Level Pemain    : Tidak Terdeteksi")

	@property
	@abstractmethod
	def PermainanMethod(self):
		pass

class Arcade(Permainan):

	def GethiArcade(self):
		print("Jumlah Hit skor : " , self.jumlahskorArcade)
			

	@Permainan.PermainanMethod.setter
	def PermainanMethod(self,input):
		self.__nama = input

	@PermainanMethod.getter
	def PermainanMethod(self):
		return self.__nama	

class Startegy(Permainan):

	def GethitStrategy(self):
		print("Jumlah Hit skor : " , self.jumlahskorStrategy)

	@Permainan.PermainanMethod.setter
	def PermainanMethod(self,input):
		self.__nama = input

	@PermainanMethod.getter
	def PermainanMethod(self):
		return self.__nama	

print('\n')
print ('===================================')
print ('          🤼‍♀️‍️ ARCADE 🤼‍♀️‍️')
print ('===================================')
Arcade1 = Arcade(str(input('Masukkan Nama	       : ')),
					int(input("Masukkan Level (1-100) : ")),
					int(input('Masukkan Hit           : ')))

print('\n')
print('\n')
print ('===================================')
print ('          ⛷️  Strategy ⛷️')
print ('===================================')
Startegy1 = Startegy(str(input('Masukkan Nama	       : ')),
					int(input("Masukkan Level (1-100) : ")),
					int(input('Masukkan Hit           : ')))
os.system('cls')
time.sleep(2)

print('\n')
print ('===================================')
print ('          🤼‍♀️‍️ ARCADE 🤼‍♀️‍️')
print ('===================================')
print('    Nama        : ', Arcade1.Getnama())
print('    Level       : ', Arcade1.Getlevel())
Arcade1.Getlevelpemain()
Arcade1.GethiArcade()
print('\n')

print ('===================================')
print ('          ⛷️  Strategy ⛷️')
print ('===================================')
print('    Nama        : ', Startegy1.Getnama())
print('    Level       : ', Startegy1.Getlevel())
Startegy1.Getlevelpemain()
Startegy1.GethitStrategy()
print('\n')