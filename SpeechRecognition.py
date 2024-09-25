import speech_recognition as sr

def get_audio():
    while True:
        rec = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening please speak now...")
            audio = rec.listen(source)
            try:
                text = rec.recognize_google(audio)
                print(f"You said: {text}")
                return text
            except sr.UnknownValueError:
                print("Sorry, I did not get that please try again")
                return None
            except sr.RequestError:
                print("Sorry, Google recognize service is down =(")
                return None
