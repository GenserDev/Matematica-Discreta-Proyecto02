#       Proyecto Matematica Discreta 
#     Universidad del Valle de Guatemala 
#            Integrantes Grupo 8 
#             Genser Catalan 
#               Maria Giron 
#             Leonardo Dufrey 
#

def generarPrimo():
    print("Trabajar")

def encontrarMCD():
    print("Trabajar")

def inversoModular():
    e = int(input("Ingresa el numero entero que desees invertir: "))
    n = int(input("Ingresa el modulo en el que lo desees operar: "))

    print(f"Inversa modular de: ({e},{n})")

def generarLlaves():
    print("Trabajar")
    
def escriptacion():
    print("Trabajar")

def desencriptacion():
    print("Trabajar")

def menu():
    print("-----------------------------------------------")
    print("Bienvenido a este programa ( ͡❛ ω ͡❛)")
    while menu: 
        print("-----------------------------------------------")
        print("1. Generar primo")
        print("2. Encontrar MCD")
        print("3. Inverso modular")
        print("4. Generar llaves")
        print("5. Encriptar por metodo RSA")
        print("6. Desencriptar por metodo RSA")
        print("-----------------------------------------------")
        userElection = int(input("Ingresar opcion: "))
        print("-----------------------------------------------")

        match userElection:
            case 1: 
                generarPrimo()
            case 2:
                encontrarMCD()
            case 3: 
                inversoModular()
            case 4: 
                generarLlaves()
            case 5:
                escriptacion()
            case 6:
                desencriptacion()
            case _:
                print("Error: Opcion no valida")
                break

menu()