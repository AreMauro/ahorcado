from urllib.request import urlopen
from re import findall
from pprint import pprint
from secrets import choice


def ObtenerPalabrasEnBruto() -> list:

    link = "https://es.wiktionary.org/wiki/Ap%C3%A9ndice:1000_palabras_b%C3%A1sicas_en_espa%C3%B1ol"

    f = urlopen(link)

    myfile = f.read()

    titleElmemnts = findall("title=\"[a-z]{1,}\"", str(myfile))

    return titleElmemnts

def LimpiarPalabras(palabras: list) -> list:

    PalabrasLimpias = []

    for palabra in palabras:

        palabraLimpia = findall("\"[a-z]{1,}\"", str(palabra))

        palabraLimpia =  palabraLimpia[0].strip("\"")

        PalabrasLimpias.append(palabraLimpia)

    return PalabrasLimpias


def seleccionDePalabras(palabrasLimpias : list) -> set:

    palabrasElegidas = set()

    while(len(palabrasElegidas) < 100):

        palabrasElegidas.add(choice(palabrasLimpias))

    return palabrasElegidas

def cargarPalabrasPrihibidas() -> set[str]:

    palabrasProhibidas = set()

    with open("PalabrasProhibidas.txt", "r") as f:

        for palabra in f:

            palabrasProhibidas.add(palabra)
    return palabrasProhibidas

def obtenerPalabraSecreta() -> str:

    palabrasBrutas = ObtenerPalabrasEnBruto()

    palabrasLimpias = LimpiarPalabras(palabrasBrutas)

    palabrasSeleccionadas = seleccionDePalabras(palabrasLimpias)

    palabrasProhibidas = cargarPalabrasPrihibidas()

    palabraValida = False

    while palabraValida == False:

        palabraSeleccionada = choice([palabra for palabra in palabrasSeleccionadas])
        if palabraSeleccionada in palabrasProhibidas:
            palabraValida =  False
        
        else:
            palabraValida = True

    return palabraSeleccionada
