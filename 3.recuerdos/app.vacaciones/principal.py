import sys
from tkinter import *
from tkinter import ttk, messagebox


class pricipal:
    def __init__(self):
        self.ventana= Tk()
        self.ventana.title('pantalla pricipal')
        self.ventana.resizable(False,False)
        self.ventana.geometry('600x635')
        self.ventana.config(bg='red')

#menu de obciones
        self.menubar1=Menu(self.ventana)
        self.ventana.config(menu=self.menubar1)
        self.opciones1=Menu(self.menubar1, tearoff=0)
        self.opciones2=Menu(self.menubar1, tearoff=0)
        self.menubar1.add_cascade(label='Obciones', menu=self.opciones1)
        self.opciones1.add_command(label='salir', command=self.salidad, font=('Arial' , 10, 'bold'))

        self.menubar1.add_cascade(label='acerca de..', menu=self.opciones2,)
        self.opciones2.add_command(label='info', command=self.acerca, font=('Arial', 10, 'bold'))

#imagen logo
        self.fondo = PhotoImage(file='/home/kali/pychar/proyecto_python/app.vacaciones/imagenes/coca-cola-p.png')
        Label(self.ventana, image=self.fondo, bg='red').place(x=0, y=0)

#label bienvenida
        self.l_bienvenida=Label(self.ventana, text='bienvenid@!')
        self.l_bienvenida.config(fg='white' , bg='red' ,font=('arial' , 20 , 'bold'))
        self.l_bienvenida.place(x=280 , y=20)

#label detalle
        self.l_bienvenida = Label(self.ventana, text='datos del trabajador para el calculo')
        self.l_bienvenida.config(fg='white', bg='red', font=('arial', 18, 'bold'))
        self.l_bienvenida.place(x=10, y=110)

     #label nombre completo

        self.l_nombre = Label(self.ventana, text='Nombre comleto')
        self.l_nombre.config(fg='white', bg='red', font=('arial', 11, 'bold'))
        self.l_nombre.place(x=10, y=160)

        self.datonombre=StringVar()
        self.e_nombre=Entry(self.ventana, bd=2 , bg='#eee8e8', fg='red', textvariable=self.datonombre)
        self.e_nombre.config(font=('arial' , 12 , 'bold') , width=22)
        self.e_nombre.place(x=10 , y=185)

#label apellido

        self.l_apellido = Label(self.ventana, text='apellido')
        self.l_apellido.config(fg='white', bg='red', font=('arial', 11, 'bold'))
        self.l_apellido.place(x=10, y=225)

        self.datoapa = StringVar()
        self.e_apellido = Entry(self.ventana, bd=2, bg='#eee8e8', fg='red', textvariable=self.datoapa)
        self.e_apellido.config(font=('arial', 12, 'bold'), width=22)
        self.e_apellido.place(x=10, y=250)

#slecionar depatamento

        self.l_departamento = Label(self.ventana, text='selecione departamento')
        self.l_departamento.config(fg='white', bg='red', font=('arial', 11, 'bold'))
        self.l_departamento.place(x=280, y=160)

        self.var_combo1=StringVar()
        self.op_combo=('', 'atencion al cliente' , 'departamento de logistica' , 'departamento de gerencia')
        self.combobox1=ttk.Combobox(self.ventana, state='readonly',
                                    width=22 , font=('andale Mono regular', 11 , 'bold'),
                                    textvariable=self.var_combo1 , values=self.op_combo)

        self.combobox1.current(0)
        self.combobox1.place(x=250 , y=185)

 #selecionar antiguedad

        self.l_antiguedad = Label(self.ventana, text='selecione antiguedad')
        self.l_antiguedad.config(fg='white', bg='red', font=('arial', 11, 'bold'))
        self.l_antiguedad.place(x=280, y=225)

        self.var_combo2=StringVar()
        self.op_combo2 = (' ', '7 o mas years', '1 year de servicio', '2-6 years de servicio')
        self.combobox2 = ttk.Combobox(self.ventana, state='readonly',
                                      width=22, font=('andale Mono regular', 11, 'bold'),
                                      textvariable=self.var_combo2, values=self.op_combo2)

        self.combobox2.current(0)
        self.combobox2.place(x=250, y=250)

        estilo=ttk.Style()
        estilo.theme_use('clam')
        estilo.configure("Tcombobox", backgrounds="red")

#label resultado

        self.l_resultado=Label(self.ventana, text='Resultado del calculo')
        self.l_resultado.config(fg='white', bg='red' , font=('arial' , 11 , 'bold'))
        self.l_resultado.place(x=250 , y=295)

        self.area_resultado=Text(self.ventana, width=35 , height=7)
        self.area_resultado.config(font=('arial',11,'bold'),bg='#eee8e8',
                                   fg='red', state=DISABLED)
        self.area_resultado.place(x=250 , y=320)




#label pie de interfaz

        self.l_footer = Label(self.ventana, text='©2023 the zazzi company ')
        self.l_footer.config(fg='white', bg='red', font=('arial', 10, 'bold'))
        self.l_footer.place(x=205, y=485)

#botonoes
        self.b_calcular=Button(self.ventana, text='Calcular', width=7 , height=2, command=self.control_datos)
        self.b_calcular.config(font=('arial', 12 , 'bold'), fg='white',bg='red',bd=4)
        self.b_calcular.place(x=130 , y=400)

        self.b_limpiar = Button(self.ventana, text='limpiar', width=7, height=2 , command=self.limpiar_campos)
        self.b_limpiar.config(font=('arial', 12, 'bold'), fg='white', bg='red', bd=4)
        self.b_limpiar.place(x=10, y=400)

        self.ventana.mainloop()

    def control_datos(self):
        if not self.datonombre.get() or not self.datoapa.get() \
                or self.var_combo1.get() == '' or self.var_combo2.get() == '':
            messagebox.showerror('AVISO', 'RELLENE TODOS LOS CAMPOS')
        else:
            self.area_resultado.config(state=NORMAL)
            self.area_resultado.delete("1.0" , "end")
            if self.var_combo1.get()=='atencion al cliente':
                if self.var_combo2.get()=='1 year de servicio':
                    self.area_resultado.insert(INSERT, self.datonombre.get()+' '+self.datoapa.get()+\
                        '\n departamento: ' + self.var_combo1.get()+\
                        '\n antiguedad: ' + self.var_combo2.get()+\
                        '\n\n RECIVE 14 DIAS DE VACACIONES')

                if self.var_combo2.get() == '2-6 years de servicio':
                    self.area_resultado.insert(INSERT,
                                               self.datonombre.get() + ' ' + self.datoapa.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antigüedad:' + self.var_combo2.get() + \
                                               '\n\n RECIBE 18 DIAS DE VACACIONES')

                if self.var_combo2.get() == '7 o mas years':
                    self.area_resultado.insert(INSERT,
                                               self.datonombre.get() + ' ' + self.datoapa.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antigüedad:' + self.var_combo2.get() + \
                                               '\n\n RECIBE 30 DIAS DE VACACIONES')

            if self.var_combo1.get()=='departamento de logistica':
                if self.var_combo2.get()=='1 year de servicio':
                    self.area_resultado.insert(INSERT, self.datonombre.get()+' '+self.datoapa.get()+\
                        '\n departamento: ' + self.var_combo1.get()+\
                        '\n antiguedad: ' + self.var_combo2.get()+\
                        '\n\n RECIVE 14 DIAS DE VACACIONES')

                if self.var_combo2.get() == '2-6 years de servicio':
                    self.area_resultado.insert(INSERT,
                                               self.datonombre.get() + ' ' + self.datoapa.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antigüedad:' + self.var_combo2.get() + \
                                               '\n\n RECIBE 18 DIAS DE VACACIONES')

                if self.var_combo2.get() == '7 o mas years':
                    self.area_resultado.insert(INSERT,
                                               self.datonombre.get() + ' ' + self.datoapa.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antigüedad:' + self.var_combo2.get() + \
                                               '\n\n RECIBE 30 DIAS DE VACACIONES')

            if self.var_combo1.get()=='departamento de gerencia':
                if self.var_combo2.get()=='1 year de servicio':
                    self.area_resultado.insert(INSERT, self.datonombre.get()+' '+self.datoapa.get()+\
                        '\n departamento: ' + self.var_combo1.get()+\
                        '\n antiguedad: ' + self.var_combo2.get()+\
                        '\n\n RECIVE 14 DIAS DE VACACIONES')

                if self.var_combo2.get() == '2-6 years de servicio':
                    self.area_resultado.insert(INSERT,
                                               self.datonombre.get() + ' ' + self.datoapa.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antigüedad:' + self.var_combo2.get() + \
                                               '\n\n RECIBE 18 DIAS DE VACACIONES')

                if self.var_combo2.get() == '7 o mas years':
                    self.area_resultado.insert(INSERT,
                                               self.datonombre.get() + ' ' + self.datoapa.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antigüedad:' + self.var_combo2.get() + \
                                               '\n\n RECIBE 30 DIAS DE VACACIONES')


    def acerca(self):
        messagebox.showinfo('Info', '''sista de control vacacional
        DESAROLLADO POR: JORGE ARMANDO ESCOBAR CORREA
        DERECHOS RESERVADOS''')

    def salidad(self):
        sys.exit()
    def limpiar_campos(self):
        self.datonombre.set('')
        self.datoapa.set('')
        self.var_combo1.set('')
        self.var_combo2.set('')
        self.area_resultado.configure(state=NORMAL)
        self.area_resultado.delete('1.0', END)
        self.area_resultado.configure(state=DISABLED)


pricipal()

