import pyttsx3
import speech_recognition as sr


class AI():
    __name = ""
    __skill = []

    def __init__(self, name=None):
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        newVoiceRate = 170
        self.engine.setProperty('rate',newVoiceRate)

        self.r = sr.Recognizer()
        self.m = sr.Microphone(device_index=1)

        if name is not None:
            self.__name = name

        print("Listening")
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        sentence = "Hello, my name is" + self.__name
        self.__name = value
        self.engine.say(sentence)
        self.engine.runAndWait() 

    def say(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()

    def listen(self):
        print("Say Something")
        with self.m as source:
            audio = self.r.listen(source)
        print("got it") 
        try:
            phrase = self.r.recognize_google(audio, show_all=False, language="en_GB")
            # print("You said", phrase)
            return phrase
        except Exception as e:
            print("Sorry, didn't catch that",e)
            # self.engine.say("Sorry, didn't catch that")
            # self.engine.runAndWait()
            return "None"

    # def get_audio(self):
    #     print("Say Something")
    #     with self.m as source:
    #         audio = self.r.listen(source)
    #         phrase = ""
    #         try:
    #             phrase = self.r.recognize_google(audio, show_all=False, language="en_GB")
    #         except Exception as e:
    #             print("Exception: " + str(e))
    #     return phrase.lower()
    
