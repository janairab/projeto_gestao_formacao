import unittest

from src.sessoes import nome_valido

class TestNomeValido(unittest.TestCase):

    def test_nome_normal(self):
        self.assertTrue(nome_valido("Ana"))

    def test_nome_espaco(self):
        self.assertTrue(nome_valido("  Ana  "))

    def test_nome_vazio(self):
        self.assertFalse(nome_valido(""))

    def test_nome_apenas_com_espaco(self):
        self.assertFalse(nome_valido("   "))