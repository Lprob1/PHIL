from imports import *

class SpeechToText:
    def __init__(self):
        self.r = sr.Recognizer()

    def record(self):
        """"""
        try:
            # use mic as input source
            with sr.Microphone() as source:
                self.r.adjust_for_ambient_noise(source, duration=2)
                #record audio
                audio = self.r.listen(source)
                text = self.r.recognize_google(audio)
        except sr.RequestError as e:
            print("Could not request results; {}".format(e))
            return None
        except sr.UnknownValueError:
            print("Unknown error occured")
            return None
        if text:
            return text
        else:
            return None