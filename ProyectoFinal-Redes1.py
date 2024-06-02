class Transmisor:
    def __init__(self):
        self.Indicador = "10000001"
        self.ACK = False
        self.ENQ = False
        self.CTR = False
        self.DAT = False
        self.PPT = False
        self.LPT = False
        self.NUM = False
        self.informacion = ""
        self.frames = 1

    def enviar_mensaje(self, ACK, ENQ, CTR, DAT, PPT, LPT, informacion, receptor):
        self.ACK = ACK
        self.ENQ = ENQ
        self.CTR = CTR
        self.DAT = DAT
        self.PPT = PPT
        self.LPT = LPT
        
        # Dividir el mensaje en frames
        frame_size = len(informacion) // self.frames
        frames = [informacion[i:i+frame_size] for i in range(0, len(informacion), frame_size)]
        
        for i in range(self.frames):
            self.NUM = i + 1
            if i == self.frames - 1:
                self.LPT = True  # Última trama
            
            trama = {
                "Indicador": self.Indicador,
                "ACK": self.ACK,
                "ENQ": self.ENQ,
                "CTR": self.CTR,
                "DAT": self.DAT,
                "PPT": self.PPT,
                "LPT": self.LPT,
                "NUM": self.NUM,
                "Informacion": frames[i],
                "Indicador_final": self.Indicador
            }
            receptor.recibir_mensaje(trama)

class Receptor:
    def __init__(self):
        self.mensajes = []

    def recibir_mensaje(self, mensaje):
        if mensaje['PPT']:
            self.mensajes.append(mensaje)
            #self.procesar_mensaje(mensaje)
            self.enviar_ack(mensaje['NUM'])
        else:
            print("No hay permiso para transmitir")

    def procesar_mensaje(self, mensaje):
        # Extraer y mostrar información de la trama
        print("Mensaje recibido:")
        print(f"Indicador: {mensaje['Indicador']}")
        print(f"ACK: {mensaje['ACK']}")
        print(f"ENQ: {mensaje['ENQ']}")
        print(f"CTR: {mensaje['CTR']}")
        print(f"DAT: {mensaje['DAT']}")
        print(f"PPT: {mensaje['PPT']}")
        print(f"LPT: {mensaje['LPT']}")
        print(f"NUM: {mensaje['NUM']}")
        print(f"Informacion: {mensaje['Informacion']}")
        print(f"Indicador final: {mensaje['Indicador_final']}")
        print()

    def enviar_ack(self, num):
        # Enviar ACK al transmisor
        print(f"ACK enviado para la trama número: {num}")

    def mostrar_mensajes(self):
        print("Mensajes recibidos:")
        for mensaje in self.mensajes:
            print(mensaje)

# Crear instancias de Transmisor y Receptor
transmisor = Transmisor()
receptor = Receptor()

# Enviar un mensaje
transmisor.frames = 3  # Configurar número de frames
transmisor.enviar_mensaje(1, 1, 0, 1, 1, 0, "Hola como estas?", receptor)

# Mostrar los mensajes recibidos
receptor.mostrar_mensajes()

'''
import tkinter as tk
from tkinter import ttk

class Transmisor:
    def __init__(self):
        self.Indicador = "10000001"
        self.ACK = False
        self.ENQ = False
        self.CTR = False
        self.DAT = False
        self.PPT = False
        self.LPT = False
        self.NUM = False
        self.informacion = ""
        self.frames = 1

    def enviar_mensaje(self, ACK, ENQ, CTR, DAT, PPT, LPT, informacion, receptor):
        self.ACK = ACK
        self.ENQ = ENQ
        self.CTR = CTR
        self.DAT = DAT
        self.PPT = PPT
        self.LPT = LPT
        
        # Dividir el mensaje en frames
        frame_size = len(informacion) // self.frames
        frames = [informacion[i:i+frame_size] for i in range(0, len(informacion), frame_size)]
        
        for i in range(self.frames):
            self.NUM = i + 1
            if i == self.frames - 1:
                self.LPT = True  # Última trama
            
            trama = {
                "Indicador": self.Indicador,
                "ACK": self.ACK,
                "ENQ": self.ENQ,
                "CTR": self.CTR,
                "DAT": self.DAT,
                "PPT": self.PPT,
                "LPT": self.LPT,
                "NUM": self.NUM,
                "Informacion": frames[i],
                "Indicador_final": self.Indicador
            }
            receptor.recibir_mensaje(trama)

class Receptor:
    def __init__(self):
        self.mensajes = []
        self.mensaje_completo = ""

    def recibir_mensaje(self, mensaje):
        if mensaje['PPT']:
            self.mensajes.append(mensaje)
            self.procesar_mensaje(mensaje)
            self.enviar_ack(mensaje['NUM'])
        else:
            print("No hay permiso para transmitir")

    def procesar_mensaje(self, mensaje):
        self.mensaje_completo += mensaje['Informacion']
        # Actualizar la interfaz con el mensaje recibido
        recibidos_var.set(self.mensaje_completo)

    def enviar_ack(self, num):
        # Enviar ACK al transmisor
        print(f"ACK enviado para la trama número: {num}")

    def mostrar_mensajes(self):
        print("Mensajes recibidos:")
        for mensaje in self.mensajes:
            print(mensaje)

# Funciones para la GUI
def enviar_trama():
    ack = ack_var.get()
    enq = enq_var.get()
    ctr = ctr_var.get()
    dat = dat_var.get()
    ppt = ppt_var.get()
    lpt = lpt_var.get()
    mensaje = mensaje_entry.get()
    frames = int(frames_entry.get())
    
    transmisor.frames = frames
    transmisor.enviar_mensaje(ack, enq, ctr, dat, ppt, lpt, mensaje, receptor)
    receptor.mostrar_mensajes()

# Crear instancias de Transmisor y Receptor
transmisor = Transmisor()
receptor = Receptor()

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Protocolo de Transmisión de Datos")

# Campo A: Mensaje a transmitir
tk.Label(root, text="Mensaje a transmitir:").grid(row=0, column=0)
mensaje_entry = tk.Entry(root, width=50)
mensaje_entry.grid(row=0, column=1, columnspan=4)

# Campo B: Número de frames
tk.Label(root, text="Número de frames:").grid(row=1, column=0)
frames_entry = tk.Entry(root, width=5)
frames_entry.grid(row=1, column=1)

# Campos de banderas C
tk.Label(root, text="ACK").grid(row=2, column=0)
ack_var = tk.BooleanVar()
tk.Checkbutton(root, variable=ack_var).grid(row=2, column=1)

tk.Label(root, text="ENQ").grid(row=2, column=2)
enq_var = tk.BooleanVar()
tk.Checkbutton(root, variable=enq_var).grid(row=2, column=3)

tk.Label(root, text="CTR").grid(row=3, column=0)
ctr_var = tk.BooleanVar()
tk.Checkbutton(root, variable=ctr_var).grid(row=3, column=1)

tk.Label(root, text="DAT").grid(row=3, column=2)
dat_var = tk.BooleanVar()
tk.Checkbutton(root, variable=dat_var).grid(row=3, column=3)

tk.Label(root, text="PPT").grid(row=4, column=0)
ppt_var = tk.BooleanVar()
tk.Checkbutton(root, variable=ppt_var).grid(row=4, column=1)

tk.Label(root, text="LPT").grid(row=4, column=2)
lpt_var = tk.BooleanVar()
tk.Checkbutton(root, variable=lpt_var).grid(row=4, column=3)

# Botón para enviar trama D
tk.Button(root, text="Enviar", command=enviar_trama).grid(row=5, column=0, columnspan=4)

# Área de receptor
tk.Label(root, text="Trama recibida:").grid(row=6, column=0)
recibidos_var = tk.StringVar()
recibidos_label = tk.Label(root, textvariable=recibidos_var, width=50)
recibidos_label.grid(row=6, column=1, columnspan=4)

# Mensaje completo recibido G
tk.Label(root, text="Mensaje recibido:").grid(row=7, column=0)
mensaje_completo_var = tk.StringVar()
mensaje_completo_label = tk.Label(root, textvariable=mensaje_completo_var, width=50)
mensaje_completo_label.grid(row=7, column=1, columnspan=4)

# Secuencia de tramas H
tk.Label(root, text="Secuencia de tramas:").grid(row=8, column=0)
secuencia_var = tk.StringVar()
secuencia_label = tk.Label(root, textvariable=secuencia_var, width=50)
secuencia_label.grid(row=8, column=1, columnspan=4)

# Inicializar GUI
root.mainloop()


'''
