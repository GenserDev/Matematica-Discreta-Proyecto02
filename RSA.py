# Autores: Leonardo Dufrey Mejía Mejía, María José Girón Isidro, Genser Catalan 
# Fecha de creación: 2024-11-17
# Fecha de actualización: 2024-11-17
# Versión: 1.1
# Descripción: Este código utiliza RSA para encriptar y desencriptar los mensajes. 
# Referencias: 
# GeeksforGeeks. (2023, June 30). ord() function in Python. GeeksforGeeks. https://www.geeksforgeeks.org/ord-function-python/
# También se uso como referencia la entrega de la actividad formativa 5, usando criba e is_prime de ese trabajo.

import random

# Descripción: Función Criba, criba de Eratóstenes para encontrar números primos
#              menores o iguales a un numero positivo dado n. 
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
#              determinando si un entero positivo n es primo o no. 
def is_prime(n):
    if n < 2:
        return False
    prime_list = criba(int(n**0.5) + 1)
    for i in prime_list:
        if n % i == 0:
            return False
    return True

# Generar número primo en un rango por medio de candidatos a ser primos
def generar_primo(rango_inferior, rango_superior):
    for _ in range(100):  # Máximo de intentos
        candidato = random.randint(rango_inferior, rango_superior)
        if is_prime(candidato):
            return candidato
    #Si se supera el máximo de intentos, en este caso 100 se manda un None. 
    return None

# Máximo común divisor
def mcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

# Inverso modular utilizando el algoritmo extendido de Euclides
# Formula inverso modular e * t + n * s = mcd(e,n)
def inverso_modular(e, n):
    t, nuevo_t = 0, 1
    residuo, nuevo_r = n, e # Usamos r para representar los residuos 
    while nuevo_r != 0:
        cociente = residuo // nuevo_r
        t, nuevo_t = nuevo_t, t - cociente * nuevo_t
        residuo, nuevo_r = nuevo_r, residuo - cociente * nuevo_r
    if residuo > 1:  # No hay inverso modular
        return None
    if t < 0:
        t += n
    return t

# Generar claves RSA, pública y provada
def generar_llaves(rango_inferior, rango_superior):
    for _ in range(100):  # Intentos
        p = generar_primo(rango_inferior, rango_superior)
        q = generar_primo(rango_inferior, rango_superior)
        if not p or not q or p == q:
            continue 
        
        n = p * q
        #Función de Euler
        phi_n = (p - 1) * (q - 1)
        
        e = random.randint(2, phi_n - 1)
        #e debe ser coprimo, aquí utilizamos MCD para aseurar que sea coprimo con phi(n)
        while mcd(e, phi_n) != 1:
            e = random.randint(2, phi_n - 1)
        
        d = inverso_modular(e, phi_n)
        if d is not None:
            #Tupla con la clave pública y privada. 
            return (e, n), (d, n)
    return None

#Función para encriptar el mensaje usando el mensaje y la llave pública. 
def encriptar(mensaje, llave_publica):
    e, n = llave_publica

    # Convertir mensaje a lista de números si es texto
    if isinstance(mensaje, str):
        #Usamos ord para poder manejar las letras también en ASCII. 
        mensaje = [ord(c) for c in mensaje] 
    elif isinstance(mensaje, int):
        mensaje = [mensaje] 
    
    # Encriptar cada valor en la lista
    return [pow(m, e, n) for m in mensaje]

#Función para desencriptar el mensaje que se encripto usando RSA con ASCII y la llave privada. 
def desencriptar(mensaje_encriptado, llave_privada):
    d, n = llave_privada

    # Desencriptar cada valor en la lista
    mensaje_desencriptado = [pow(c, d, n) for c in mensaje_encriptado]

    # Verificar si es texto (todos los valores desencriptados son caracteres válidos)
    try:
        return ''.join(chr(m) for m in mensaje_desencriptado)
    except ValueError:
        # Si no es texto, devolver los números desencriptados
        return mensaje_desencriptado

# Pruebas del sistema RSA
def pruebas():
    print("Las llaves que se generaron son: ")
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
    mensaje_encriptado = encriptar(mensaje, llave_publica)
    print(f"Mensaje Encriptado: {mensaje_encriptado}")
    
    # Desencriptar el mensaje
    mensaje_desencriptado = desencriptar(mensaje_encriptado, llave_privada)
    print(f"Mensaje Desencriptado: {mensaje_desencriptado}")
    
    #Mensaje eroro. 
    assert mensaje == mensaje_desencriptado, "Error en el proceso RSA."
    print("\nEL RSA funciono")

pruebas()
