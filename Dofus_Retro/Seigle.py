import cv2
import numpy
import pyautogui
import time
import tkinter as tk
import os
import sys

from PIL import ImageGrab

# Pour MacOS
try:
    from Quartz.CoreGraphics import CGMainDisplayID, CGDisplayBounds

    screen_width = CGDisplayBounds(CGMainDisplayID()).size.width
    screen_height = CGDisplayBounds(CGMainDisplayID()).size.height
    print("hauteur", screen_height)
    print("largeur", screen_width)

# Pour Windows
except ImportError:
    import win32api, win32con

    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)
    print("hauteur", screen_height)
    print("largeur", screen_width)


# Vérifiez si nous sommes en mode "bundled" ou non
if getattr(sys, 'frozen', False):
    # Nous sommes en mode "bundled" (exécutable créé par PyInstaller)
    bundle_dir = sys._MEIPASS
else:
    # Nous ne sommes pas en mode "bundled" (script exécuté à partir du code source Python)
    bundle_dir = os.path.dirname(os.path.abspath(__file__))
# Construire les chemins d'accès aux images
image_paths = {
    'Menu': os.path.join(bundle_dir, 'Image', 'Interface', 'Menu.PNG'),
    'Cereale_0': os.path.join(bundle_dir, 'Image', 'Metier', 'Paysan', 'Seigle_0.png'),
    'Cereale_1': os.path.join(bundle_dir, 'Image', 'Metier', 'Paysan', 'Seigle_1.png'),
    'Cereale_2': os.path.join(bundle_dir, 'Image', 'Metier', 'Paysan', 'Seigle_2.png'),
    # Ajoutez autant d'entrées que nécessaire pour vos images
}


def ask_for_values():
    def submit():
        global X_CONSTANTE_2, Y_CONSTANTE_2
        X_CONSTANTE_2 = int(x_entry.get())
        Y_CONSTANTE_2 = int(y_entry.get())
        window.destroy()

    window = tk.Tk()
    window.title("Enter X_CONSTANTE_2 and Y_CONSTANTE_2")

    x_label = tk.Label(window, text="X_CONSTANTE_2")
    x_entry = tk.Entry(window)
    y_label = tk.Label(window, text="Y_CONSTANTE_2")
    y_entry = tk.Entry(window)
    submit_button = tk.Button(window, text="Submit", command=submit)

    x_label.pack()
    x_entry.pack()
    y_label.pack()
    y_entry.pack()
    submit_button.pack()

    window.mainloop()


# Call the function to get the X_CONSTANTE_2 and Y_CONSTANTE_2 values
ask_for_values()


class ModelDetector:
    def __init__(self, templates, method=cv2.TM_CCOEFF_NORMED, threshold=0.8):
        self.templates = templates
        self.method = method
        self.threshold = threshold

    def detect(self, X_CONSTANTE_2, Y_CONSTANTE_2):

        # Capturez une capture d'écran
        screenshot = ImageGrab.grab()

        # Convertir l'image en tableau numpy
        screenshot = cv2.cvtColor(numpy.array(screenshot), cv2.COLOR_RGB2BGR)

        # Recherchez la correspondance de chaque modèle dans la capture d'écran
        found = False
        for template_idx, template in enumerate(self.templates):
            result = cv2.matchTemplate(screenshot, template, self.method)

            # Obtenez les coordonnées du match avec la correspondance maximale
            location = numpy.where(result >= self.threshold)
            for point in zip(*location[::-1]):
                # Ajuster les coordonnées relatives en utilisant les coordonnées de capture d'écran
                X_CONSTANTE, Y_CONSTANTE = -80, 100
                x, y = point[0] - int(template.shape[1] / 2) - X_CONSTANTE, point[1] - int(
                    template.shape[0] / 2) + Y_CONSTANTE

                # Obtenir les coordonnées relatives
                relative_x = int((x / screenshot.shape[1]) * screen_width)
                relative_y = int((y / screenshot.shape[0]) * screen_height)

                # Utiliser les coordonnées relatives pour déplacer la souris
                pyautogui.moveTo(relative_x, relative_y, duration=0.3)

                # Attendre 5 secondes
                pyautogui.click()
                # X_CONSTANTE_2, Y_CONSTANTE_2 = 10, 140
                pyautogui.move(X_CONSTANTE_2, Y_CONSTANTE_2, duration=0.2)
                time.sleep(0.2)
                pyautogui.click()

                time.sleep(0.3)
                found = True
                return found
                # self.show_template(screenshot, point, template)

        # Si un modèle est trouvé, attendez 2 secondes
        print("Rien trouvé...")
        time.sleep(0.5)


templates = [
    # Image conseillé : 61px x 61px en PNG
    cv2.imread(image_paths['Menu']),
    cv2.imread(image_paths['Cereale_0']),
    cv2.imread(image_paths['Cereale_1']),
    cv2.imread(image_paths['Cereale_2']),
    # Ajoutez autant d'images que nécessaire
]

detector = ModelDetector(templates, method=cv2.TM_CCOEFF_NORMED, threshold=0.5)

while True:
    menu = pyautogui.locateOnScreen('Image/Interface/Menu.PNG', confidence=0.6)
    if menu:
        pyautogui.moveTo(menu, duration=0.2)
        time.sleep(0.1)
        pyautogui.click()
        print("Level Up")
    if detector.detect(X_CONSTANTE_2, Y_CONSTANTE_2):
        time.sleep(1)
    if cv2.waitKey(1) == ord('q'):
        break
    continue
