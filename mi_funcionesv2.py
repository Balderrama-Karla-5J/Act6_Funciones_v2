print("Ejemplos de funciones v2")
print("Balderrama Karla")
 # Lista > Tupla > Set > Diccionario

ingredientes =  ["Mantequilla", "Huevo", "Harina", "Leche", "Escencia de vainilla"]
pokemon = ("Pokemon B&W", "Pokemon: Alpha Zafiro", "Pokemon S&M")
libros = {"Sherlock Holmes","La cancion de aquiles", "Harry Potter", "Seras"}
gameboysp = {"Año de salida:": "2003" , "Color:":"Negro", "Tipo:":"Advance sp"}

 # Funciones
def recetario (receta):
    for i in ingredientes:
        print(i)

def sinjugar (juegos):
    for j in pokemon:
        print(j)

def leer(libro):
    for l in libros:
        print(l)

def vidjuego(game):
    for a ,b in gameboysp.items():
        print(a,b)

 # Llamar funciones 
print("-----Receta de hotcakes")
recetario(ingredientes)
print("-----Juegos de pokemon")
sinjugar(pokemon)
print("-----Libros por leer")
leer(libros)
print("-----Nintendo: Gameboy")
vidjuego(gameboysp)