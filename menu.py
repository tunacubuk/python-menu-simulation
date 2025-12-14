menu = [
     "Pizza",
     "Adana Kebap",
     "Urfa Kebap",
     "Hamburger",
     "Cola",
     "Fanta",
     "Soda"
]

for gosterilen_menu in menu:
     print(gosterilen_menu)

def urun_ekle():
     with open("secilen_menu.txt","a",encoding="utf-8") as file:
          
          urun_sec = input("Ürün seçiniz: ").capitalize()
          if urun_sec in menu:
               file.write(f"Seçtiğiniz ürünler: {urun_sec} \n")
               
          
          
          else:
               print("Menüden ürün seçiniz")
               
def urun_cıkar():
     pass

def urun_kaydet():

     with open("secilen_menu.txt", "r", encoding="utf-8") as file:
          urunler = file.readlines()

     if len(urunler) == 0:
          print("Kaydedilecek ürün yok!")
          return
     
     with open("kaydedilen_menu.txt", "a", encoding="utf-8") as file2:
          file2.writelines(urunler)
          
          with open("secilen_menu.txt", "w", encoding="utf-8") as file:
               file.truncate(0)
     
     print("Sipariş başarıyla kaydedildi!")

          

while True:
     
     islem = input(("------ İşlem Seçiniz -------\n1- Ürün ekle \n2- Ürün çıkar \n3- Kaydet \n4- Çıkış \n------------------------------------\nSeçiminiz: "))
     
     if islem == "1":
          urun_ekle()
     
     elif islem == "2":
          pass
     
     elif islem == "3":
          urun_kaydet()

     else:
          break
     
