settings = open("settings.txt", "r")
crudeDir = settings.readline()
print(crudeDir)
reallyDir= crudeDir[crudeDir.find("=")+1:]
print(f"Geçerli Ayarlarınız:\n"
      "------------------------------\n"
      f"Şarkıların yükleneceği dizin={reallyDir}"
      "------------------------------\n"

      )

settings.close()
choose = int(input("Eğer Geçerli ayarları değiştirmek istiyorsanız bire tıklayın"))

if choose == 1:
    reset = open("settings.txt", "w")
    newDir = input("Şarkıların yükleneceği yeni yeri seçin")
    reset.write(f"dir={newDir}")
    reset.close()
else:
    print("Herhangi bir ayar yapılmadı")