from pyfiglet import Figlet
import random

f = Figlet()
lista = f.getFonts()
rand = random.choice(lista)

print(rand)