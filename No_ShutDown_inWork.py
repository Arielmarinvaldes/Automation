import pyautogui
import time
from pynput import mouse

# Configuración
intervalo = 1  # segundos
tecla = 'esc'
contador = 0
movimiento = False

# Función para detectar el movimiento del mouse
def on_move(x, y):
    global movimiento
    movimiento = True

# Función para detectar la liberación del mouse
def on_release(x, y, button, pressed):
    global movimiento
    movimiento = False

# Configuración del listener del mouse
listener = mouse.Listener(on_move=on_move, on_release=on_release)
listener.start()

while True:
    if not movimiento:
        pyautogui.press(tecla)
        contador += 1
        print(f"Tecla {tecla} pulsada {contador} veces")
        time.sleep(intervalo)
    else:
        print(f"Tecla {tecla} pulsada {contador} veces")
        time.sleep(intervalo)


# Lo mismo pero con el mouse


# import pyautogui
# import time


# pyautogui.FAILSAFE = False

# def mover_mouse():
#     # Obtiene la posición actual del mouse
#     x, y = pyautogui.position()
    
#     # Mueve el mouse a la derecha 10 píxeles, asegurándose de que no se salga de la pantalla
#     screen_width, screen_height = pyautogui.size()
#     if x + 10 < screen_width:
#         pyautogui.moveTo(x + 10, y)
#     else:
#         pyautogui.moveTo(x - 10, y)  # Mueve a la izquierda si está cerca del borde derecho
    
#     # Espera 5 segundos
#     time.sleep(5)
    
#     # Mueve el mouse de vuelta a la posición original
#     pyautogui.moveTo(x, y)

# if __name__ == "__main__":
#     try:
#         print("El programa está en ejecución. Presiona Ctrl + C para detenerlo.")
#         while True:
#             mover_mouse()
#     except KeyboardInterrupt:
#         print("Programa detenido.")
