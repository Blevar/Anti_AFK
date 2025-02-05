import pyautogui
import time
import random
from datetime import datetime

# Wyłączenie funkcji bezpieczeństwa PyAutoGUI (opcjonalne)
pyautogui.FAILSAFE = False  

# Czas ostatniej aktywności użytkownika
last_x, last_y = pyautogui.position()
last_active_time = time.time()

def get_current_time():
    """Zwraca aktualną datę i godzinę w formacie YYYY-MM-DD HH:MM:SS"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def check_user_activity():
    """Sprawdza, czy użytkownik poruszył myszą."""
    global last_x, last_y, last_active_time
    x, y = pyautogui.position()
    if (x, y) != (last_x, last_y):
        last_x, last_y = x, y
        last_active_time = time.time()
        return True
    return False

def move_mouse():
    while True:
        if check_user_activity():
            print(f"[{get_current_time()}] Wykryto aktywność użytkownika. Pauza w działaniu...")
            time.sleep(60)  # Przerwa 1 minuta
            print(f"[{get_current_time()}] Wznawiam działanie...")
        else:
            # Pobranie aktualnej pozycji myszy
            x, y = pyautogui.position()
            
            # Przesunięcie o bardzo mały dystans (aby uniknąć ruchu do rogów ekranu)
            dx = random.randint(-3, 3)
            dy = random.randint(-3, 3)
            
            # Przesuń mysz minimalnie w losowym kierunku
            pyautogui.moveTo(x + dx, y + dy, duration=0.2)
            
            # Wyświetl informację o ruchu myszy
            print(f"[{get_current_time()}] Przesunięto mysz o ({dx}, {dy})")

            # Odczekaj losowy czas między ruchami (np. 30-60 sekund)
            time.sleep(random.randint(30, 60))

if __name__ == "__main__":
    print(f"[{get_current_time()}] Uruchamiam skrypt zapobiegający przejściu w stan uśpienia...")
    move_mouse()
