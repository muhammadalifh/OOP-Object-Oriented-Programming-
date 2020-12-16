from abc import ABC,abstractmethod
import os
import time

class Robot(ABC):

	def __init__(self,set_nama,set_pemilik,set_tahun):
		self.__nama = set_nama
		self.__pemilik = set_pemilik
		self.__tahun = set_tahun

	@property
	@abstractmethod
	def Robots(self):
		pass

class DoraMini(Robot):
	
	def SayDora(self):
		pass

	@Robot.Robots.setter
	def Robots(self,input):
		self.__nama = input

	@Robots.getter
	def Robots(self):
		return self.__nama	

class Doraemon(DoraMini):
	
	def DoraEmon(self):
		print("🤡 Halo, Saya Dora Mini 🤡")
		print("Saya juga seperti Doraemon yang memiliki kantung ajaib")
		print("Nama           : " , self._Robot__nama)
		print("Pemilik        : " , self._Robot__pemilik)
		print("Tahun Terbit   : " , self._Robot__tahun)

	@DoraMini.Robots.setter
	def Robots(self,input):
		self.__nama = input

	@Robots.getter
	def Robots(self):
		return self.__nama	

print('\n')
print ('=======================')
print ('🤡 Masukkan DoraMini 🤡')
print ('=======================')
Emon = Doraemon(str(input('Masukkan Nama	 : ')),
					str(input("Masukkan Pemilik : ")),
					int(input('Masukkan Tahun   : ')))

os.system('cls')
time.sleep(2)	
Emon.DoraEmon()
