import requests #con esto importas la libreria requests, 
#basicamente lo que hace esta libreria es permitir que se manden requests (solicitudes) desde python para interactuar con una API y agarrar algun dato especifico que estes buscando, 
#en este caso son los tipos de cambio actualizados
import tkinter as tk 
#from tkinter import ttk #para el styling mas desarrollado del UI
import pygame #importar la libreria pygame para agregar sonido
def get_tiposdecambio(api_key):
    url = "https://v6.exchangerate-api.com/v6/" + api_key + "/latest/ARS" #link del sitio que vamos a usar para extraer los datos del tipo de cambio
    response= requests.get(url)
    data= response.json() 
    cambio_oficial= data['conversion_rates']['USD'] #dolar oficial
    blue= cambio_oficial* 1.2 #asumamos que el blue vale 20% mas
    # Debugging: Print the fetched rates
    print("Official Rate:", cambio_oficial)
    print("Blue Rate:", blue)
    return cambio_oficial,blue

def play_completion_sound():
    pygame.mixer.Sound("TADA.wav").play()
def play_close_sound():
    pygame.mixer.Sound("CHIMES.wav").play()

def convert_currency():
    try:
        pesos = float(entry_pesos.get()) 
        cambio_oficial,blue= get_tiposdecambio(api_key) #con esta linea "agarramos" los valores en tiempo real de los tipos de cambio respectivos con la llave de la API
        exchange = pesos * cambio_oficial 
        parallel_ex = pesos * blue
        label_result.config(text=f"Oficial: {exchange:.2f} USD\nBlue: {parallel_ex:.2f} USD")
        play_completion_sound()
    except ValueError:
        label_result.config(text="Por favor ingrese un numero valido...")  

def on_closing():
    play_close_sound()  # Play the close sound
    root.after(1000, root.destroy)  # Wait for 2 seconds to let the sound play before closing
#ahora inicializamos pygame para que se reproduzca la intro de Windows 95 compuesta por Brian Eno
pygame.mixer.init()
pygame.mixer.music.load("Windows 95 Startup Sound - Brian Eno - The Microsoft Sound.mp3")
pygame.mixer.music.play()

api_key= "95203ef207a68485ebd8fdf7" #esta es la llave de la API con la que vamos a acceder a la informacion que nos interesa de la web
#creo la ventana principal
root=tk.Tk()
root.title("Parallel Currency Converter")
#style = tk.Style()
#style.configure("TLabel", font=("Arial", 12))
#style.configure("TButton", font=("Arial", 12))
#style.configure("TEntry", font=("Arial", 12))
#title_label = tk.Label(root, text="Currency Converter", font=("Arial", 16, "bold"))
#title_label.grid(row=0, column=0, columnspan=2, pady=10)
#creo los widgets
label_pesos=tk.Label(root, text="Monto en pesos argentinos: ")
#label_pesos=tk.Label(root, text="Monto en pesos argentinos: ",font="Arial")



label_pesos.pack()
entry_pesos = tk.Entry(root)
entry_pesos.focus_set()
entry_pesos.pack()
button_convert= tk.Button(root, text="Convertir",command=convert_currency)
button_convert.pack()
label_result = tk.Label(root, text="")
label_result.pack()
# Load the image
image_path = "/Users/cucu/Downloads/Flag_of_Argentina.png"  # Ensure this path is correct
image = tk.PhotoImage(file=image_path)

# Create an image label and place it
image_label = tk.Label(root, image=image)
image_label.pack(pady=10)

root.geometry("400x500")
root.protocol("WM_DELETE_WINDOW", on_closing)
#ahora corremos la aplicacion
root.mainloop()

#print ("\nEquivalente a {:.2f} (Dólar oficial)".format(exchange)) #lo de {:.2f} es para que la variable que se imprima solo tenga dos decimales y no tenga muchisimos que es medio nocivo para la vista del usuario. 
#print ("\nEquivalente a {:.2f} (Dólar blue)".format(parallel_ex)) #aca lo mismo, y se usa el .format que es un metodo para darle formato a strings en Python

#print("\nEl cambio oficial es el valor del dólar según el gobierno") #imprimir en pantalla explicacion basica del termino dolar oficial
#print("\nEl dolar blue se refiere al valor del dólar en el mercado paralelo") #imprimir en pantalla explicacion basica del termino dolar blue

#print("\nMuchas gracias por usar nuestro conversor de monedas. Vuelva pronto!") #imprimir en pantalla un mensaje agradeciendo al usuario
