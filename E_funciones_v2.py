print("funciones creadas por el usuario")
print("---Lista---")
def Mi_lista():
    amigos=["Homero","Paty","Lety"]
    for nava in amigos:
        print(nava)
Mi_lista()
print("---Tupla---")
def Mi_tupla(): 
    amigos=("David Munoz Salazar","Emmanuel","Melgar Oropeza")
    for movi in amigos:
        print(movi)
Mi_tupla()
print("---Conjunto---")
def Mi_Conjunto():
    amigos={"David Martinez","Robert","ivana"}
    for movi in amigos:
        print(movi)
Mi_Conjunto()
print("--Diccionario---")
def Mi_Diccionario():
    estedicc={
        "Amigo 1" : "Johana",
        "Amigo 2" : "Ale",
        "Amigo 3" : "Sky"
    }

    for key, value in estedicc.items() :
        print(f"{key} = {value}")

Mi_Diccionario()
