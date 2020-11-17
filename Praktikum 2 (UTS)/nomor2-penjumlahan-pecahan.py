import time
def gcd(a, b): 
    if (a == 0):  
        return b  
    return gcd(b % a, a)  

def lowest(HasilPembilang, HasilPenyebut):  
    common_factor = gcd(HasilPenyebut, HasilPembilang)  
    HasilPembilang = int(HasilPembilang / common_factor)  
    HasilPenyebut = int(HasilPenyebut / common_factor) 
    print(HasilPenyebut, "/", HasilPembilang) 
  
def addFraction(pembilang1, penyebut1, pembilang2, penyebut2):  
    HasilPembilang = gcd(penyebut1, penyebut2)    
    HasilPembilang = (penyebut1 * penyebut2) / HasilPembilang  
    HasilPenyebut = ((pembilang1) * (HasilPembilang / penyebut1) + 
            (pembilang2) * (HasilPembilang / penyebut2))  
    lowest(HasilPembilang, HasilPenyebut)  
  
print("\n")
print("=============================================")
print("💻 Program Penjumlahan 2 Bilangan Pecahan 💻")
print("=============================================")
time.sleep(3)
print("\n")
pembilang1 =  int(input("Masukkan Pembilang 1  : "))
penyebut1  =  int(input("Masukkan Penyebut  1  : "))  
pembilang2 =  int(input("Masukkan Pembilang 2  : "))
penyebut2  =  int(input("Masukkan Penyebut  2  : "))
print("\n")  
time.sleep(3)
print("================================")
print("💾 Hasil Perhitungan Program 💾") 
print("================================")
print(pembilang1,"/",penyebut1," ➕ ",pembilang2,"/",  
      penyebut2, "  = ", end = " ") 

addFraction(pembilang1, penyebut1, pembilang2, penyebut2) 
time.sleep(3)
print("\n")









