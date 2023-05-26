import cv2
import numpy
import pyautogui
import time

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


class ModelDetector:
    def __init__(self, templates, method=cv2.TM_CCOEFF_NORMED, threshold=0.7):
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
                X_CONSTANTE, Y_CONSTANTE = -15, 70
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
    cv2.imread('Image/Interface/Menu.PNG'),
    # cv2.imread('Image/Metier/Paysan/Template.png'),
    # cv2.imread('Image/Metier/Paysan/Orge_0.png'),
    # cv2.imread('Image/Metier/Paysan/Orge_1.png'),
    # cv2.imread('Image/Metier/Paysan/Orge_2.png'),
    # cv2.imread('Image/Metier/Paysan/Ble_0.png'),
    # cv2.imread('Image/Metier/Paysan/Ble_1.png'),
    # cv2.imread('Image/Metier/Paysan/Ble_2.png'),
    # cv2.imread('Image/Metier/Paysan/Lin_0.png'),
    # cv2.imread('Image/Metier/Paysan/Lin_1.png'),
    # cv2.imread('Image/Metier/Paysan/Lin_2.png'),
    # cv2.imread('Image/Metier/Paysan/Lin_3.png'),
    # cv2.imread('Image/Metier/Paysan/Avoine_0.png'),
    # cv2.imread('Image/Metier/Paysan/Avoine_1.png'),
    # cv2.imread('Image/Metier/Paysan/Avoine_2.png'),
    # cv2.imread('Image/Metier/Paysan/Houblon_0.png'),
    # cv2.imread('Image/Metier/Paysan/Houblon_1.png'),
    # cv2.imread('Image/Metier/Paysan/Houblon_2.png'),
    # cv2.imread('Image/Metier/Paysan/Houblon_3.png'),
    cv2.imread('Image/Metier/Paysan/Seigle_0.png'),
    cv2.imread('Image/Metier/Paysan/Seigle_1.png'),
    cv2.imread('Image/Metier/Paysan/Seigle_2.png'),
    cv2.imread('Image/Metier/Paysan/Seigle_3.png'),
    # Ajoutez autant d'images que nécessaire
]

detector = ModelDetector(templates, method=cv2.TM_CCOEFF_NORMED, threshold=0.6)

while True:
    menu = pyautogui.locateOnScreen('Image/Interface/Menu.PNG', confidence=0.6)
    if menu:
        pyautogui.moveTo(menu, duration=0.2)
        time.sleep(0.1)
        pyautogui.click()
        print("Level Up")
    if detector.detect(10, 40):
        time.sleep(2)
    if cv2.waitKey(1) == ord('q'):
        break
    continue
