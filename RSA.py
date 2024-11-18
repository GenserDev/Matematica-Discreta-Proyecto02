# Autores: Leonardo Dufrey Mejía Mejía, María José Girón Isidro, Genser Catalan 
# Fecha de creación: 2024-11-17
# Fecha de actualización: 2024-11-17
# Versión: 1.1
# Descripción: 


import random
import math 

# Descripción: Función Criba necesaria para la función isPrime. 
def criba(n):
    not_prime = set()
    primes = []
    for i in range(2, n + 1):
        if i not in not_prime:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                not_prime.add(j)
    return primes


# Descripción: Función isPrime, test de primalidad utilizando la criba de Eratóstenes, 
#              determinando si un entero positivo n es primo o no, código utilizados en DivisibilityFunctions para formativa. 
def is_prime(n):
    if n < 2:
        return False
    prime_list = criba(int(n**0.5) + 1)
    for i in prime_list:
        if n % i == 0:
            return False
    return True

# 1. Generar número primo en un rango, utiliza la función isPrime para los candidatos al numero primo
def generar_primo(rango_inferior, rango_superior):
    for x in range(100):  # Intentos para encontrar un primo
        candidato = random.randint(rango_inferior, rango_superior)
        if is_prime(candidato):
            return candidato
    return None  # Si no se encuentra un primo

# 2. Máximo Común Divisor
def mcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

# 3. Inverso Modular
def inverso_modular(e, n):
    t, nuevo_t = 0, 1
    r, nuevo_r = n, e
    while nuevo_r != 0:
        cociente = r // nuevo_r
        t, nuevo_t = nuevo_t, t - cociente * nuevo_t
        r, nuevo_r = nuevo_r, r - cociente * nuevo_r
    if r > 1:  # No hay inverso modular
        return None
    if t < 0:
        t += n
    return t

# 4. Generar Llaves
def generar_llaves(rango_inferior, rango_superior):
    # Intentar generar llaves hasta 100 veces
    for _ in range(100):
        p = generar_primo(rango_inferior, rango_superior)
        q = generar_primo(rango_inferior, rango_superior)
        
        if not p or not q or p == q:
            continue  # Intentar con nuevos números primos
        
        n = p * q
        phi_n = (p - 1) * (q - 1)
        
        # Generar e tal que gcd(e, phi_n) == 1
        e = random.randint(2, phi_n - 1)
        while mcd(e, phi_n) != 1:
            e = random.randint(2, phi_n - 1)
        
        # Generar inverso modular
        d = inverso_modular(e, phi_n)
        if d is not None:
            return (e, n), (d, n)
    return None# Si no se encuentran llaves válidas tras 100 intentos

# 5. Encriptar
def encriptar(mensaje, llave_publica):
    e, n = llave_publica
    if mensaje >= n:
        raise ValueError("El mensaje debe ser menor que n.")
    return pow(mensaje, e, n)

# 6. Desencriptar
def desencriptar(mensaje_encriptado, llave_privada):
    d, n = llave_privada
    return pow(mensaje_encriptado, d, n)

# 7. Pruebas
def pruebas():
    print("Generando llaves...")
    llave_publica, llave_privada = generar_llaves(100, 300)
    
    if not llave_publica or not llave_privada:
        print("Error al generar las llaves.")
        return
    
    print(f"Clave Pública: {llave_publica}")
    print(f"Clave Privada: {llave_privada}")
    
    mensajes = [42, 123, 99]  # Mensajes de prueba

    for mensaje in mensajes:
        print(f"\nMensaje Original: {mensaje}")
        mensaje_encriptado = encriptar(mensaje, llave_publica)
        print(f"Mensaje Encriptado: {mensaje_encriptado}")
        mensaje_desencriptado = desencriptar(mensaje_encriptado, llave_privada)
        print(f"Mensaje Desencriptado: {mensaje_desencriptado}")
        assert mensaje == mensaje_desencriptado, "Error en el proceso RSA."

pruebas()