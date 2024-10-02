from re import findall

class Palabra():

    def __init__(self, palabra: str) -> None:

        
            
        if( len(palabra) >= 3 and len(palabra) >0
           and any([caracter.isspace() for caracter in palabra]) == False):

            self._Palabra = palabra

            self.Longitud = len(self._Palabra)
        
        else:
            raise Exception("La palabra debe medir 3 caracteres o mas y no debe contener espacios")

    @property
    def Palabra(self) -> str:

        return self._Palabra

    @Palabra.setter
    def Palabra(self, palabraNueva) ->None:

        whitespace = findall(r'[\s]', palabraNueva)

        if (not(palabraNueva == "") and any(whitespace) == False and len(palabraNueva) > 3):

            self._Palabra = palabraNueva


    def ObtenerLongitud(self) -> int:

        return self.Longitud - 1
    
    def __repr__(self) -> str:
        
        cls = self.__class__.__name__

        return f"{cls} = [{self.Palabra}; {self.Longitud}]"
