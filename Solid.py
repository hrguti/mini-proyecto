# importar los módulos
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import time
from tkinter import messagebox
from tkinter import PhotoImage

# ------------------------------------------------------------------------- FUNCIONES ----------------------------------------------------------------

# Clase para manejar el reloj y actualización de hora
class Reloj:
    def __init__(self, etiqueta_reloj, ventana):
        self.etiqueta_reloj = etiqueta_reloj
        self.ventana = ventana

    def actualizar(self):
        hora_actual = time.strftime("%H:%M:%S")
        self.etiqueta_reloj.config(text=hora_actual)
        self.ventana.after(1000, self.actualizar)
    

# Clase para manejar el registro de entrada/salida de empleados
class RegistroEntradaSalida:
    def __init__(self, combo_empleados, lista_registro, mensaje_error):
        self.combo_empleados = combo_empleados
        self.lista_registro = lista_registro
        self.mensaje_error = mensaje_error

    def registrar(self, accion):
        nombre_empleado = self.combo_empleados.get()
        if nombre_empleado:
            mensaje = f"{nombre_empleado} ha registrado su {accion} a las {time.strftime('%H:%M:%S')}"
            self.lista_registro.insert(tk.END, mensaje)
        else:
            self.mensaje_error.config(text="¡Seleccione un empleado!")

# Clase para manejar la gestión de empleados
class GestionEmpleados:
    def __init__(self, combo_empleados, entrada_nuevo_empleado):
        self.combo_empleados = combo_empleados
        self.entrada_nuevo_empleado = entrada_nuevo_empleado
        self.empleados = []

    def agregar(self, nuevo_empleado):
        if nuevo_empleado:
            self.empleados.append(nuevo_empleado)
            self.actualizar_lista()

    def actualizar_lista(self):
        self.combo_empleados['values'] = self.empleados
    
    # Clase para manejar la interfaz de usuario
class InterfazUsuario:
    def __init__(self, ventana_principal, empleados):
        self.ventana_principal = ventana_principal
        self.empleados = empleados

    def abrir_lista_empleados(self):
        ventana_lista = VentanaModal("Seleccionar Empleado", "300x200")
        lista_empleados = ListaEmpleados(ventana_lista, self.empleados)
        lista_empleados.mostrar()

    def eliminar_empleado(self):
        ventana_eliminar = VentanaModal("Eliminar Empleado", "300x300")
        eliminar = EliminarEmpleado(ventana_eliminar, self.empleados)
        eliminar.mostrar()

# Clase para manejar ventanas modales
class VentanaModal:
    def __init__(self, titulo, dimensiones):
        self.ventana = tk.Toplevel()
        self.ventana.title(titulo)
        self.ventana.geometry(dimensiones)

# Clase para mostrar y gestionar la lista de empleados
class ListaEmpleados:
    def __init__(self, ventana, empleados):
        self.ventana = ventana
        self.empleados = empleados

    def mostrar(self):
        # Lógica para mostrar la lista de empleados en la ventana modal

# Clase para eliminar un empleado
class EliminarEmpleado:
    def __init__(self, ventana, empleados):
        self.ventana = ventana
        self.empleados = empleados

    def mostrar(self):
        # Lógica para mostrar la lista de empleados a eliminar y confirmar la acción
        pass

# Clase para manejar la interfaz de usuario
class InterfazUsuario:
    def __init__(self, ventana):
        self.ventana = ventana
        self.menu = MenuApp(ventana)
        self.reloj = Reloj(ventana)
        self.gestor_empleados = GestorEmpleados(ventana)
        self.registro_entradas_salidas = RegistroEntradasSalidas(ventana)

    def iniciar_aplicacion(self):
        self.menu.mostrar()
        self.reloj.mostrar()
        self.gestor_empleados.mostrar()
        self.registro_entradas_salidas.mostrar()

# Clase para manejar el menú de la aplicación
class MenuApp:
    def __init__(self, ventana):
        self.menu_barra = tk.Menu(ventana)
        ventana.config(menu=self.menu_barra)
        self.menu_archivo = tk.Menu(self.menu_barra, tearoff=0)
        self.menu_barra.add_cascade(label="Archivo", menu=self.menu_archivo)
        self.menu_archivo.add_command(label="Salir", command=ventana.quit)

    def mostrar(self):
        pass  # Lógica para mostrar el menú en la interfaz

# Clase para manejar el reloj
class Reloj:
    def __init__(self, ventana):
        self.etiqueta_reloj = tk.Label(ventana, font=('Arial', 14))
        self.etiqueta_reloj.pack(pady=10)
        self.actualizar_reloj()

    def actualizar_reloj(self):
        pass  # Lógica para actualizar el reloj

# Clase para gestionar empleados
class GestorEmpleados:
    def __init__(self, ventana):
        self.label_empleado = tk.Label(ventana, text="Seleccione su nombre:")
        self.label_empleado.pack(pady=5)
        self.combo_empleados = ttk.Combobox(ventana, values=ListaEmpleados)
        self.combo_empleados.pack(pady=5)

    def mostrar(self):
        pass  # Lógica para mostrar la gestión de empleados

# Clase para gestionar el registro de entradas y salidas
class RegistroEntradasSalidas:
    def __init__(self, ventana):
        self.boton_entrada = tk.Button(ventana, text="Entrada", command=lambda: self.registrar_entrada_salida("entrada"))
        self.boton_entrada.pack(pady=5)
        self.boton_salida = tk.Button(ventana, text="Salida", command=lambda: self.registrar_entrada_salida("salida"))
        self.boton_salida.pack(pady=5)

    def registrar_entrada_salida(self, tipo):
        pass  # Lógica para registrar entradas y salidas
    
    # estoy ptobando que onda
