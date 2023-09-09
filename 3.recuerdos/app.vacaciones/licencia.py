import sys
from tkinter import *


class licencia:
    def __init__(self):
        self.ventana =Tk()
        self.ventana.title('TERMINOS Y CONDICIONES')
        self.ventana.resizable(False , False)
        self.ventana.geometry('600x360')

        self.fondo=PhotoImage(file='/home/kali/pychar/proyecto_python/app.vacaciones/imagenes/coca-cola-l.png')
        Label(self.ventana, image=self.fondo).place(x=300, y=220)

        #labels

        self.label1=Label(self.ventana , text='TERMINOS Y CONDICIONES')
        self.label1.config(font=('arial',13 , 'bold'))
        self.label1.place(x=180 , y=10)

        self.texto_condicones= Text(self.ventana, width=96, height=12)
        self.texto_condicones.config(font=('arial', 8), bg='white' , state=NORMAL)
        self.texto_condicones.insert(INSERT, '''       
    TÉRMINOS Y CONDICIONES"

    A.  PROHIBIDA SU VENTA O DISTRIBUCIÓN SIN AUTORIZACIÓN DE INFORMATICONFIG.
    B.  PROHIBIDA LA ALTERACIÓN DEL CÓDIGO FUENTE O DISEÑO DE LAS INTERFACES GRÁFICAS.
    C.  INFORMATICONFIG DE ERNESTO NO SE HACE RESPONSABLE DEL MAL USO DE ESTE SOFTWARE.

    LOS ACUERDOS LEGALES EXPUESTOS A CONTINUACION RIGEN EL USO QUE USTED HAGA DE ESTE SOFTWARE
    (INFORMATICONFIG), NO SE RESPONSABILIZA DEL USO QUE USTED"
    HAGA CON ESTE SOFTWARE Y SUS SERVICIOS. PARA ACEPTAR ESTOS TERMINOS HAGA CLIC EN (ACEPTO)"
    SI USTED NO ACEPTA ESTOS TERMINOS, HAGA CLIC EN (NO ACEPTO) Y NO UTILICE ESTE SOFTWARE."
         ''')
        self.texto_condicones.place(x=10 , y=40)
        self.texto_condicones.config(state=DISABLED)

        self.acepto=IntVar()
        self.check_acepto=Checkbutton(self.ventana, text='Acepto', font=('arial' , 12 , 'bold' ),
                                      command=self.acceptar)
        self.check_acepto.place(x=10 ,y=260)

        #botones

        self.continuar=Button(self.ventana, text='acepto', font=('arial' , 11 , 'bold'),\
                           width=7,height=2, bd=3, state=DISABLED , command=self.acceso)
        self.continuar.place(x=10 , y=300)
        self.cancelar=Button(self.ventana, text='cancelar' , font=('arial' , 11, 'bold'),\
                             width=7,height=2, bd=3,command=self.cancelar )
        self.cancelar.place(x=100 , y=300)


        self.ventana.mainloop()

    def acceptar(self):
        if (self.continuar['state']==DISABLED):
            self.continuar['state']=NORMAL
        else:
            self.continuar['state']=DISABLED

    def acceso(self):
        self.ventana.destroy()
        from principal import pricipal
        pricipal()

    def cancelar(self):
        sys.exit()


