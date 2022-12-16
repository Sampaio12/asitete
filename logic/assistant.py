import speech_recognition as sr
import pyttsx3
from logic.devices import Sound
from logic.skills import Skills

class Rebeca_ai(Sound):

    def __init__(self, skills):
        super().__init__()
        self.skill = skills
        self.skill_list = self.skill.get_skill()
    
    def run(self):
        comm = self.get_comm()
        if comm == None:
            print("Aguardando comando...")
            return
        elif '$$' in comm:
            comm = comm.replace('$$', '')
            print(f"comando: {comm}")
            for skill in self.skill_list:
                if skill in comm:
                    comm = comm.replace(skill, '')
                    self.skill.skill_dict(skill)(comm)
                                
        else:
            print(f"comando: {comm}")
        
    def fala(self, text):
        self.voice.say(text)
        self.voice.runAndWait()
            
if __name__ == '__main__':
    ai_name = 'rebeca'
    skills = Skills()
    rebeca = Rebeca_ai(skills)
    rebeca.fala(f"Olá, eu sou a {ai_name}, sua assistente virtual")
    
    counter = 0
    while True:
        counter += 1
        rebeca.run()
        print(counter)
        