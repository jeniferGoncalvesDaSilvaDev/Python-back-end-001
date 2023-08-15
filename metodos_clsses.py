import time
class Pessoa:
    ano_atual=2023
    passos=0

    def __init__(self, nome, idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso=peso
        self.altura=altura
    #criando um metodo
    def get_ano_atual(self):
       return self.ano_atual - self.idade
    def falar(self):
        print(f"Olá eu sou {self.nome}")
        return "Sistema iniciado..."
    def apresentar(self):
        print(f"Meu nome é {self.nome}")
        print(f"Eu tenho {self.idade} anos")
        print(f"Eu peso {self.peso} kg")
        print(f"Eu tenho {self.altura} metros de altura")
        return "Prazer em conhecer :)"
    def andar(self):
        for self.passos in range(0,10):
            self.passos+=1
          
            print(f"{self.nome} está andando {self.passos} vezes")
            time.sleep(1)
            
            
    def comer(self):
        print(f"{self.nome} está comendo")
        return "yummy yummy yummy yummy yummy"
    #metodo para a classe, nao para instancia
    @classmethod
    def comida_favorita(cls):
        return "Minha comida favorita é sushi"

pessoa=Pessoa("Jenifer",26,50.0,1.55)

print(pessoa.nome)

print(pessoa.idade)
print(pessoa.peso)

print(pessoa.altura)
falar=pessoa.falar()
print(falar)
anoNascimento = pessoa.get_ano_atual()
print(anoNascimento)
apresentar=pessoa.apresentar()

print(apresentar)
andar=pessoa.andar()
print(andar)


comer=pessoa.comer()

print(comer)

comida_favorita=pessoa.comida_favorita()

print(comida_favorita)



