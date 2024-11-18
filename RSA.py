# Autores: Leonardo Dufrey Mejía Mejía, María José Girón Isidro, Genser Catalan 
# Fecha de creación: 2024-11-17
# Fecha de actualización: 2024-11-17
# Versión: 1.1
# Descripción: Este código utiliza RSA para encriptar y desencriptar las 

import random

# Función Criba de Eratóstenes
def criba(n):
    not_prime = set()
    primes = []
    for i in range(2, n + 1):
        if i not in not_prime:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                not_prime.add(j)
    return primes

# Función is_prime para verificar si un número es primo
def is_prime(n):
    if n < 2:
        return False
    prime_list = criba(int(n**0.5) + 1)
    for i in prime_list:
        if n % i == 0:
            return False
    return True

# Generar número primo en un rango
def generar_primo(rango_inferior, rango_superior):
    for _ in range(100):  # Máximo de intentos
        candidato = random.randint(rango_inferior, rango_superior)
        if is_prime(candidato):
            return candidato
    return None

# Máximo común divisor
def mcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

# Inverso modular utilizando el algoritmo extendido de Euclides
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

# Generar claves RSA
def generar_llaves(rango_inferior, rango_superior):
    for _ in range(100):  # Intentos
        p = generar_primo(rango_inferior, rango_superior)
        q = generar_primo(rango_inferior, rango_superior)
        if not p or not q or p == q:
            continue
        
        n = p * q
        phi_n = (p - 1) * (q - 1)
        
        e = random.randint(2, phi_n - 1)
        while mcd(e, phi_n) != 1:
            e = random.randint(2, phi_n - 1)
        
        d = inverso_modular(e, phi_n)
        if d is not None:
            return (e, n), (d, n)
    return None

# Encriptar mensaje (carácter individual o número)
def encriptar(mensaje, llave_publica):
    e, n = llave_publica
    if mensaje < 0 or mensaje >= n:
        raise ValueError("El mensaje debe ser un entero positivo menor que n.")
    return pow(mensaje, e, n)

# Desencriptar mensaje (carácter encriptado)
def desencriptar(mensaje_encriptado, llave_privada):
    d, n = llave_privada
    if mensaje_encriptado < 0 or mensaje_encriptado >= n:
        raise ValueError("El mensaje encriptado debe ser un entero positivo menor que n.")
    return pow(mensaje_encriptado, d, n)

# Función para encriptar texto completo
def encriptar_texto(texto, llave_publica):
    return [encriptar(ord(c), llave_publica) for c in texto]

# Función para desencriptar texto completo
def desencriptar_texto(texto_encriptado, llave_privada):
    return ''.join(chr(desencriptar(c, llave_privada)) for c in texto_encriptado)

# Pruebas del sistema RSA
def pruebas():
    print("Generando llaves RSA...")
    llaves = generar_llaves(100, 300)
    if not llaves:
        print("No se pudieron generar las llaves.")
        return
    
    llave_publica, llave_privada = llaves
    print(f"Clave Pública: {llave_publica}")
    print(f"Clave Privada: {llave_privada}")
    
    # Pedir al usuario que ingrese un mensaje
    mensaje = input("\nIngrese el mensaje a encriptar: ")
    print(f"Mensaje Original: {mensaje}")
    
    # Encriptar el mensaje
    mensaje_encriptado = encriptar_texto(mensaje, llave_publica)
    print(f"Mensaje Encriptado: {mensaje_encriptado}")
    
    # Desencriptar el mensaje
    mensaje_desencriptado = desencriptar_texto(mensaje_encriptado, llave_privada)
    print(f"Mensaje Desencriptado: {mensaje_desencriptado}")
    
    assert mensaje == mensaje_desencriptado, "Error en el proceso RSA."
    print("\n¡El sistema RSA funcionó correctamente!")

pruebas()
