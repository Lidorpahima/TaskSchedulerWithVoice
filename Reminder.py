import time
import threading
from playsound import playsound

def remind_me(task, delay):
    def reminder():
        time.sleep(delay)
        print(f"Reminder: {task}")
        playsound('reminder_sound.wav')

    t = threading.Thread(target=reminder)
    t.start()