# test_rsa.py
import unittest
from RSA import criba, is_prime, generar_primo, inverso_modular, generar_llaves, encriptar, desencriptar

class TestRSA(unittest.TestCase):
    
    def test_criba(self):
        self.assertEqual(criba(10), [2, 3, 5, 7])
        self.assertEqual(criba(1), [])
    
    def test_is_prime(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
    
    def test_generar_primo(self):
        primo = generar_primo(10, 20)
        self.assertIn(primo, [11, 13, 17, 19])
    
    def test_inverso_modular(self):
        self.assertEqual(inverso_modular(3, 26), 9)
        self.assertEqual(inverso_modular(10, 17), 12)
        self.assertIsNone(inverso_modular(6, 9))  # No tiene inverso modular
    
    def test_generar_llaves(self):
        llaves = generar_llaves(100, 200)
        self.assertIsNotNone(llaves)
        clave_publica, clave_privada = llaves
        self.assertEqual(len(clave_publica), 2)
        self.assertEqual(len(clave_privada), 2)
    
    def test_encriptar_y_desencriptar(self):
        llave_publica, llave_privada = generar_llaves(100, 200)
        mensaje = "Hola Mundo"
        mensaje_encriptado = encriptar(mensaje, llave_publica)
        mensaje_desencriptado = desencriptar(mensaje_encriptado, llave_privada)
        self.assertEqual(mensaje, mensaje_desencriptado)
    
    def test_encriptar_numero(self):
        llave_publica, llave_privada = generar_llaves(100, 200)
        mensaje = "Hola123"
        mensaje_encriptado = encriptar(mensaje, llave_publica)
        mensaje_desencriptado = desencriptar(mensaje_encriptado, llave_privada)
        self.assertEqual(mensaje, mensaje_desencriptado)

if __name__ == "__main__":
    unittest.main()
