import os


os.system("cls")
print("[Notif] Program ini dijalankan untuk menghasilkan sebuah diamond berdasarkan jumlah banyak range")
z = input("Tekan enter untuk melanjutkan: ")

os.system("cls")
print("====== [Status] Masuk ke dalam sistem =======")
a = 0
b = 1
c = 1
d = int(input("Masukkan range: "))
a = d//2


while c <= d:
    if d%2 !=0:
        if c <= (d//2):
            print("="*a + "*"*b + "="*a)
            a -=1
            b +=2 
        else:
            print("="*a + "*"*b + "="*a)
            a +=1
            b -=2
        c +=1
    else:
        print("Bilangan yang anda masukkan tidak termasuk bilangan ganjil\nCoba sekali lagi dan pastikan angka berikutnya bernilai ganjil")
        break


    
