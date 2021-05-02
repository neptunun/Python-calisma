import datetime

# name=input("write your name ")
# surname=input("write your surname")
# name_surname=name+' '+surname
# gender=input("Write your gender  ")
# id=input("write your id  ")
# date_=input("Write your birtdate  ")
# address=input("Write your address  ")
# age=datetime.datetime.now().year-int(date_)


#print(dir(datetime))

# pi=3.14
# radius=float(input("enter radius value"))
# S=2*pi*radius
# A=pi*(radius**2)
# print(f"S:{S}  A:{A}")




# print(f'Dün "1984" eserini okudum')
# print(f"Dün '1984' eserini okudum")


# a="Hello World"
# a[6].upper
# print(a)

# b='abc'*3
# print(b)

#Listede birden farklı veri tipinde eleman bulunabilir 


# a=[1,True,'adana']
# a.append('bursa')
# print(a)

# result=a.count('adana')
# print(result)

# a.remove('adana')
# print(a)


#Listenin içindeki listenin elemanına ulaşım

# user1=['adana',12,'bursa']
# user2=[43,'ankara',99]
# users=[user1,user2]

# print(users[0][1])


# A=['Bmw','Mercedes','Opel','Mazda']
# print(len(A))
# print(A[0])
# print(A[len(A)-1])
# print(A[len(A)-1], A[0] )

# A[3]='Toyota'
# print(A)
# print(A.count('Mercedes'))

# print(A[-2])

# print(A[:3])

# A[2:4]=['Toyota','Renault']
# print(A)

# A.append('Audi')
# A.append('Nissan')
# print(A)


# A.pop(len(A)-1)
# print(A)

# A.reverse()
# print(A)



# names=['Ali','Yağmur','Hakan','Deniz']
# years=[1998,2000,1998,1987]

# names.append('Cenk')
# print(names)

# names.insert(0,'Sena')
# print(names)

# print(names.index('Deniz'))

# names.remove('Deniz')
# print(names)

# print('Ali' in names)

# names.reverse()
# print(names)

# names.sort()
# print(names)

# years.sort()
# years.reverse()
# print(years)

# str_="Chevrolet,Dacia"
# str_.split()
# print(str_)

# print(max(years))
# print(min(years))

# print(years.count(1998))

# years.clear()

# print(years)

# liste=[]


# for i in range(0,3):

#   a=input("deger girin")
#   liste.append(a)


# print(liste)


# ogrenciler={
#  '120':{
#      'ad':'Ali',
#      'soyad':'Yılmaz',
#      'telefon':'532 000 00 01'
#  },
#   '125':{
#      'ad':'Can',
#      'soyad':'Korkmaz',
#      'telefon':'532 000 00 02'
#  },
#  '128':{
#      'ad':'Volkan',
#      'soyad':'Yükselen',
#      'telefon':'532 000 00 03'
#  }

# }
# print(ogrenciler)

# number=input("write number")
# name=input("write name")
# surname=input("write surname")
# tel=input("write tel number")

# ogrenciler.update({
#     number:{
#       'ad':name,
#       'soyad':surname,
#       'telefon':tel
# }
# })

# print(ogrenciler)


 #atama,bool 
# x,y,z=1,2,"adana"
# print(x,y,z)


# values=1,2,3,4,6
# x,y,*z=values
# print(x,y,z)

# x,y,z=1,2,3

# result=x<y
# print(result)

# result=x>y
# print(result)

# result=x!=y
# print(result)

# result=x==y
# print(result)


#mod ile döngü


# while True:
    
#         islem=int(input("çift ya da tek olduğu kontrol edilecek sayıyı girin "))

#         if (islem)%2==0:
#             print(f"{islem} çift")
#         elif (islem)%2==1:
#             print(f"{islem} tek")   


# sayi=11

# result=sayi<11 and sayi>0
# print(result)


# result=sayi>11 or sayi>0
# print(result)
   
   #4.6 uygulama

#1 sayi=float(input("Sayı giriniz "))
# if sayi<100 and sayi>0:
#     print("sayi 0 ile 100 arasında")
# elif sayi<=0:
#     print("Sayi 0'dan küçük ya da eşit ")    
# else:
#     print("Sayi 100den büyük ya da eşit")    


# 2
# sayi=int(input("Sayı giriniz "))
# if sayi>0 and sayi%2==0:
#     print("sayi pozitif ve çift")    
# else:
#     print("durum sağlanmadı")    

#3

# email="123@gmail.com"
# sifre="123"

# email_deneme=input("email girin")
# sifre_deneme=input("şifre giriniz")

# if email_deneme==email and sifre_deneme==sifre:
#     print("giriş yapılıyor")
# elif email_deneme!=email and sifre_deneme==sifre:
#     print("email yanlış")
# elif email_deneme==email and sifre_deneme!=sifre:
#     print("şifre yanlış")
# else:
#     print("şifre ve email yanlış")


# liste=[]
# for i in range(0,3):
#     sayi=float(input("sayi giriniz"))
#     liste.append(sayi)

# if liste[0]<liste[1] and liste[0]<liste[2]:
#     print(f"{liste[0]} en küçük eleman")

# if liste[1]<liste[0] and liste[1]<liste[2]:
#     print(f"{liste[1]} en küçük eleman")

# if liste[2]<liste[0] and liste[2]<liste[1]:
#     print(f"{liste[2]} en küçük eleman")    


# x=y=[1,2,3]
# z=[1,2,3]

# print(x is y)
# print(x is z)
# print(x is not y)
# print(x is not z)

# x.append(4)
# print(x)
# print(y)
# print(z)

# meyveler=['muz','elma']
# print('muz' in meyveler)


# name=input("İsminizi giriniz ")
# age=int(input("Yaşınızı giriniz"))
# degree=input("Eğitim durumunuzu giriniz (ilkokul,lise,üniversite")

# if age>=18:
#        if degree=='lise' or degree=='üniversite':
#               print("ehiyet alabilirsin")

#        else:
#           print("eğitim durumundan dolayı ehliyet alamazsınız")    
# else:
#        print("yaşınızdan dolayı ehilet alamazsınız")

# toplam=0
# for i in range(0,2):
#        sayi=float(input("not giriniz"))
#        toplam+=sayi


# ortalama=toplam/2

# if ortalama>0 and ortalama<24:
#        print("0")
# elif ortalama>25 and ortalama<44:
#        print("1")
# elif ortalama>45 and ortalama<54:
#        print("2")
# elif ortalama>55 and ortalama<69:
#        print("3")
# elif ortalama>70 and ortalama<84:
#        print("4")              
# elif ortalama>85 and ortalama<100:
#        print("5")


# sayi=float(input("sayi giriniz"))

# if sayi>0 and sayi<100:
#        print(f"{sayi}, 0 ile 100 arasında")
# else:
#    print(f"{sayi},0 ile 100 arasında değildir")       


# sayilar=[1,2,3,4,5,6]

# for a in sayilar:
#        print(a)



# for a in range(0,6):
#        sayilar[a]+=1

# print(sayilar)      


# tuple=(1,2,3,4,)

# for i in tuple:
#        print(i)

# list=[(1,2),(3,4)]

# for i in list:
#    print(i)

# for a,b in list:
#    print(a)   

# for a,b in list:
#        print(a,b)   


# for a,b in list:
#        print(b)   


# dict_={'k1':1,'k2':2}

# for i in dict_:
#    print(i)

# for i in dict_.keys():
#    print(i) 

# for i in dict_.values():
#    print(i)

# for a,b in dict_.items():
#        print(a,b)



# sayilar=[1,3,5,7,9,12,19,21]

# for i in sayilar:
#        if i%3==0:
#               print(i)

# toplam=0
# for i in sayilar:
#  toplam+=i
# print(toplam)

# liste=[]
# for i in sayilar:
#        if i%3==0:
#               i=i**2
#               liste.append(i)
# print(liste)
          



# sehirler=['kocaeli','istanbul','ankara','izmir','rize']

# for i in sehirler:
#        if len(i)<=5:
#               print(i)


# ürünler=[
#  {'name':'samsung s6','price':'3000'},
#  {'name':'samsung s7','price':'4000'},
#  {'name':'samsung s8','price':'5000'},
#  {'name':'samsung s9','price':'6000'},
#  {'name':'samsung s10','price':'7000'}
# ]
# toplam=0
# for i in ürünler:
#        toplam+=int(i['price'])
# print(toplam)       
   

# for i in ürünler:
#    if i['price']<='5000'  :
#           print(i)



users={}

# for i in range(0,2):
#        name=input("Enter your name ")
#        surname=input("Enter your surname ")
#        age=int(input("Enter your age "))
#        print(f"{i+1}. ok")

#        users.update({
#           i:
#           {"name":name,"surname":surname,"age":age}
          
#        })

# print(users)


# import math

# print(math.pow(2,3))



# saat=18
# sicaklik=35
# print(saat<16 or sicaklik>35)


# str="python güzel bir programlama dilidir"
# yeni=str.replace("python","c#").title()
# print(yeni)

# a=5
# b=7

# sonuc="{}+{}={}". format(a,b,a+b)
# print(sonuc)

# a="dfdfdgfdgd"
# print(a.find("g",6))



# sayilar=[1,3,5,7,9,12,19,21]
# x=0
# while x<len(sayilar):
#        print(sayilar[x])
#        x+=1


# baslangic=int(input("başlangıç değerini girin"))
# bitis=int(input("bitiş değerini girin"))       

# x=baslangic
# while x<bitis:
#       if sayilar[x]%2==1:
#           print(sayilar[x])
#       x+=1
   
# baslangic=int(input("başlangıç değerini girin"))
# bitis=int(input("bitiş değerini girin"))       
# x=baslangic

# while x<bitis:
#        if x%2==1:
#               print(x)
#        x+=1       



# x=100
# while x>=0:
#    print(x)
#    x-=1


# liste=[]

# x=0
# while x<5:
#       sayi=int(input("sayi giriniz"))
#       liste.append(sayi)
#       x+=1



# liste.sort()
# print(liste)   

# import random
# sayi=random.randint(1,100)
# hak=10

# while hak>=0:
#       deneme=int(input("sayi giriniz"))
#       if deneme<sayi:
#               print("daha büyük")
#       elif deneme>sayi:
#              print("daha küçük")
#       else:
#          print("tebrikler!!!") 
#          break
#       hak-=1         

# if hak==-1:
#  print(f" bilemediniz, sayi {sayi}")             

# def fonksiyon(a,b):
#        return a+b

# print(fonksiyon(10,5))

# sehirler=["ankara","istanbul"]
# sehirler1=sehirler[:]
# sehirler1.append("izmir")
# print(sehirler,sehirler1)



# def displayUser(args):
#        for key,value in args.items():
              
#               print(f"{key} {value}")


# user={"name":"Ada","surname":"Çınar"}
# displayUser(user)


# def fonk1(value,number):
       
#        for i in range(0,number):
#               print(value)



# value=input("Ekranda görmek istediğiniz kelimeyi yazın")
# number=int(input("Kaç kere görmek istiyorsanız sayı değerini girin"))
# fonk1(value,number)


# liste=[]

# def fonk2(*args):
       
#       for i in args:
             
#              liste.append(i)
#       return liste

# print(fonk2(1,3,2))    

# def fonk4(sayi):
#    liste=[]
#    for i in range(2,sayi+1):
#       if sayi%i==0:
#          liste.append(i)

#    return liste     

# print(fonk4(24))         



# def  square(a):
#        return a**2


# print(square(4))

# liste=[1,2,3,4,5]

# print(list(map(square,liste)))


# liste=[1,2,3,4]

# print (list(map(lambda num: num**2,liste )))







# x="value"        #global variable tanımlayarak fonksiyon içindeki değişkeni projenin her yerinde değiştirebiliriz. 

# def fonk():
#        global x
#        x="key"

# fonk()
# print(x)       


# import math

# print(math.factorial(5))
# print(help(math))
# print(dir(math))
# print(help(math.factorial))


# # import math as islem
# # print(islem.sqrt(16))


# from math import factorial,sqrt
# print(sqrt(25))


import random
liste=list(range(1,10)) 
random.shuffle(liste)
print(liste)


