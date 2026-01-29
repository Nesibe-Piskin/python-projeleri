kullanıcıHesabı = {
    "ad" : "kullanıcı adı",
    "soyad" : "kullanıcı soyadı",
    "numura" : 5555555555,
    "bakiye" : 10000,
    "ek hesap" : 5000
}

donguSayisi= int(input("Döngünün kaç kere çalışmasını istersizniz : "))
for x in range (donguSayisi):


    def paraCek (hesap):
        paraMiktar = float(input("Çekmek istediğiniz para miktarıı giriniz: "))

        if (hesap["bakiye"] >= paraMiktar):
            print("Hesabınızdan parayı çektiniz")
            yeniMiktar = hesap["bakiye"] - paraMiktar
            hesap.update({"bakiye" : yeniMiktar})
            print(f"Kalan bakiyeniz = {hesap['bakiye']}")
        
        else:
            toplam = hesap["bakiye"] + hesap["ek hesap"]
            if toplam >= paraMiktar:
                ekHesap = input("Ek hesaptan para çekmek ister misiniz : e/h ")
                if ekHesap == "e":
                    print ("Para çekme işlemi tamamlanmıştı.")
                    sonpara = paraMiktar - hesap["bakiye"]                
                    hesap.update({"bakiye":0})
                    print(f"kalan bakiyeniz = {hesap["bakiye"]}")
                    sonek =hesap["ek hesap"] - sonpara
                    hesap.update({"ek hesap":sonek})
                    print(f"kalan ek hesabınız = {hesap["ek hesap"]}")

                elif ekHesap == "h":
                    print("Girdiğiniz değer bakiyenizde yetersiz")

                else:
                    print("Girdiğiniz değerin burada sonucu yok")

            else:
                print("Çekmek istediğiniz para hesabınızda mevcut değil")
                
    paraCek(kullanıcıHesabı)