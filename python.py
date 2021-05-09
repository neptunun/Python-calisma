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


# import random
# liste=list(range(1,10)) 
# random.shuffle(liste)
# print(liste)

# try:
#    x=int(input("x " ))
#    y=int(input("y "))
#    print(x/y)
# except ZeroDivisionError:
#    print("y  0 olamaz")   
# except ValueError:
#    print("x ve y sayısal değer olmalı")


# # try:
# #    x=int(input("x " ))
# #    y=int(input("y "))
# #    print(x/y)
# # except (ZeroDivisionError,ValueError):
# #    print("yanlış değer girdiniz")   


# while True:
#    try:
#       x=int(input("x " ))
#       y=int(input("y "))
#       print(x/y)
#    except (ZeroDivisionError,ValueError):
#       print("yanlış değer girdiniz")   
#    else:
#       break


# # while True:
# #    try:
# #       x=int(input("x "))
# #       y=int(input("y "))
# #       print(x/y)
# #    except Exception as e :
# #       print(e)
# #    else:
# #       break




# while True:
#    try:
#       x=int(input("x "))
#       y=int(input("y "))
#       print(x/y)
#    except Exception as e :
#       print(e)
#    else:
#       break
#    finally:
#       print("hata denetimi yapıldı")



# # message="hello world"
# # message=" ".join(message)
# # print(message)

# def func1(num1):
#    print(num1)
#    def func2(num1):
#           num2=num1+1
#           print(num1,num2)

#    func2(num1)

# func1(10)
   

# # def func1(number1):
# #        if number1==0:
# #         return 1
# #        return number1*func1(number1-1)   


# # print(func1(4))      



# file=open("text.txt","w")
# file.write("hello\n")
# file.close()

# # file=open("text.txt","a")
# # file.write("hello\n")
# # file.close()


# file=open("text.txt")
# context=file.read()
# print(context)

# context2=file.read()
# print(context2)



# # file=open("text.txt")
# # context=file.read()
# # print(context)

# # file=open("text.txt")
# # context2=file.read()
# # print(context2)


# file=open("text.txt")
# content=file.read(5)
# print(content)

# # file=open("text.txt")
# # context=file.read()
# # print(context)
# # file.seek(5)                    #   negatif olmaz !!!!
# # context2=file.read()
# # print(context2)


# import datetime

# print(datetime.datetime.now())
# print(datetime.datetime.now().second)

# # import re
# # str="python programlama kursu:python giriş"

# # print(re.search("python",str))



# import numpy as np
# np_array=np.array([1,2,3,4])
# print(type(np_array))

# np_multi=np_array.reshape(2,2)
# print(np_multi)


# result=np.zeros(10)
# result=np.ones(10)
# result=np.arange(1,10)
# result=np.arange(1,10,2)
# result=np.linspace(1,1,5)
# result=np.linspace(20,100,5)
# result=np.random.randint(1,10)
# result=np.random.rand(5)

# array=np.arange(50)
# array=array.reshape(5,10)
# print(array.sum(axis=1))   #satır toplamı
# print(array.sum(axis=0))   #sütun toplamı

# result=np.random.randint(1,10,2)
# result2=result.max()
# result2=result.min()
# result2=result.mean()
# result2=result.argmax()
# result2=result.argmin()




# print(result2)
# print(result)


# result=np.linspace(2,2,5)
# print(result)









# # import numpy as np

# # np_array=np.array([1,2,3,4])
# # result=np_array[1]
# # result=np_array[0:3]
# # result=np_array[: :-1]

# # np_array=np.array([[0,5,10],[15,20,25],[50,75,85]])
# # result=np_array[0]
# # result=np_array[0][0]
# # result=np_array[0,2]
# # result=np_array[:,2]
# # result=np_array[:,:2]

# # print(result)



# import numpy as np
# numbers1=np.random.randint(1,100,6)
# numbers2=np.random.randint(1,100,6)

# result=numbers1+numbers2
# result=numbers1+10
# result=numbers1-numbers2
# result=numbers1-10
# result=numbers1*numbers2
# result=numbers1*10
# result=numbers1/numbers2
# result=numbers1/10
# result=np.sin(numbers1)
# result=np.sqrt(numbers1)
# result=np.log(numbers1)

# numbers1=numbers1.reshape(2,3)
# numbers2=numbers2.reshape(2,3)
# result=np.vstack((numbers1,numbers2))
# result=np.hstack((numbers1,numbers2))

# result=numbers1>=50
# print(numbers1[result])



# print(numbers1)
# print(numbers2)
# print(result)



#Uygulama 19.5

# # import numpy as np

# # np_array=np.array([10,15,30,45,60])
# # np_array=np.arange(5,15)
# # np_array=np.arange(50,100,5)
# # np_array=np.zeros(10)
# # np_array=np.ones(10)
# # np_array=np.linspace(0,100,5)
# # np_array=np.random.randint(10,30,5)
# # np_array=np.random.randn(10)
# # np_array=np.random.randint(10,50,15)
# # np_array=np_array.reshape(3,5)

# # result=np_array.sum(1)
# # result=np_array.sum(0)
# # result=np_array.max()
# # result=np_array.min()
# # result=np_array.mean()
# # result=np_array.argmax()
# # result=np_array.argmin()
# # np_array=np.arange(10,20)
# # result=np_array[:3]
# # result=np_array[: :-1]

# # np_array=np.random.randint(10,50,15)
# # np_array=np_array.reshape(3,5)
# # result=np_array[0]
# # result=np_array[2,3]
# # result=np_array[:,0]
# # result=np.sqrt(np_array)
# # result=np_array**2

# # np_array=np.random.randint(-50,50,15)
# # np_array=np_array.reshape(3,5)
# # result=np_array>=0
# # print(np_array[result])



# # print(np_array)
# # print(result)


# import pandas as pd

# pandas_series=pd.Series()
# print(pandas_series)

# numbers=[10,20,33,40]
# pandas_series=pd.Series(numbers)


# letters=["a","b","c"]
# pandas_series=pd.Series(letters)


# liste=[20,30,"a","b"]
# pandas_series=pd.Series(liste)

# number=5
# pandas_series=pd.Series(number)
# pandas_series=pd.Series(number,[0 ,1, 2, 3])


# numbers=[10,20,30,40]
# pandas_series=pd.Series(numbers,["a","b","c","d"])

# dict={"a":20,"b":30,"c":40}
# pandas_series=pd.Series(dict)

# pandas_series=pd.Series([10,20,30,40],["a","b","c","d"])
# result=pandas_series.min()
# result=pandas_series.max()
# result=pandas_series.sum()
# result=pandas_series+50
# result=pandas_series>=20
# print(pandas_series[result])
# print(result)


# # import pandas as pd
# # s1=pd.Series([10,32,14])
# # s2=pd.Series([11,98,112])
# # data=dict(apple=s1,orange=s2)
# # df=pd.DataFrame(data)



# # df=pd.DataFrame([1,2,3,4])

# # df=pd.DataFrame([["ahmet",50],["ali",2]],columns=["name","grade"],index=[1,2])

# # dict={"name":["ahmet","ali"],"grade":[50,60]}
# # df=pd.DataFrame(dict)



# # dict_list=[{"name":"ahmet","grade":50},
# #          {"name":"ali","grade":60}]

# # df=pd.DataFrame(dict_list)

# # print(df)

# import pandas as pd
# df=pd.read_json("sample.json")
# print(df)


#--------------------------------------------------------------

# # import pandas as pd
# # import numpy as np

# # np_sample=np.random.randint(10,100,9).reshape(3,3)


# # df=pd.DataFrame(np_sample,["a","b","c"],["c1","c2","c3"])
# # result=df["c1"]               
# # result=df.loc["a"]            #loc[row]

# # result=df.loc[["a","b"]]      

# # result=df.loc[:,"c1"]            #loc[:,column]
# # result=df.loc["a","c1"]          #loc[row,column]
# # result=df.iloc[2]                #loc[row]

# # df["c4"]=pd.Series(np.random.randint(10,50,3),["a","b","c"])   #column ekleme


# # df.drop("c4",axis=1,inplace=True)   #inplace normalde false, false kullanımında kopyasını siliyor df'yi yazdırırsak
# #                                     # df c4 silinmeden önceki haliyle durur. true yaparsak direkt df üzerinde silme yapar.
# # print(df)
# # print(result)


# # deneme=np.random.randint(10,50,9).reshape(3,3)


#-------------------------------------------------------------------------

# import pandas as pd
# import numpy as np

# sample=np.random.randint(10,100,15).reshape(3,5)
# df=pd.DataFrame(sample,columns=["c1","c2","c3","c4","c5"])

# result=df.columns

# result=df.c1
# result=df["c1"]

# result=df.head()
# result=df.tail()

# result=df.head(10)
# result=df.tail(10)

# result=df[df<50]

# result=df[df<50]["c1"]

# result=df[df["c1"]<50]     #sadece sağlayan satırları getirir 

# result=df[(df["c1"]<50) & (df["c2"]>70)]       #and
# result=df[(df["c1"]<50) | (df["c2"]>70)]        #or

# result=df[(df["c1"]<50) | (df["c2"]>70)]["c1"]    
# result=df.query("c1<50 | c2>70")
    
# print(result)


#---------------------------------------------------------------
"""
import pandas as pd

personeller={
   "çalışan":["Ahmet Yılmaz","Can Ertürk","Hasan Korkmaz","Cenk Saymaz","Ali Turan","Rıza Ertürk","Mustafa Can"],
   "departman":["İnsan Kaynakları","Bilgi İşlem","Muhasebe","İnsan Kaynakları","Bilgi İşlem","Muhasebe","İnsan Kaynakları"],
   "yaş":[30,25,45,50,23,34,42],
   "semt":["Kadıköy","Tuzla","Maltepe","Tuzla","Kadıköy","Tuzla","Maltepe"],
   "maaş":[5000,3000,4000,3500,2750,6500,4500]
}

df=pd.DataFrame(personeller)
result=df

result=df["maaş"].sum()
result=df.groupby("departman").groups
result=df.groupby(["departman","semt"]).groups


semtler=df.groupby("semt")

# for name,group in semtler:
#        print(name)
#        print(group)


for group in df.groupby("departman"):
       
       #print(group)
       pass



result=df.groupby("semt").get_group("Kadıköy")

result=df.groupby("departman").get_group("Bilgi İşlem")

result=df.groupby("departman").sum()
result=df.groupby("departman").mean()
result=df.groupby("departman").max()
result=df.groupby("departman").min()

result=df.groupby("departman")["maaş"].sum()

result=df.groupby("semt")["çalışan"].count()


result=df.groupby("departman")["yaş"].max()["Muhasebe"]
print(result)




"""
#---------------------------------------------------------------------


# import pandas as pd
# import numpy as np

# data=np.random.randint(10,100,15).reshape(3,5)
# df=pd.DataFrame(data,[1,5,7],["c1","c2","c3","c4","c5"])

# df=df.reindex([1,2,3,4,5,6,7])
# result=df.drop("c1",axis=1)  #axis=1 satır
# result=df.drop(1,axis=0)   #axis=0 satır

# result=df.isnull()
# result=df.notnull()
# result=df[df.notnull()]

# result=df.dropna()
# result=df.dropna(axis=1)
# result=df.dropna(axis=1,how="all")

# result=df.fillna(value="heyo" )

# result=df.isnull().sum().sum()              #nan olan hücre sayısı

# result=df.size      #toplam hücre sayısı


# print(result)

#------------------------------------------------------


# import pandas as pd

# personeller={
#    "çalışan":["Ahmet Yılmaz","Can Ertürk","Hasan Korkmaz","Cenk Saymaz","Ali Turan","Rıza Ertürk","Mustafa Can"],
#    "departman":["İnsan Kaynakları","Bilgi İşlem","Muhasebe","İnsan Kaynakları","Bilgi İşlem","Muhasebe","İnsan Kaynakları"],
#    "yaş":[30,25,45,50,23,34,42],
#    "semt":["Kadıköy","Tuzla","Maltepe","Tuzla","Kadıköy","Tuzla","Maltepe"],
#    "maaş":[5000,3000,4000,3500,2750,6500,4500]
# }


# df=pd.DataFrame(personeller)
# df["çalışan"]=df["çalışan"].str.upper()
# df["çalışan"]=df["çalışan"].str.lower()



# print(df)


#------join işlemleri------------------------

# import pandas as pd

# customers={
#    "CustomerId":[1,2,3,4],
#    "FirstName":["Ahmet","Ali","Hasan","Canan"],
#    "LastName":["Yılmaz","Korkmaz","Çelik","Toprak"]
# }

# orders={
#    "OrderId":[10,11,12,13],
#    "CustomerId":[1,2,5,7],
#    "OrderDate":["2012","2011","2010","2015"]
# }

# df_customers=pd.DataFrame(customers,columns=["CustomerId","FirstName","LastName"])
# df_orders=pd.DataFrame(orders,columns=["OrderId","CustomerId","OrderDate"])

# print(df_customers)
# print(df_orders)

# result=pd.merge(df_customers,df_orders,how="inner")
# result=pd.merge(df_customers,df_orders,how="left")
# result=pd.merge(df_customers,df_orders,how="right")

# print(result)


#-----tablo birleştirme-------------------------

# import pandas as pd

# customersA={
#    "CustomerId":[1,2,3,4],
#    "FirstName":["Ahmet","Ali","Hasan","Canan"],
#    "LastName":["Yılmaz","Korkmaz","Çelik","Toprak"]
# }


# customersB={
#    "CustomerId":[5,6,7,8],
#    "FirstName":["Damla","Nazlı","Sedat","Melda"],
#    "LastName":["Korkut","Kaya","Çakır","Susmaz"]
# }

# df_customersa=pd.DataFrame(customersA,columns=["CustomerId","FirstName","LastName"])
# df_customersb=pd.DataFrame(customersB,columns=["CustomerId","FirstName","LastName"])

# result=pd.concat([df_customersa,df_customersb])
# print(result)


# result=pd.concat([df_customersa,df_customersb],axis=1)
# print(result)



#-----dataframe metotları---

# import pandas as pd
# import numpy as np

# data={
#    "Column1":[1,2,3,4],
#    "Column2":[10,10,20,43],
#    "Column3":["ab","ba","ac","ca"]
# }


# df=pd.DataFrame(data)

# result=df
# result=df.Column2.unique()
# result=df.columns
# result=len(df.columns)
# result=df.index
# result=len(df.index)
# result=df.info
 
# print(result)

# data={
#    "Ay":["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran"],
#    "Kategori":["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Giyim","Giyim","Giyim"],
#    "Gelir":[20,30,12,54,76,23,10,3]

# }

# df=pd.DataFrame(data)
# df=df.pivot_table(index="Ay",columns="Kategori",values="Gelir")

# print(df)

#-----matplotlib---------

import matplotlib.pyplot as plt
import numpy as np

# x=[1,2,3,4]
# plt.plot(x)
# plt.show()

# y=[1,4,9,16]
# plt.axis([0,6,0,20])
# plt.plot(x,y)
# plt.show()

# # x=np.linspace(0,2,100)
# # plt.plot(x,x,label="x=y",color="yellow")
# # plt.plot(x,x**2,label="x=y^2",color="red")
# # plt.plot(x,x**3,label="x=y^3")
# # plt.legend()
# # plt.show()


# x=np.linspace(0,2,100)
# fig,axs=plt.subplots(3)

# axs[0].plot(x,x)
# axs[1].plot(x,x**2)
# axs[2].plot(x,x**3)
# plt.show()

# # x=np.linspace(1,2,100)
# # fig,axs=plt.subplots(2,2)
# # axs[0,0].plot(x,x)
# # axs[0,1].plot(x,x**2)
# # axs[1,0].plot(x,x**3)
# # axs[1,1].plot(x,x**4)
# # plt.show()

#-----------------------------------------
# import matplotlib.pyplot as plt

# yil=[2010,2011,2012,2013,2014]

# oyuncu1=[7,2,9,1,6]
# oyuncu2=[9,4,1,7,4]
# oyuncu3=[10,3,11,8,7]


# # plt.plot([],[],color="y",label="oyuncu1")
# # plt.plot([],[],color="b",label="oyuncu2")
# # plt.plot([],[],color="g",label="oyuncu3")

# plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3,colors=["y","r","g"])
# plt.legend()
# plt.show()


#---------------------------------
# import matplotlib.pyplot as plt

# types=["a","b","c"]
# values=[10,13,14]

# # plt.pie(values,labels=types)
# plt.pie(values,labels=types,shadow=True,explode=(0.05,0.05,0.05),autopct="%1.1f%%")

# plt.show()

#------------------------------------

# import matplotlib.pyplot as plt
# plt.bar([1,2,3,4,5],[32,12,45,12,9])
# plt.show()























