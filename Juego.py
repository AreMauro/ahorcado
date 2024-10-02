from Obtener_palabras import obtenerPalabraSecreta
from palabra import Palabra

class Juego():

    def __init__(self) -> None:

        try:
            self._PalabraSecreta = Palabra(obtenerPalabraSecreta())
        
        except:
            self._PalabraSecreta = Palabra(obtenerPalabraSecreta())
        
        

        self._Intentos = 5

        self._PalabraAdivinada = [""] * self._PalabraSecreta.ObtenerLongitud()

    @property
    def PalabraSecreta(self) -> Palabra:
        return self._PalabraSecreta
    
    @PalabraSecreta.setter
    def PalabraSecreta(self, nuevaPalabra: Palabra) -> None:
        
        if (isinstance(nuevaPalabra,Palabra)):

            self._PalabraSecreta = nuevaPalabra

    @property
    def Intentos(self) -> int:
        return self._Intentos
    
    @Intentos.setter
    def Intentos(self, nuevosIntentos: int) -> None:
        
        if (isinstance(nuevosIntentos,int)):

            self._Intentos = nuevosIntentos

    @property
    def PalabraAdivinada(self) -> int:
        return self._PalabraAdivinada
    
    @PalabraAdivinada.setter
    def PalabraAdivinada(self, nuevosPalabra: list) -> None:
        
        if (isinstance(nuevosPalabra,list)):

            self._PalabraAdivinada = nuevosPalabra

    def adivinarLetra(self, letra) -> bool:

        if len(letra) != 1:

            return False
        
        if letra in self.PalabraSecreta.Palabra:

            i = 0

            for letra_secreta in self.PalabraSecreta.Palabra:

                if letra_secreta == letra:
                    
                    if ( i <= self.PalabraSecreta.ObtenerLongitud()):

                        self.PalabraAdivinada[i] = letra
                
                        return True
                
                i += 1
        else:
            self.Intentos -= 1
            return False
    
    def obtenerPalabraAdivinada (self) -> str:

        return "".join(self.PalabraAdivinada)
    
    def obtenerIntentos(self) -> int:

        return self.Intentos
    
    def hasGanado(self) -> bool:

        return "" not in self.PalabraAdivinada
    
    def hasPerdido(self) -> bool:
        
        return self.Intentos == 0