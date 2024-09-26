from TaskFunctions import *
from SpeechRecognition import *
from fuzzywuzzy import fuzz,process

if __name__ == "__main__":
    while True:
        print("Say a command ( ~insert~ , ~remove~ , ~mytodo~ , ~exit~ ):")
        command = get_audio()
        commands = ["insert", "remove", "exit" ,"my to do"]
        best_match = process.extractOne(command, commands, scorer=fuzz.ratio)
        if best_match[1] < 30:
            print("Unknown command please try again...")
            continue
        commandDo = best_match[0]
        print(f"You said: ", commandDo)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~INSERT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        if commandDo == "insert":
            print("What task do you want to insert?")
            task = get_audio()
            add_task(task)
            print("Done!")
            display_tasks()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~REMOVE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        elif commandDo == "remove":
            print(load_tasks())
            print("What task do you want to remove(chose task name)?")
            task = get_audio()
            remove_task(task)
            display_tasks()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MY-TO-DO~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        elif commandDo == "my to do":
            display_tasks()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~EXIT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        elif commandDo == "exit":
            print("Goodbye!")
            break

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Unknown~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        else:
            print("Unknown command please try again...")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MORE REQUEST?~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        print("Do you have any more requests? ( ~YES~ / ~NO~ )")
        more_requests = get_audio()
        print("You said: ", more_requests)
        if more_requests == "no":
            print("Goodbye!")
            break
        elif more_requests == "yes":
            continue
        else:
            print("Unknown command please try again...")
            break