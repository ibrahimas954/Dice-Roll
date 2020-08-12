import random

def your():
    print("Sizin zarınız:")

def enemy():
    print("Rakibin zarı:")

def roll1():
    print("""              __________
             |          |
             |     @    |
             |          |
             |__________| 
             """)

def roll2():
    print("""             __________
            |          |
            |  @    @  |
            |          |
            |__________| 
             """)

def roll3():
    print("""             __________
            |          |
            |  @    @  |
            |     @    |
            |__________| 
             """)

def roll4():
    print("""             __________
            |          |
            |  @    @  |
            |  @    @  |
            |__________| 
             """)

def roll5():
    print("""             __________
            |  @       |
            |  @    @  |
            |  @    @  |
            |__________| 
             """)

def roll6():
    print("""             __________
            |  @    @  |
            |  @    @  |
            |  @    @  |
            |__________| 
             """)


def cizgi():                    #Görüntüyü biraz daha düzeltmek için şekil çizdirme.
   print("*-"*25+"*")

def sonuc(skor_oyuncu,skor_bilgisayar):
    if skor_oyuncu<skor_bilgisayar:
        print("--->KAYBETTİNİZ<---")
    elif skor_oyuncu>skor_bilgisayar:
        print("--->KAZANDINIZ<---")
    else:
        print("--->BERABERE<---")
#BAŞLANGIÇ

cizgi()
döngü=int(input("Hoşgeldin lütfen oynamak istediğin tur sayısını gir:"))
your_Score=0
computer_Score=0
cizgi()
#OYUN BAŞLIYOR
for i in range(döngü):
    print("Zarlar atılıyor...")
    your_Roll=random.randint(1,6)
    computer_Roll=random.randint(1,6)
    if computer_Roll == 1:
        enemy()
        roll1()
    elif computer_Roll == 2:
        enemy()
        roll2()
    elif computer_Roll == 3:
        enemy()
        roll3()
    elif computer_Roll == 4:
        enemy()
        roll4()
    elif computer_Roll == 5:
        enemy()
        roll5()
    elif computer_Roll == 6:
        enemy()
        roll6()

    if your_Roll == 1:
        your()
        roll1()
    elif your_Roll == 2:
        your()
        roll2()
    elif your_Roll == 3:
        your()
        roll3()
    elif your_Roll == 4:
        your()
        roll4()
    elif your_Roll == 5:
        your()
        roll5()
    elif your_Roll == 6:
        your()
        roll6()
    if your_Roll<computer_Roll:
        cizgi()
        print("Sonuç:Sizin zarınız--"+str(your_Roll)+"   "+"Rakibin zarı--"+str(computer_Roll)+" "+"Kaybettiniz!")
        computer_Score=computer_Score+1
    elif your_Roll>computer_Roll:
        cizgi()
        print("Sonuç:Sizin zarınız--"+str(your_Roll)+"   "+"Rakibin zarı--"+str(computer_Roll)+" "+"Kazandınız!")
        your_Score=your_Score+1
    else:
        cizgi()
        print("Sonuç:Sizin zarınız--"+str(your_Roll)+"   "+"Rakibin zarı--"+str(computer_Roll)+" "+"Berabere!")

cizgi()
print("Sizin skorunuz--->"+str(your_Score)+" "+"Bilgisayarın skoru--->"+str(computer_Score))
cizgi()
sonuc(your_Score,computer_Score)
