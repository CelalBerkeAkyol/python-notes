# bu uygulamanın amacı kişinin yatırmının ne kadar büyüyeceğini tahmin eden bir uygulama yaratmak 
'''
    Inputs : 
    yatirim_yapilacak_yil = paranın kaç sene sonra lazım olacağı 
    hedeflenen_büyüme_orani = yıllık olarak yatırımdan beklenen büyüme 
    ana_para = ilk başta yatırılan para 
    yatirilan_para = dönemlik para yatırma 
    yatirilan_para_degisim_orani = %10 gibi enflasyon oranında gibi 
    yatirilan_para_sikligi  = yılda bir ayda bir gibi 
    yatirilan_para_degisim_sikligi = yatırılan para ne kadar sürede artırılacak 
    enflasyon_orani 
'''

print("Merhaba yatırım hesaplayıcıya hoşgeldiniz \n  ")
ana_para =  float(input("Ne kadar ana paranız var ?")) 
hedeflenen_buyume_orani =   float(input(" Bir yılda portfoyünüzde yüzde  kaç büyüme bekliyorsunuz   ")) 
yatirim_yapilacak_yil = int(input(" Kaç sene boyunca yatırım yapmayı planlıyorsunuz    ")) 

devam_mi = int (input("Eğer düzenli olarak para eklemeyi düşünüyorsanız 1 e basınız "))
if(devam_mi != 1 ) : 
    son_para = ana_para *  ( ((hedeflenen_buyume_orani  / 100) + 1) ** yatirim_yapilacak_yil )
    print(f"Son paranız : {son_para:.2f} Tl")
    exit()
  
# paranın gelecekteki değeri düşülerek ilk baştaki para hesaplanabilir şimdilik es geçelim 
yatirilan_para_sikligi  =  float(input(" Yılda kaç ay boyunca para yatırmayı planlıyorsunuz  ")) 
yatirilan_para =  float(input(" Şu an ne kadar para yatırmayı düşünüyorsunuz  ")) 
yatirilan_para_degisim_orani =  float(input(" Yıllık hangi oranda yatırdığınz paranızı arttırmayı düşünüyorsunuz   ")) 

#bu seçilen yıl boyunca devam eder 
for yil in range(1, yatirim_yapilacak_yil + 1):
    
    yil_boyunca_yatirilan_para = yatirilan_para * yatirilan_para_sikligi
    ana_para += yil_boyunca_yatirilan_para
    ana_para *= (1 + hedeflenen_buyume_orani / 100)
    print(f"{yil}. yıl sonunda yatırılan toplam para: {yil_boyunca_yatirilan_para:.2f} TL, Toplam bakiye: {ana_para:.2f} TL")


    # bir sonraki sene işlemleri set ediliyor 
    yatirilan_para *= ((yatirilan_para_degisim_orani / 100) + 1)






