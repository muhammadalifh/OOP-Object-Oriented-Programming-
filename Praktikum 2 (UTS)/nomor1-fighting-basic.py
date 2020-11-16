import time
class Hero:

	def __init__(self,name,health,attackHitPoint,attackKickPoint):
		self.name = name
		self.health = health
		self.attackHitPoint = attackHitPoint
		self.attackKickPoint = attackKickPoint

	
	def tendang(self, lawan):
		print(self.name + ' menendang 🦶 ' + lawan.name )
		lawan.ditendang(self, self.attackKickPoint)

	def ditendang(self, lawan, attacKickPoint_lawan):
		print(self.name + ' ditendang ' + lawan.name)
		attack_diterima = attacKickPoint_lawan
		print('Damage diterima : ' + str(attack_diterima))
		self.health -= attack_diterima
		print('Darah ' + self.name + ' tersisa: ' + str(self.health))


	def pukulan(self, lawan):
		print(self.name + ' memukul 🤜 ' + lawan.name )
		lawan.pukulanberturut(self, self.attackHitPoint)


	def pukulanberturut(self, lawan, attackPukulanberturut_lawan):
		while self.health != 60:
			print(self.name + ' dipukul oleh ' + lawan.name)
			attack_diterima = attackPukulanberturut_lawan
			print('Damage diterima : ' + str(attack_diterima))
			self.health -= attack_diterima
			print('Darah ' + self.name + ' tersisa: ' + str(self.health))
			print("\n")
			time.sleep(3)

	def sepak(self, lawan):
		print(self.name + ' menendang 🦶 ' + lawan.name )
		lawan.disepak(self, self.attackKickPoint)

	def disepak(self, lawan, attackSepakPoint_lawan):
		while self.health != 0:
			print(self.name + ' ditendang ' + lawan.name)
			attack_diterima = attackSepakPoint_lawan
			print('Damage diterima : ' + str(attack_diterima))
			self.health -= attack_diterima
			print('Darah ' + self.name + ' tersisa: ' + str(self.health))
			print("\n")
			time.sleep(3)
	
	def darahRaiden(self, lawan):
		print('Darah 🧙‍♂️ ' + self.name + ' tersisa: ' + str(self.health))
	
	def darahSubZero(self, lawan):
		print('Darah 🧟‍♂️ ' + self.name + ' tersisa: ' + str(self.health))

		

Raiden = Hero('Raiden',100,10,20)
SubZero = Hero('SubZero',100,5,25)


print("\n")
Raiden.darahRaiden(SubZero)
SubZero.darahSubZero(Raiden)
time.sleep(3)
print("\n")
Raiden.tendang(SubZero)
time.sleep(3)
print("\n")
SubZero.tendang(Raiden)
time.sleep(3)
print("\n")
SubZero.pukulan(Raiden)
time.sleep(3)
print("SubZero Memukul 3x Secara Beruntun")
time.sleep(3)
print("\n")
Raiden.sepak(SubZero)
time.sleep(3)
print("Raiden Menendang 4x Secara Beruntun")
print("\n")
time.sleep(3)
Raiden.darahRaiden(SubZero)
SubZero.darahSubZero(Raiden)
print("\n")
time.sleep(3)
print("🔥Pertandingan Dimenangkan Oleh 🧙‍♂️ Raiden🔥")
time.sleep(3)
print("\n")

