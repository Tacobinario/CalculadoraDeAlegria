# Este script implementa una calculadora interactiva con interfaz gráfica creada en Python usando Tkinter.
# **Características principales:**
# - **Operaciones básicas:** Suma, resta, multiplicación y división, con soporte para números decimales.
# - **Botón "ALEGRAME":** Muestra un chiste matemático aleatorio para darle un toque divertido. Garantiza que no se repitan consecutivamente.
# - **Gestión de errores:** Maneja entradas inválidas y errores en las operaciones matemáticas.
# - **Borrado de caracteres:** Permite borrar el último carácter ingresado para correcciones rápidas.
# - **Hora y fecha dinámicas:** Muestra la hora local en formato 24 horas y la fecha actual en la interfaz. La información se actualiza automáticamente cada segundo.
# - **Proporción áurea inicial:** La ventana se inicia con un tamaño basado en la proporción áurea, simulando la forma vertical de un smartphone.
# - **Redimensionamiento dinámico:** Los botones y la interfaz se ajustan automáticamente al tamaño de la ventana, manteniendo proporciones y diseño.
# - **Estilo moderno y atractivo:** Diseño con colores personalizados, fuentes estilizadas y una disposición agradable y funcional.


import tkinter as tk
import random
from datetime import datetime

# Variables globales
hay_chiste = False
ultimo_chiste = None  # Variable para almacenar el último chiste mostrado

# Función para manejar las operaciones
def presionar_tecla(tecla):
    global hay_chiste
    # Si hay un chiste, eliminarlo primero
    if hay_chiste and tecla != "ALEGRAME":
        pantalla.delete("1.0", tk.END)
        hay_chiste = False

    # Operar la calculadora con normalidad
    if tecla == "=":
        try:
            # Evaluar la expresión matemática ingresada
            expresion = pantalla.get("1.0", tk.END).strip()  # Obtener to do el texto y eliminar espacios en blanco
            resultado = eval(expresion)
            pantalla.delete("1.0", tk.END)
            pantalla.insert(tk.END, str(resultado))
        except:
            pantalla.delete("1.0", tk.END)
            pantalla.insert(tk.END, "Error")
    elif tecla == "C":
        # Limpiar la pantalla
        pantalla.delete("1.0", tk.END)
    else:
        # Insertar la tecla presionada en la pantalla
        pantalla.insert(tk.END, tecla)

# Función para borrar el último carácter
def borrar_ultimo_caracter():
    global hay_chiste
    if hay_chiste:
        # Si hay un chiste, eliminar to do el texto
        pantalla.delete("1.0", tk.END)
        hay_chiste = False
    else:
        # Obtener el contenido actual de la pantalla
        contenido = pantalla.get("1.0", tk.END).strip()
        if contenido:  # Verificar que no esté vacío
            nuevo_contenido = contenido[:-1]  # Eliminar el último carácter
            pantalla.delete("1.0", tk.END)
            pantalla.insert(tk.END, nuevo_contenido)

# Función para mostrar chistes
def contar_chiste():
    global hay_chiste, ultimo_chiste
    chistes = [
        "¿Qué le dijo la calculadora al estudiante? ¡No me presiones tanto!",
        "¿Por qué los números no juegan a las escondidas? Porque siempre se encuentran en la ecuación.",
        "¿Qué le dijo el círculo a la línea recta? ¡Relájate, la vida no siempre es tan directa!",
        "¿Por qué los triángulos son malos amigos? Porque siempre están buscando ángulos.",
        "¿Qué pasa si divides la alegría entre cero? Te metes en un lío infinito.",
        "¿Por qué los números no pelean? Porque saben sumar.",
        "¿Qué hace un matemático perdido? Busca el punto de referencia.",
        "¿Por qué está triste el libro de matemáticas? ¡Porque tiene demasiados problemas!",
        "¿Qué dijo el 0 al 8? ¡Bonito cinturón!",
        "¿Por qué nadie confía en el álgebra? ¡Porque siempre está llena de incógnitas!"
    ]

    # Elegir un chiste que no sea igual al último mostrado
    chiste_nuevo = random.choice([chiste for chiste in chistes if chiste != ultimo_chiste])
    pantalla.delete("1.0", tk.END)
    pantalla.insert(tk.END, chiste_nuevo)
    ultimo_chiste = chiste_nuevo  # Actualizar el último chiste mostrado
    hay_chiste = True  # Indicar que hay un chiste en pantalla

# Función para actualizar la hora, día de la semana y fecha
def actualizar_fecha_hora():
    ahora = datetime.now()
    hora_actual = ahora.strftime("%H:%M:%S")  # Hora en formato 24 horas
    fecha_actual = ahora.strftime("%A, %d %B %Y")  # Día de la semana, número del día, mes y año
    etiqueta_hora_fecha.config(text=f"{hora_actual}\n{fecha_actual}")  # Mostrar hora y fecha juntas
    ventana.after(1000, actualizar_fecha_hora)  # Actualizar cada segundo

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Alegradora")
ventana.configure(bg="#f0f8ff")  # Fondo azul claro

# Establecer las dimensiones iniciales de la ventana basadas en la proporción áurea
ancho_inicial = 400  # Ancho inicial de la ventana
alto_inicial = int(ancho_inicial * 1.618)  # Alto basado en la proporción áurea
ventana.geometry(f"{ancho_inicial}x{alto_inicial}")  # Establecer dimensiones iniciales

# Configurar la ventana para que el diseño sea redimensionable
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)
ventana.rowconfigure(3, weight=1)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)
ventana.columnconfigure(3, weight=1)

# Crear el área de pantalla de la calculadora
pantalla = tk.Text(ventana, font=("Courier", 16, "bold"), borderwidth=2, relief="solid", height=3, wrap="word", bg="#e6f7ff", fg="#000")
pantalla.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# Crear el área para mostrar la hora y la fecha en la esquina inferior derecha
etiqueta_hora_fecha = tk.Label(ventana, text="", font=("Arial", 12), anchor="e", justify="right", bg="#f0f8ff", fg="#555")
etiqueta_hora_fecha.grid(row=6, column=2, columnspan=2, sticky="se", padx=10, pady=10)

# Definir los botones reorganizados
botones = [
    "1", "2", "3", "/",
    "4", "5", "6", "*",
    "7", "8", "9", "-",
    ".", "0", "=", "+"
]

# Crear los botones de números y operaciones
fila = 1
columna = 0
for boton in botones:
    b = tk.Button(ventana, text=boton, font=("Arial", 16, "bold"), command=lambda tecla=boton: presionar_tecla(tecla),
                  width=5, height=2, bg="#add8e6", fg="#000")
    b.grid(row=fila, column=columna, sticky="nsew", padx=5, pady=5)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Configurar redimensionamiento para los botones
for i in range(1, fila + 1):
    ventana.rowconfigure(i, weight=1)
for j in range(4):
    ventana.columnconfigure(j, weight=1)

# Agregar el botón "←" para borrar el último carácter
boton_borrar = tk.Button(ventana, text="←", font=("Arial", 16, "bold"), command=borrar_ultimo_caracter, bg="#ff9999", fg="#000")
boton_borrar.grid(row=fila, column=0, sticky="nsew", padx=5, pady=5)

# Agregar el botón "ALEGRAME"
columna += 1
boton_chiste = tk.Button(ventana, text="ALEGRAME", font=("Arial", 16, "bold"), command=contar_chiste, bg="#ffd700", fg="#000")
boton_chiste.grid(row=fila, column=1, columnspan=3, sticky="nsew", padx=5, pady=5)

# Iniciar la actualización de la hora y la fecha
actualizar_fecha_hora()

# Ejecutar la ventana principal
ventana.mainloop()
