from src.modelo.formando_model import Formando

formando1 = Formando("\nAna", 32)
print(formando1.apresentar())

formando2 = Formando("Jana", 32)
print(formando2.apresentar())

print(formando1.nome)
formando1.nome = "Alyson"
print(formando1.apresentar())


# Testar os diferentes atributos
print(Formando.categoria)
print(formando1.categoria)

# Encapsulamento
formando1.nome = "Maria" 
print(formando1.apresentar())

formando1.idade = 12
print(formando1.apresentar())