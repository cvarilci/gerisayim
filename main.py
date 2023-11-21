import time

def gerisayim(t):
    while t > 0:
        print(t,end=" ")
        t -= 1
        time.sleep(1)
    print("geri sayim bitti")


print("Kaç saniyeden sonra geri sayım başlayacak. lütfen tam sayı olarak giriniz :")
saniye = input()
while not saniye.isdigit():
    print("Tam sayı girmediniz tekrar deneyin")
    saniye = input()
saniye = int(saniye)
gerisayim(saniye)
