#herança em POO
#passando a classe Student() para a classe Person()
#a classe Person(), ira herdar os atributos e métodos da classe Student()
class Student():
    name= "jenifer"
    age = 26
    gender="female"
    def ola():
        print("ola")
    
    
class Person(Student):
    #pass, evita erros
    pass
    
p=Person()
print(p.name)
print(p.age)
print(p.gender)
