#classe
class Jenifer:
    nome= "Jenifer"
    idade=26
    altura=1.55
    peso=50.00
    cor_olhos="verdes"
    cabelo="castanho escuro"
    apelido="JeyJey"
    nome_completo= "Jenifer Gonçalves da Silva"
    nacionalidade= "Brasileira"
    idioma_nativo= "Portugues"
    idioma_aprendido= "Ingles Japones Coreano Espanhol Alemão"
#objeto
objeto_nome=Jenifer()
objeto_idade=Jenifer()
objeto_altura=Jenifer()
objeto_peso=Jenifer()
objeto_olhos=Jenifer()
objeto_cabelo=Jenifer()
objeto_apelido=Jenifer()
objeto_nome_completo=Jenifer()
objeto_nacionalidade=Jenifer()
objeto_idioma_nativo=Jenifer()
objeto_idioma_aprendido=Jenifer()
#imprimindo na tela, acessando apenas um dos atributos da classe
print(objeto_nome.nome)
print(objeto_idade.idade)
print(objeto_altura.altura)
print(objeto_peso.peso)
print(objeto_olhos.cor_olhos)
print(objeto_cabelo.cabelo)
print(objeto_apelido.apelido)
print(objeto_nome_completo.nome_completo)
print(objeto_nacionalidade.nacionalidade)
print(objeto_idioma_nativo.idioma_nativo)
print(objeto_idioma_aprendido.idioma_aprendido)
#usando a funçao self
#self seria o constructor da clase
#em javascript
"""
class nome_da_classe={
    nome;
    idade;
    sexo;
    constructor(){
        this.nome=nome;
        this.idade=idade;
        this.sexo=sexo;
    }
}
"""
class Kuro:
    def __init__(self, name, age, eyes, hair, height,weight, full_name, nacionality, language, learned_language):
        self.name = name
        self.age = age
        self.eyes = eyes
        self.hair = hair
        self.height = height
        self.weight = weight
        self.full_name = full_name
        self.nacionality= nacionality
        self.language = language
        self.learned_language = learned_language

#instanciando em variaveis
kuro = Kuro("Kuro", 25, "violetas", "pretos", 1.85, 50.00, "Lucian Blake", "Ingles-Britanico", "Ingles", "Portugues Japones Coreano Espanhol Alemão Russo Dinamarques")

print(kuro.name)
print(kuro.age)
print(kuro.eyes)
print(kuro.hair)
print(kuro.height)
print(kuro.weight)
print(kuro.full_name)
print(kuro.nacionality)
print(kuro.language)
print(kuro.learned_language)
print(kuro.nacionality)

# usando imput com classe e objeto
class lawly:
    def __init__(self, name, age, eyes, hair, height,weight, full_name, nacionality, language, learned_language):
        self.name = name
        self.age = age
        self.eyes = eyes
        self.hair = hair
        self.height = height
        self.weight = weight
        self.full_name = full_name
        self.nacionality= nacionality
        self.language = language
        self.learned_language = learned_language


lawly = lawly("lawly", 18, "cinzas", "brancos", 1.65, 45.00, "Dimitri Zelinsky", "Romeno", "Romeno", "Portugues Japones Coreano Espanhol Alemão Russo Dinamarques")
name = input('enter your name: ')
age = input('enter your age: ')
print(lawly.name)
print(lawly.age)
