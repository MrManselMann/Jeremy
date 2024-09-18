import speech_recognition as sr
def get_text():
    def record_text():
        r = sr.Recognizer()
        while True:
            try:
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=0.2)
                    audio = r.listen(source)
                    mytext = r.recognize_google(audio)
                    return mytext
            except sr.RequestError as e:
                print("qq")
            except sr.UnknownValueError:
                print("qq")
            except Exception as e:
                print("qq")

    while True:
        text = record_text()
        return text
        break
