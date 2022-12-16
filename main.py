from logic.skills import Skills
from logic.assistant import Rebeca_ai

skills = Skills()
rebeca = Rebeca_ai(skills)
rebeca.fala(f"Olá, eu sou a Rebeca! Uma assistente virtual")

counter = 0
while True:
    counter += 1
    rebeca.run()
    print(counter)