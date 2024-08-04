import pygame

from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
from draw import draw

# Setup Pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma Simulator")

# Create fonts
BOLD = pygame.font.SysFont("Helvetica", 20, bold=True)
HELV = pygame.font.SysFont("Helvetica", 20)


# Global Variables
WIDTH = 1200
HEIGHT = 675
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
MARGINS = {"top": 125, "bottom": 25, "left": 75, "right": 75}
GAP = 75

INPUT = ""
OUTPUT = ""
PATH = []

# Enigma Rotors and Reflectors
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

# Keyboard and Plugboard
KB = Keyboard()
PB = Plugboard(["AB", "CD", "EF"])

# Enigma Machince
ENIGMA = Enigma(B, I, II, III, PB, KB)

# Set Rings
ENIGMA.set_rings((1,1,1))

# Set Message Key
ENIGMA.set_key("CAT")

"""
# Enicpher a message
message = "TestingTestingTestingTesting".upper()
cipher_text = ""
for letter in message:
    cipher_text = cipher_text + ENIGMA.encipher(letter)
print(cipher_text)
"""

animating = True
while animating:

    # Background Color
    SCREEN.fill("#333333")

    # Text Input
    text = BOLD.render(INPUT, True, "white")
    text_box = text.get_rect(center = (WIDTH/2, MARGINS["top"]/4))
    SCREEN.blit(text, text_box)

    # Text Output
    text = HELV.render(OUTPUT, True, "white")
    text_box = text.get_rect(center = (WIDTH/2, MARGINS["top"]/4+25))
    SCREEN.blit(text, text_box)


    # Draw Enigma Machine
    draw(ENIGMA, PATH, SCREEN, WIDTH, HEIGHT, MARGINS, GAP, HELV)

    # Update Screen
    pygame.display.flip()

    # Track user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                #II.rotate()
                pass
            elif event.key == pygame.K_SPACE:
                INPUT = INPUT + " "
                OUTPUT = OUTPUT + " "
        
            else: 
                key = event.unicode
                if key in "abcdefghijklmnopqrstuvwxyz":
                    letter = key.upper()
                    INPUT = INPUT + letter
                    PATH, cipher = ENIGMA.encipher(letter)
                    print(PATH)
                    OUTPUT = OUTPUT + cipher