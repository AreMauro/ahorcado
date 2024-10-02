from Obtener_palabras import obtenerPalabraSecreta
from palabra import Palabra
from tkinter import Tk, Label, Button, Canvas, Entry, StringVar, Toplevel
from Juego import Juego
from string import ascii_lowercase, ascii_uppercase
from PIL import ImageTk, Image



class Interfaz():

    def __init__(self, juego: Juego) -> None:
        
        self.Juego = juego

        self.root = Tk()

        self.root.title("Juego del ahorcado")

        self.root.iconbitmap("Ahorcado.ico")

        self.root.update_idletasks()

        self.width = self.root.winfo_width()

        self. frm_width = self.root.winfo_rootx() - self.root.winfo_x()
        
        self.win_width = self.width + 2 * self.frm_width
        
        self.height = self.root.winfo_height()
        
        titlebar_height = self.root.winfo_rooty() - self.root.winfo_y()

        self.win_height = self.height + titlebar_height + self.frm_width
        
        self.x = self.root.winfo_screenwidth() // 2 - self.win_width // 2
        self.y = self.root.winfo_screenheight() // 2 - self.win_height // 2
        
        self.root.geometry('{}x{}+{}+{}'.format(self.width, self.height, self.x, self.y))
        
        self.root.deiconify()

        self.primer_frame = Canvas()

        self.primer_frame.pack(fill="both", expand=1)

        self.primer_frame.config()

        self.crearTablero(self.primer_frame)

    def crearTablero(self, frame : Canvas)->None:

        self.etiqueta_bienvenida = Label(frame, text="Bienvenido a el ahorcado")

        self.etiqueta_bienvenida.grid(column=6, row=0)

        self.Etiqueta_intentos = Label(frame, 
                                       text = f"Intentos {self.Juego.obtenerIntentos()}")

        self.Etiqueta_intentos.grid(column=6, row=1)

        self.Etiqueta_letra = Label (frame, text = "Escribe una letra: ")

        self.Etiqueta_letra.grid(column=6, row=2)

        self.vcmd = (self.root.register(self.validate), '%P')

        self.letraObtenida = StringVar()

        self.Entry_letra = Entry(frame, width=30, textvariable=self.letraObtenida,
                                    validate="key", validatecommand=self.vcmd)

        self.Entry_letra.grid(column=7, row=2)

        self.Entry_letra.bind('<KeyPress>', self.keyPress)

        self.Entry_letra.focus()

        self.button_probar = Button(frame, text="Probar letra", command=self.probarLetra)

        self.button_probar.grid(column=6, row = 3)

        self.mensaje_label = Label(frame, text= "")

        self.mensaje_label.grid(column=6, row=4)

        self.Guiones = [Label(frame, text="_",
                                font=("Arial", 24)) for _ in range(
                                                len(self.Juego.PalabraAdivinada) )]

        self.column_giones= 9

        row = 5

        for i in range(len(self.Juego.PalabraAdivinada)):

            self.Guiones[i].grid(column=self.column_giones, row = row)

            self.column_giones += 1

        self.letras_no_usadas = [Label(frame,text=letra) for letra in ascii_uppercase]

        column = 0

        row = 6
        
        for letra in self.letras_no_usadas:

            letra.grid(column=column, row= row)

            column += 1

            if column % 5 == 0:
                row += 1
                column = 0

        self.BotonSalida = Button(frame, text="Salida", command=self.root.destroy)

        self.BotonSalida.grid(row=row, column=5)

        self.myImage = Image.open("Imagenes/7.png")

        self.resized = self.myImage.resize((300,225))

        self.Image = ImageTk.PhotoImage(self.resized)


        self.LabelImage = Label(frame, 
                                image=self.Image)

        self.LabelImage.grid(column=self.column_giones, row =0, sticky="e", pady=20)





    def probarLetra(self):
      
        resultado = self.Juego.adivinarLetra(self.letraObtenida.get())

        for label in self.letras_no_usadas:
            
            if (label.cget("text").lower() == self.letraObtenida.get()):

                label.config(text="")


        if(resultado == True):
            
            for i in range(self.Juego.PalabraSecreta.ObtenerLongitud()):

                if(self.Juego.PalabraSecreta.Palabra[i] == self.letraObtenida.get()):

                    self.Guiones[i].config(text=""+self.letraObtenida.get())
                    self.Juego.PalabraAdivinada[i] = self.letraObtenida.get()
                    

        else:
            
            self.Etiqueta_intentos.config(text=f"Le quedan {self.Juego.obtenerIntentos()} intentos")

            self.myImage = Image.open(f"Imagenes/{self.Juego.obtenerIntentos() + 1}.png")

            self.resized = self.myImage.resize((300,225))

            self.Image = ImageTk.PhotoImage(self.resized)


            self.LabelImage = Label(self.primer_frame, 
                                    image=self.Image)

            self.LabelImage.grid(column=self.column_giones, row =0, sticky="e", pady=20)

        self.Entry_letra.delete(0, "end")

        if(self.Juego.hasPerdido() == True):

            self.Etiqueta_intentos.config(text="Ha perdido...")

            nuevaVentana = Toplevel(self.root)

            nuevaVentana.title("Perdedor...")

            perdedor_Label  = Label(nuevaVentana, text="Perdio", font=("Arial", 34))

            perdedor_Label.pack()

            salir = Button(nuevaVentana, text="Salir", command=nuevaVentana.destroy)

            respuesta_correcta = Label(nuevaVentana, 
                                       text=f"La respiuesta es: {self.Juego.PalabraSecreta.Palabra}")

            respuesta_correcta.pack()

            salir.pack()

            self.myImage = Image.open("Imagenes/1.png")

            self.resized = self.myImage.resize((300,225))

            self.Image = ImageTk.PhotoImage(self.resized)


            self.LabelImage = Label(self.primer_frame, 
                                    image=self.Image)

            self.LabelImage.grid(column=self.column_giones, row =0, sticky="e", pady=20)

            self.restart()


        if(self.Juego.hasGanado() == True):

            self.Etiqueta_intentos.config(text="Ganador...")

            nuevaVentana = Toplevel(self.root)

            nuevaVentana.title("Ganador...")

            perdedor_Label  = Label(nuevaVentana, text=f"Ha ganado y le quedan {self.Juego.obtenerIntentos()} intentos", 
                                    font=("Arial", 34))

            perdedor_Label.pack()

            salir = Button(nuevaVentana, text="Salir", command=nuevaVentana.destroy)

            salir.pack()

            self.restart()

    def keyPress(self, event):
        if event.char in ascii_lowercase :
            return event.char
        elif event.keysym not in ('Alt_r', 'Alt_L', 'F4', 'BackSpace', 'Return'):
            print (event.keysym)
            return 'break'

    def validate(self, P):
        if len(P) == 0:
            # empty Entry is ok
            return True
        elif len(P) == 1:
            # Entry with 1 digit is ok
            return True
        else:
            # Anything else, reject it
            return False

    def restart(self):
        
        self.primer_frame.destroy()

        self.primer_frame = Canvas(self.root)

        self.primer_frame.pack()

        self.Juego.Intentos = 5

        self.Juego.PalabraSecreta = Palabra(obtenerPalabraSecreta())

        self.Juego.PalabraAdivinada = [""] * self.Juego.PalabraSecreta.ObtenerLongitud()

        self.crearTablero(self.primer_frame)
       

    def Run(self):

        self.root.mainloop()