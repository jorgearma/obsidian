from tkinter import *
from tkinter import messagebox


class bienvenida:
    def __init__(self):
        self.ventana=Tk()
        self.ventana.title('acceso')
        self.ventana.resizable(False,False)
        self.ventana.geometry('350x450+800+300')
        self.ventana.configure(bg='red')


        self.fondo= PhotoImage(file='/home/kali/pychar/proyecto_python/app.vacaciones/imagenes/logo-coca.png')
        Label(self.ventana, image=self.fondo, bg='red').pack()

#labels
        self.Label1=Label(self.ventana, text='sistema de control vacacional')
        self.Label1.config(fg='white', bg='red', font=('arial',18,'italic'))
        self.Label1.place(x=10,y=140)

        self.Label2=Label(self.ventana, text='ingrese nombre')
        self.Label2.config(fg='white', bg='red', font=('arial', 12, 'bold'))
        self.Label2.place(x=50 , y=230)

        self.Label3=Label(self.ventana, text='©2023 the zazzi company')
        self.Label3.config(bg='red' , fg='white' , font=('arial',10,'bold'))
        self.Label3.place(x=70 , y=410)


#entry nombre de usuario

        self.dato1=StringVar()
        self.entry1=Entry(self.ventana, bd=2 , bg='#eee8e8', fg='red', textvariable=self.dato1)
        self.entry1.config(font=('arial', 12 , 'bold'), width=27)
        self.entry1.place(x=50 ,y=255)

# boton
        self.boton1 = Button(self.ventana, text='ingresar', bd=2, bg='white', fg='red')
        self.boton1.config(font=('arial', 14),width=12, command=self.acceso)
        self.boton1.place(x=100 , y=285)

        self.ventana.mainloop()

    def acceso(self):
        self.largo=self.dato1.get()
        if not self.dato1.get():
            messagebox.showerror('ATENCION' , 'DEBE COLOCAR NOMBRE DE USUARIO!!')
        elif len(self.largo)>0 and len(self.largo)<8:
            messagebox.showerror('ATENCION', 'EL NOMBRe DEBE DE SER MAS LARGO')
        else:
            self.ventana.destroy()
            from licencia import licencia
            licencia()



if __name__ == '__main__':
    ejecutar=bienvenida()

