from pip._internal import commands

from TaskFunctions import add_task, remove_task, load_tasks
from SpeechRecognition import get_audio
from Reminder import remind_me
from playsound import playsound
from fuzzywuzzy import fuzz,process

if __name__ == "__main__":
    while True:
        print("Say a command (insert, remove, exit, mytodo):")
        command = get_audio()
        commands = ["insert", "remove", "exit" ,"my to do"]
        best_match = process.extractOne(command, commands, scorer=fuzz.ratio)
        if best_match[1] < 30:
            print("Unknown command please try again...")
            continue
        commandDo = best_match[0]
        rate = best_match[1]
        print(commandDo,"and rate",rate)
        if commandDo == "insert":
            print("What task do you want to insert?")
            task = get_audio()
            add_task(task)
            print(load_tasks())
            #print("When do you want to be reminded?")
            #delay = get_audio()
            #remind_me(task, int(delay))
            #print("Reminder set for", task, "in", delay, "seconds")


        elif commandDo == "remove":
            print("What task do you want to remove?")
            task = get_audio()
            remove_task(task)
        elif commandDo == "exit":
            print("Goodbye!")
            break
        elif commandDo == "my to do":
            print(load_tasks())
        else:
            print("Unknown command please try again...")
