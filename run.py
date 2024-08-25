from TaskFunctions import add_task, remove_task
from SpeechRecognition import get_audio
from Reminder import remind_me
from playsound import playsound

if __name__ == "__main__":
    while True:
        print("Say a command (add, remove, exit):")
        command = get_audio()

        if command:
            if "add" in command.lower() or "ad" in command.lower() or "ed" in command.lower() or \
                    "at" in command.lower() or "aad" in command.lower() or "had" in command.lower() or \
                    "and" in command.lower() or "ad" in command.lower() or "a d" in command.lower() or \
                    "addd" in command.lower() or "adde" in command.lower():
              if("add" in command.lower()):
                task = command.replace("add", "").strip()
                add_task(task)
                remind_me(task, 10)
                try:
                    playsound('reminder_sound.wav') # This will play a sound when the reminder is triggered
                except Exception as e:
                    print(f"Failed to play sound: {e}")


                try:
                    task_number = int(command.replace("remove", "").strip())
                    remove_task(task_number - 1)
                except ValueError:
                    print("Invalid number")
            elif "exit" in command.lower():
                break
            else:
                print("Unknown command ")
