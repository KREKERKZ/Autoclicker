
from pynput import mouse, keyboard
from threading import Thread, Event
import time
import sys

print("Скрипт запущен")

print("Библиотеки импортированы")


class AutoClicker:
    def __init__(self, interval=0.01, click_count=100):
        print("Автокликер инициализирован")
        self.interval = interval
        self.click_count = click_count
        self.clicking = Event()
        self.thread = Thread(target=self.click_mouse)
        self.thread.daemon = True
        self.thread.start()

    def click_mouse(self):
        while True:
            self.clicking.wait()
            for _ in range(self.click_count):
                mouse_controller.click(mouse.Button.left)  # Левая кнопка мыши
                time.sleep(self.interval)

    def start_clicking(self):
        print("Автокликер запущен")
        self.clicking.set()

    def stop_clicking(self):
        print("Автокликер остановлен")
        self.clicking.clear()


print("Перед созданием контроллера мыши")
mouse_controller = mouse.Controller()
auto_clicker = AutoClicker()

# Определим комбинации клавиш для запуска, остановки и завершения автокликера
start_key = keyboard.Key.f1
stop_key = keyboard.Key.f2
exit_key = keyboard.Key.f3

current_keys = set()


def on_press(key):
    global current_keys
    print(f"Клавиша нажата: {key}")
    current_keys.add(key)
    if key == start_key:
        auto_clicker.start_clicking()
    elif key == stop_key:
        auto_clicker.stop_clicking()
    elif key == exit_key:
        print("Скрипт завершен")
        # Останавливаем автокликер перед завершением
        auto_clicker.stop_clicking()
        sys.exit(0)


def on_release(key):
    global current_keys
    print(f"Клавиша отпущена: {key}")
    current_keys.discard(key)


print("Перед запуском слушателя клавиатуры")
keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
keyboard_listener.start()

print("Скрипт работает")
keyboard_listener.join()
