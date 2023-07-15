class Hogwarts_Student():
    house="Gryffindor"
    wand="mogno"
    nucleos="phoenix"
    
    
    
    
class Person(Hogwarts_Student):
    name="Harry Potter"
    age=11
    gender="male"
    
    
   
   
objeto = Person()
objeto_house=objeto.house
objeto_name=objeto.name
objeto_age=objeto.age
objeto_wand=objeto.wand
objeto_nucleos=objeto.nucleos
print(objeto_name)
print(objeto_house)
print(objeto_age)
print(objeto_wand)
print(objeto_nucleos)
#com self
class Professor():
    
    def __init__(self,name,house, function):
        self.name=name
        self.house=house
        self.function=function
   
        
             
class PhoenixOrder(Professor):
        pass
            
               
                
order_phoenix_member= Professor("Severus", "Stytherin","Spy")
        
#professor=Professor("Severus Snape","Slytherin")
print(order_phoenix_member.name)
print(order_phoenix_member.house)
print(order_phoenix_member.function)
