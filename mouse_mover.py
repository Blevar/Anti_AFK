import pyautogui
import time
import random
import ctypes
from datetime import datetime

# Wyłączenie funkcji bezpieczeństwa PyAutoGUI (opcjonalne)
pyautogui.FAILSAFE = False  

# Stałe systemowe do blokowania wygaszacza ekranu
ES_CONTINUOUS = 0x80000000
ES_DISPLAY_REQUIRED = 0x00000002
ES_SYSTEM_REQUIRED = 0x00000001

# Pobranie wskaźnika do funkcji Windows API
def prevent_sleep():
    """Zapobiega włączeniu wygaszacza ekranu oraz uśpienia systemu."""
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_DISPLAY_REQUIRED | ES_SYSTEM_REQUIRED)

def get_current_time():
    """Zwraca aktualną datę i godzinę w formacie YYYY-MM-DD HH:MM:SS"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def move_mouse_and_press_key():
    """Porusza myszką i naciska klawisz, aby zapobiec uśpieniu systemu."""
    while True:
        prevent_sleep()  # Powstrzymuje system przed uśpieniem
        
        # Pobranie aktualnej pozycji myszy
        x, y = pyautogui.position()
        
        # Przesunięcie o bardzo mały dystans (aby uniknąć ruchu do rogów ekranu)
        dx = random.randint(-3, 3)
        dy = random.randint(-3, 3)
        
        # Przesuń mysz minimalnie w losowym kierunku
        pyautogui.moveTo(x + dx, y + dy, duration=0.2)
        print(f"[{get_current_time()}] Przesunięto mysz o ({dx}, {dy})")

        # Co jakiś czas naciska `Shift`, aby zresetować licznik bezczynności
        if random.random() < 0.5:  # Co drugi ruch naciska `Shift`
            pyautogui.press("shift")
            print(f"[{get_current_time()}] Naciśnięto klawisz Shift")

        # Odczekaj losowy czas między ruchami (np. 30-60 sekund)
        time.sleep(random.randint(30, 60))

if __name__ == "__main__":
    print(f"[{get_current_time()}] Uruchamiam skrypt zapobiegający przejściu w stan uśpienia...")
    move_mouse_and_press_key()
