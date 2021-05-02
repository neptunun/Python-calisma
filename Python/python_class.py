



# class Person:
       
#        address=" no information  "
       
#        def __init__(self,name,year):
#               self.name=name+"ada"
#               self.year=year
#               print(name)
#               print(self.name)



# pq=Person("Ada",1987)              
# print(f"console {pq.name} {pq.year} {pq.address}")




# # class Person:

# #     def __init__(self,name,surname,age):
# #         self.name=name
# #         self.surname=surname
# #         self.age=age


# #     def greeting(self,name):

# #         print(f"hello {self.name}")

# #     def introduce(self,name,surname,age):
# #         print(f"my name is {self.name} {self.surname}. My age is {self.age}")


# # p1=Person("ada","çınar","14")    
# # p1.greeting("ada")   
# # p1.introduce("ada","çınar","14")



# class Deneme:

#     pi=3.14


#     def __init__(self,r):

#         self.r=r

#     def alan(self):

#         alan=self.pi*self.r*self.r 
#         return alan  

#     def cevre(self):
#            cevre=2*self.pi*self.r
#            return cevre


# p1=Deneme(4)
# result=p1.alan()
# print(result)
# result=p1.cevre()          
# print(result)      



# # class Person:

# #     def __init__(self,name,surname,age):
# #         self.name=name
# #         self.surname=surname
# #         self.age=age


# #     def greeting(self):

# #         print(f"hello {self.name}")

# #     def introduce(self):
# #         print(f"my name is {self.name} {self.surname}. My age is {self.age}")


# #     def deneme(self):
# #          Person.introduce(self)
# #          Person.greeting(self)
# #          print("deneme")



# # p1=Person("ada","çınar","14")    
# # # p1.greeting()   
# # # p1.introduce()

# # p1.deneme()



# class Person:

#     def __init__(self):
#         print("ffrgr")


# class Student(Person):

#     pass


# p1=Student()




# # class Person:

# #     def __init__(self):
# #         print("ffrgr")


# # class Student(Person):

# #     def __init__(self):                              #burda Student için olan init Person'ın initini ezer. 
# #         print("ajsdfd")


# # p1=Student()
       
   
# class Person:

#     def __init__(self):
#         print("ffrgr")


# class Student(Person):

#     def __init__(self):  
#         Person.__init__(self)                            #bu şekilde ezme durumu ortadan kalktı
#         print("ajsdfd")


# p1=Student()





# # class Person:
    
# #     def __init__(self,name,surname):
# #         self.name=name
# #         self.surname=surname

# #     def greeting(self):
# #         print(f"hello {self.name}")



# # class Student(Person):

# #     def __init__(self,name,surname,number):  
# #         Person.__init__(self,name,surname)  
# #         self.number=number
# #         Person.greeting(self)      
        


# # p2=Person("dd","sss")
# # p2.greeting()

# # p1=Student("aa","bb",21)
# # print(p1.name)
# # print(p1.surname)
# # print(p1.number)

# # p1.greeting()








# class Animals():
#     def __init__(self,name,age,legs,breed,color):
#         self.name=name
#         self.age=age
#         self.legs=legs
#         self.breed=breed
#         self.color=color
    
#     def my_breed(self):
#         print(f"My breed is {self.breed}") 
 
# class Dogs(Animals):
#     def __init__(self,name,age,legs,breed,color,extra='loyal'):
#      Animals.__init__(self,name,age,legs,breed,color)

#      self.extra=extra
     

#     def who_am_I (self):
#         print(f"I am a dog.My name is {self.name}.People think that I'm {self.extra}.I'm {self.age} years old.I have {self.legs} legs")
#         print(f"My color is {self.color}")
#         print(Animals.my_breed(self))


# class Cats(Animals):
#     def __init__(self,name,age,legs,breed,color,extra='sleeper'):
#      Animals.__init__(self,name,age,legs,breed,color)

#      self.extra=extra

#     def who_am_I (self):
#         print(f"I am a cat.My name is {self.name}.People think that I'm {self.extra}.I'm {self.age} years old.I have {self.legs} legs")
#         print(f"My color is {self.color}")
#         print(Animals.my_breed(self))





# #Animals('Lucy',2,3,'terrier','gray').my_breed() 
# #Dogs('Lucy',2,3,'terrier','brown').who_am_I()
# #Cats("Kömür",4,4,'Angora','grey','crazy :)').who_am_I()

# Dogs('Lucy',2,3,'terrier','brown').my_breed()

# Cats("Kömür",4,4,'Angora','grey','crazy :)').my_breed()




# # class Question:
# #     def __init__(self,text,choices,answer):
# #         self.text=text
# #         self.choices=choices
# #         self.answer=answer

# #     def checkAnswer(self,answer):
# #         return self.answer==answer

# # q1=Question("soru 1",["a","b","c","d"],"a")
# # q2=Question("soru 2",["a","b","c","d"],"b") 



# # print(q1.checkAnswer("d"))




        