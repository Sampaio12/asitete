import pywhatkit, datetime, wikipedia, sys, os
from  logic.devices import Sound
from logic.advices import get_ptbr_advice
import webbrowser as web
from logic.spotify_api import Spotify

spotify = Spotify()

class Skills:
    def __init__(self):
        self.sound = Sound()
        self.say = self.sound.talk
        self.skills = {
            # Tocar música no YouTube
            'assistir': self.music,
            'ouvir': self.music,
            
            # Tocar música no Spotify
            'spotify': self.spotify_start,
            'toca': self.spotify_start,
            'toque': self.spotify_start,
            'tocar': self.spotify_start,
            
            # Opções do spotify
            'aumenta o volume': self.spotify_vol_up,
            'aumenta': self.spotify_vol_up,
            'diminui o volume': self.spotify_vol_down,
            'diminui': self.spotify_vol_down,
            'abaixa': self.spotify_vol_down,
            'pausa': self.spotify_pause,
            'continua': self.spotify_resume,
            
            # Pesquisar no Google
            'pesquisa': self.search,
            'procura': self.search,
            
            # Dizer a hora
            'hora': self.time,
            'horas': self.time,
            
            # Pesquisar no Wikipedia
            'quem é': self.who_is,
            'quem foi': self.who_is,
            
            # Abrir programas
            'discord': self.discord,
            'vs code': self.vscode,
            'quero programar': self.vscode,
            
            # Dizer Olá
            'oi': self.hello,
            'olá': self.hello,
            
            # Dizer o que Rebeca pode fazer
            'o que você pode fazer': self.can_do,
            'o que você sabe fazer': self.can_do,
            'me ajuda': self.can_do,
            
            # Dizer uma dica
            'conselho': self.advice,
            'dica': self.advice,
            
            # Encerrar Rebeca
            'sair': self.leave,
            'desligar': self.leave,
}
        
    def time(self, comm):
        time = datetime.datetime.now().strftime('%H:%M')
        self.say(f"Agora são {time}")
        return
    
    def music(self, song):
        video = pywhatkit.playonyt(song)
        self.say(f"Tocando {song} no YouTube")
        return
    
    def spotify_start(self, comm):
        comm = comm.replace(' ', '')
        self.say(f"Tocando {spotify.get_title(comm)} no Spotify")
        song = spotify.spotify_play(comm)
        return
    
    def spotify_vol_up(self, comm):
        self.say(f"Aumentando volume")
        spotify.volume_up()
        return
    
    def spotify_vol_down(self, comm):
        self.say(f"Diminuindo volume")
        spotify.volume_down()
        return
    
    def spotify_pause(self, comm):
        self.say(f"Pausando música no Spotify")
        spotify.pause()
        return
    
    def spotify_resume(self, comm):
        self.say (f"Retomando música no Spotify")
        spotify.resume()
        return
    
    def who_is(self, person):
        wikipedia.set_lang('pt')
        info = wikipedia.summary(person, 1)
        self.say(info)
        return
    
    def search(self, comm):
        pesquisa = pywhatkit.search(comm)
        self.say(f"Pesquisando {comm} no Google")
    
    def vscode(self, comm):
        self.say('Abrindo Visual Studio Code')
        sys = os.system('code')
        return
    
    def discord(self, comm):
        discord_exe = 'C:\\Users\\lucas\\AppData\\Local\\Discord\\app-1.0.9008\\Discord.exe'
        self.say('Abrindo Discord')
        sys = os.system(discord_exe)
        
    def hello(self, comm):
        self.say('Olá, como vai?')
        return
    
    def advice(self, comm):
        advice = get_ptbr_advice()
        self.say(advice)
        return
    
    def can_do(self, comm):
        self.say('Eu posso tocar músicas, pesquisar no Google, pesquisar no Wikipedia, te dar conselhos, te dizer a hora, abrir o VS Code, e muito mais!')
    
    def leave(self, comm):
        self.say('Até mais!')
        sys.exit()
        exit()
    
    def get_skill(self):
        skill_list = []
        for skill in self.skills:
            skill_list.append(skill)
        
        return skill_list

    def skill_dict(self, comm):
        return self.skills[comm]


if __name__ == '__main__':
    skill = Skills()
    skill.say('oi')