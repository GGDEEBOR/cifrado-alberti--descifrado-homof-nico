import tkinter as tk
from tkinter import CENTER
import random
#Algoritmo basado en ejemplo de la documentacion recomendada por la profesora.
# Correspondencias usadas para evitar usar libreria random para alfabetos aleatorios.
correspondencia_1 = {
    'a': 'G', 'b': '5', 'c': 'X', 'd': 'C', 'e': '3', 'f': 'P', 'g': 'A', 'h': 'W',
    'i': 'K', 'j': 'N', 'k': 'E', 'l': '1', 'm': 'M', 'n': 'L', 'o': 'Z', 'p': 'T',
    'q': 'Q', 'r': '9', 's': 'I', 't': 'D', 'u': 'Y', 'v': 'O', 'w': 'R', 'x': 'J',
    'y': 'U', 'z': 'H'
}

correspondencia_2 = {
    'a': 'V', 'b': '5', 'c': 'X', 'd': 'C', 'e': 'F', 'f': 'P', 'g': 'A', 'h': 'W',
    'i': 'B', 'j': 'N', 'k': 'E', 'l': '1', 'm': 'M', 'n': 'L', 'o': 'S', 'p': 'T',
    'q': 'Q', 'r': '9', 's': 'I', 't': 'D', 'u': 'Y', 'v': 'O', 'w': 'R', 'x': 'J',
    'y': 'U', 'z': 'H'
}

correspondencia_3 = {
    'a': 'Z', 'b': '6', 'c': 'J', 'd': 'D', 'e': 'F', 'f': 'P', 'g': 'A', 'h': 'W',
    'i': 'B', 'j': 'N', 'k': 'E', '9': '1', 'm': 'L', 'n': 'L', 'o': 'S', 'p': 'T',
    'q': 'Q', 'r': '8', 's': 'I', 't': 'D', 'u': 'Y', 'v': 'O', 'w': 'R', 'x': 'J',
    'y': 'U', 'z': 'H'
}

def cifrar_texto(texto, correspondencia):
    texto_cifrado = ''
    for letra in texto:
        if letra in correspondencia:
            texto_cifrado += correspondencia[letra]
        else:
            texto_cifrado += letra
    return texto_cifrado

def descifrar_texto(texto_cifrado, correspondencia):
    texto_descifrado = ''
    correspondencia_inversa = {valor: clave for clave, valor in correspondencia.items()}
    for letra in texto_cifrado:
        if letra in correspondencia_inversa:
            texto_descifrado += correspondencia_inversa[letra]
        else:
            texto_descifrado += letra
    return texto_descifrado

def cifrar_descifrar():
    texto_plano = entrada_texto.get()
    
    #Seleccionar aleatoria de una correspondencia
    correspondencia_seleccionada = random.choice([correspondencia_1, correspondencia_2, correspondencia_3])
    
    texto_cifrado = cifrar_texto(texto_plano, correspondencia_seleccionada)
    texto_descifrado = descifrar_texto(texto_cifrado, correspondencia_seleccionada)
    
    resultado_cifrado.config(text=f'Texto cifrado: {texto_cifrado}')
    resultado_descifrado.config(text=f'Texto descifrado: {texto_descifrado}')

#ventana
ventana = tk.Tk()
ventana.title("Cifrado Homofónico")

#tamaño y centrar ventana
ancho_ventana = 400
alto_ventana = 200
x_ventana = (ventana.winfo_screenwidth() - ancho_ventana) // 2
y_ventana = (ventana.winfo_screenheight() - alto_ventana) // 2
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_ventana}+{y_ventana}")

#entrada de texto
etiqueta = tk.Label(ventana, text="Texto a cifrar/descifrar:")
etiqueta.pack()

entrada_texto = tk.Entry(ventana)
entrada_texto.pack()

#cifrar/descifrar(boton)
boton = tk.Button(ventana, text="Cifrar/Descifrar", command=cifrar_descifrar)
boton.pack()

#resultados
resultado_cifrado = tk.Label(ventana, text="")
resultado_cifrado.pack()

resultado_descifrado = tk.Label(ventana, text="")
resultado_descifrado.pack()

#center
ventana.withdraw()
ventana.update_idletasks()
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_ventana}+{y_ventana}")
ventana.deiconify()

ventana.mainloop()
