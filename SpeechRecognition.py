import speech_recognition as sr
# This function is used to get the audio from the user and return the text

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~AUDIO RECOGNIZER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def get_audio():
    while True:#This loop will run until the user gives a clear audio
        rec = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening please speak now...")
            audio = rec.listen(source)
            try:
                text = rec.recognize_google(audio)
                return text#This will return the text
            except sr.UnknownValueError:
                print("Sorry, I did not get that please try again")#This error is raised when the audio is unclear
            except sr.RequestError:
                print("Sorry, Google recognize service is down =(")#This error is raised when the service is down
                return None
