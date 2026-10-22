import unittest

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        resultado = 10 + 5
        self.assertEqual(resultado, 15)
