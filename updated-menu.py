menu = [
    # Çorbalar & Başlangıçlar
    "Mercimek Çorbası",
    "Ezogelin Çorbası",
    "Patates Kızartması",
    
    # Kebap & Pide & Lahmacun
    "Adana Kebap",
    "Urfa Kebap",
    "İskender",
    "Beyti Sarma",
    "Tavuk Şiş",
    "Lahmacun",
    "Kuşbaşılı Pide",
    "Kaşarlı Pide",
    
    # Fast Food
    "Hamburger",
    "Cheeseburger",
    "Karışık Pizza",
    "Margarita Pizza",
    
    # Tatlılar
    "Künefe",
    "Fıstıklı Baklava",
    "Sütlaç",
    "Sufle",
    
    # İçecekler
    "Cola",
    "Fanta",
    "Sprite",
    "Ayran",
    "Şalgam Suyu",
    "Su",
    "Soda"
]

# Menü yazdırmayı bir fonksiyon yaptım, istediğimiz zaman çağıralım
def menu_goster():
    print("\n------- MENÜ -------")
    for gosterilen_menu in menu:
        print(f"- {gosterilen_menu}")
    print("--------------------")

def urun_ekle():
     menu_goster() # Kullanıcıya menüyü gösterelim
     with open("secilen_menu.txt","a",encoding="utf-8") as file:
          
          # HATA DÜZELTİLDİ: capitalize() -> title()
          urun_sec = input("Ürün seçiniz: ").title() # <--- DEĞİŞTİ
          
          if urun_sec in menu:
               file.write(f"Seçtiğiniz ürünler: {urun_sec} \n")
               print(f"{urun_sec} sepete eklendi.")
          else:
               print("Hata: Menüde böyle bir ürün yok (Yazımı kontrol edin).")

def urun_cıkar():
    try:
        with open("secilen_menu.txt", "r", encoding="utf-8") as file:
            mevcut_sepet = file.readlines()
    except FileNotFoundError:
        print("Sepetiniz zaten boş.")
        return

    if not mevcut_sepet: # Dosya var ama içi boşsa
        print("Sepet boş, çıkarılacak ürün yok.")
        return

    # Kullanıcıya sepetini gösterelim ki ne sileceğini görsün
    print("\n--- Sepetiniz ---")
    for urun in mevcut_sepet:
        print(urun.strip())

    # HATA DÜZELTİLDİ: capitalize() -> title()
    silinecek_isim = input("Çıkarmak istediğiniz ürün: ").title() # <--- DEĞİŞTİ
    
    aranan_satir = f"Seçtiğiniz ürünler: {silinecek_isim} \n"

    if aranan_satir in mevcut_sepet:
        mevcut_sepet.remove(aranan_satir)
        
        with open("secilen_menu.txt", "w", encoding="utf-8") as file:
            file.writelines(mevcut_sepet)
            
        print(f"{silinecek_isim} sepetten çıkarıldı.")
    else:
        print("Bu ürün sepetinizde bulunamadı.")

def urun_kaydet():
     # HATA DÜZELTİLDİ: Dosya yoksa çökmesin diye try-except eklendi
     try: # <--- EKLENDİ
          with open("secilen_menu.txt", "r", encoding="utf-8") as file:
               urunler = file.readlines()
     except FileNotFoundError:
          print("Sepet boş, kaydedilecek ürün yok!")
          return

     if len(urunler) == 0:
          print("Kaydedilecek ürün yok!")
          return
     
     with open("kaydedilen_menu.txt", "a", encoding="utf-8") as file2:
          file2.write("\n--- Yeni Sipariş ---\n") # Okuması kolay olsun diye başlık
          file2.writelines(urunler)
          
          with open("secilen_menu.txt", "w", encoding="utf-8") as file:
               file.truncate(0)
     
     print("Sipariş başarıyla kaydedildi!")
     
def kaydedilen_menu_goster():
     print("\n--- GEÇMİŞ KAYITLI SİPARİŞLER ---")
     try:
          with open("kaydedilen_menu.txt", "r", encoding="utf-8") as file:
               icerik = file.read()
               if len(icerik) == 0:
                    print("Henüz kayıtlı sipariş yok.")
               else:
                    print(icerik)
     except FileNotFoundError:
          print("Henüz oluşturulmuş bir kayıt dosyası yok.")
     print("---------------------------------")


while True:
     islem = input(("\n------ İşlem Seçiniz -------\n1- Ürün ekle \n2- Ürün çıkar \n3- Kaydet \n4- Sipariş görüntüle\n5- Çıkış \n------------------------------------\nSeçiminiz: "))
     
     if islem == "1":
          urun_ekle()
     
     elif islem == "2":
          urun_cıkar()
     
     elif islem == "3":
          urun_kaydet()
     
     elif islem =="4":
          kaydedilen_menu_goster()

     elif islem == "5": # Çıkış için 5'i kontrol ediyoruz
          print("Çıkış yapılıyor...")
          break
     
     else:
          print("Geçersiz işlem!")
