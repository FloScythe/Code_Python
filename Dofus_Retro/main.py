import cv2
import numpy
import pyautogui
import time

from PIL import ImageGrab

# Pour Mac OS
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
                X_CONSTANTE, Y_CONSTANTE = -20, 70
                x, y = point[0] - int(template.shape[1] / 2) - X_CONSTANTE, point[1] - int(
                    template.shape[0] / 2) + Y_CONSTANTE

                # Obtenir les coordonnées relatives
                relative_x = int((x / screenshot.shape[1]) * screen_width)
                relative_y = int((y / screenshot.shape[0]) * screen_height)

                print("x:", x, "y:", y, "relative_x:", relative_x, "relative_y:", relative_y)

                # Utiliser les coordonnées relatives pour déplacer la souris
                pyautogui.moveTo(relative_x, relative_y, duration=0.3)

                # Attendre 5 secondes
                print(f"Template {template_idx + 1} trouvé")
                pyautogui.click()
                X_CONSTANTE, Y_CONSTANTE = 10, 80
                pyautogui.move(X_CONSTANTE,Y_CONSTANTE,duration=0.2)
                time.sleep(0.2)
                pyautogui.click()

                time.sleep(0.5)
                found = True
                return found
                # self.show_template(screenshot, point, template)

        # Si un modèle est trouvé, attendez 2 secondes
        print("Rien trouvé...")
        time.sleep(0.5)

    """def show_template(self, screenshot, point, template):
        # Dessinez un rectangle rouge autour de l'élément détecté
        x, y = point[0], point[1]
        print("x , y : ", x, y)
        w, h, _ = template.shape[::-1]
        print("w,h :", w, h)
        debut_x, debut_y = x, y
        fin_x, fin_y = x + w, y + h
        cv2.rectangle(screenshot, (debut_x, debut_y), (fin_x, fin_y), (0, 0, 255), 1)
        cv2.imshow('Template', screenshot)
        cv2.waitKey(0)
        cv2.destroyAllWindows()"""


templates = [
    # cv2.imread('Image/Metier/Paysan/Template.png'),
    # cv2.imread('Image/Metier/Paysan/Template1.png'),
    # cv2.imread('Image/Metier/Paysan/Ble_0.png'),
    # cv2.imread('Image/Metier/Paysan/Orge_0.png'),
    cv2.imread('Image/Metier/Paysan/Lin_0.png'),
    cv2.imread('Image/Metier/Paysan/Lin_1.png'),
    cv2.imread('Image/Metier/Paysan/Lin_2.png'),
    cv2.imread('Image/Metier/Paysan/Avoine_0.png'),
    cv2.imread('Image/Metier/Paysan/Avoine_1.png'),
    cv2.imread('Image/Metier/Paysan/Avoine_2.png'),
    cv2.imread('Image/Metier/Paysan/Houblon_0.png'),
    cv2.imread('Image/Metier/Paysan/Houblon_1.png'),
    cv2.imread('Image/Metier/Paysan/Houblon_2.png'),
    cv2.imread('Image/Metier/Paysan/Houblon_3.png'),
    # Ajoutez autant d'images que nécessaire
]

detector = ModelDetector(templates, method=cv2.TM_CCOEFF_NORMED, threshold=0.5)

while True:
    print("Detection...")
    if detector.detect():
        """
        x, y = pyautogui.position()
        x_click, y_click = x + 0, y + 0
        print("x:", x, "y:", y)
        print("x_click:", x_click, "y_click:", y_click)
        """
        time.sleep(2)
        # pyautogui.moveTo(x_click, y_click)
        if cv2.waitKey(1) == ord('q'):
            break
        continue
