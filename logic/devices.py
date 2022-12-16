import speech_recognition as sr
import pyttsx3

class Sound:
    def __init__(self, mic=1):
        self.voice = pyttsx3.init()
    
        voices = self.voice.getProperty('voices')
        ratio = self.voice.getProperty('rate')

        self.voice.setProperty('rate', ratio+50)
        self.voice.setProperty('voice', voices[0].id)
        
        self.listener = sr.Recognizer()
        self.mic = sr.Microphone(device_index=mic)
    
    def list_microphone(self):
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

    def talk(self, text):
        self.voice.say(text)
        self.voice.runAndWait()
        
    def get_comm(self):
        try:
            with self.mic as source:
                print('ouvindo\n.\n.\n')
                voice = self.listener.listen(source, phrase_time_limit=5)
                comm = self.listener.recognize_google(voice, language='pt-BR')
                comm = comm.lower()
                if 'rebeca' in comm:
                    comm = comm.replace('rebeca', '$$')
                    print('/ / /')
                    
            print('.\n.\n.\n')
            return comm   
        except:
            print('Não entendi')