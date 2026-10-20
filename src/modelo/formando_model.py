from src.sessoes import nome_valido, idade_valida


class Formando:

    # Atributo de classe

    categoria = "Categoria - Formando"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not nome_valido(valor):
            raise ValueError("Nome é inválido")
        self._nome = valor.strip()

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if not idade_valida(valor):
            raise ValueError("Idade inválida")
        self._idade = valor

    def apresentar(self):
        return f"{self.nome} - {self.idade} anos"
