print("Manejo de funciones V1")
def Hola_mundo():
    print("Hola aqui estoy")

def Mensa(msg):
    print(msg)

def EscribeNC(Nombre, Apellido):
    print(Nombre ,Apellido)
    print(f"Tu nombre completo es {Nombre} {Apellido}")

def suma2numeros(n1,n2):
    s=n1+n2
    return f"La suma de {n1} + {n2} es de:",s
# llamando a la funcion
Hola_mundo()
Mensa("hola WhatsAPP") # llama a mensa con1 parametro
Mensa("El profe me sorprendio enviendo mensaje") # llama a mensa con un parametro
EscribeNC("Angel","Perez")
print("Funciones que regresan valores")
print(suma2numeros(7,3))
print(suma2numeros(15,45))


