from Juego import Juego
from Interfaz import Interfaz

class Principal():

    def __init__(self) -> None:
        
        self.Juego = Juego()

        self.Interfaz = Interfaz(self.Juego)

    def iniciar_nuevo_juego (self):

        self.Interfaz.Run()

if __name__ == "__main__":

    principal = Principal()

    principal.iniciar_nuevo_juego()
