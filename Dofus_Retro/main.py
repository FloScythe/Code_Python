import cv2
import numpy
import pyautogui
import time

from PIL import ImageGrab

from Quartz.CoreGraphics import CGMainDisplayID, CGDisplayBounds

screen_width = CGDisplayBounds(CGMainDisplayID()).size.width
screen_height = CGDisplayBounds(CGMainDisplayID()).size.height
print("hauteur",screen_height)
print("largeur",screen_width)


class ModelDetector:
    def __init__(self, templates, method=cv2.TM_CCOEFF_NORMED, threshold=0.8):
        self.templates = templates
        self.method = method
        self.threshold = threshold

    def detect(self):
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
                x, y = point[0] - int(template.shape[1] / 2), point[1] - int(template.shape[0] / 2)

                # Dessiner un rectangle rouge autour de la correspondance
                top_left = (x, y)
                bottom_right = (x + template.shape[1], y + template.shape[0])
                cv2.rectangle(screenshot, top_left, bottom_right, (0, 0, 255), 2)

                # Obtenir les coordonnées relatives
                relative_x = int((x / screenshot.shape[1]) * screen_width)
                relative_y = int((y / screenshot.shape[0]) * screen_height)

                # Utiliser les coordonnées relatives pour déplacer la souris
                pyautogui.moveTo(relative_x, relative_y)

                found = True
                print(f"Template {template_idx + 1} trouvé")

        cv2.imshow('Capture d\'ecran', screenshot)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Si un modèle est trouvé, attendez 10 secondes
        if found:
            time.sleep(10)

        return found


templates = [
    cv2.imread('Image/Metier/Paysan/Template1.png'),
    cv2.imread('Image/Metier/Paysan/Template2.png'),
    cv2.imread('Image/Metier/Paysan/Template3.png'),
    cv2.imread('Image/Metier/Paysan/Template4.png'),
    cv2.imread('Image/Metier/Paysan/Template5.png'),
    cv2.imread('Image/Metier/Paysan/Template6.png'),
    cv2.imread('Image/Metier/Paysan/Template7.png'),
    cv2.imread('Image/Metier/Paysan/Template8.png'),
    cv2.imread('Image/Metier/Paysan/Template99.png'),
    # Ajoutez autant d'images que nécessaire
]

detector = ModelDetector(templates, method=cv2.TM_CCOEFF_NORMED, threshold=0.8)

while True:
    print("Detection...")
    if detector.detect():
        continue
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
