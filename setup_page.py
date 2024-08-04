import os
from time import sleep

logo = """

$$$$$$$$\ $$\   $$\ $$$$$$\  $$$$$$\  $$\      $$\  $$$$$$\  
$$  _____|$$$\  $$ |\_$$  _|$$  __$$\ $$$\    $$$ |$$  __$$\ 
$$ |      $$$$\ $$ |  $$ |  $$ /  \__|$$$$\  $$$$ |$$ /  $$ |
$$$$$\    $$ $$\$$ |  $$ |  $$ |$$$$\ $$\$$\$$ $$ |$$$$$$$$ |
$$  __|   $$ \$$$$ |  $$ |  $$ |\_$$ |$$ \$$$  $$ |$$  __$$ |
$$ |      $$ |\$$$ |  $$ |  $$ |  $$ |$$ |\$  /$$ |$$ |  $$ |
$$$$$$$$\ $$ | \$$ |$$$$$$\ \$$$$$$  |$$ | \_/ $$ |$$ |  $$ |
\________|\__|  \__|\______| \______/ \__|     \__|\__|  \__|
_____________________________________________________________

"""

print(logo)

print("Welcome to the Enigma Simulator!")

sleep(3)
os.system("clear")

print("Now let's begin by configuring the Enigma Machine.\n")

sleep(3)
os.system("clear")

rotor = input("""Which 3 rotors would you like to use and which order?\n
Example Input: I,V,III\n
1.I (EKMFLGDQVZNTOWYHXUSPAIBRCJ)
2.II (AJDKSIRUXBLHWTMCQGZNPYFVOE)
3.III (BDFHJLCPRTXVZNYEIWGAKMUSQO)
4.IV (ESOVPZJAYQUIRHXLNFTGKDCMWB)
5.V (VZBRGITYUPSDNHLXAWMJQOFECK)
\n:""")

print(rotor, type(rotor))

formatted_rotor = rotor.split(",")

print(formatted_rotor)

# os.system("clear")

# reflector = input("""Which reflector would you like to use?\n
# Example Input: C\n
# 1. A (EJMZALYXVBWFCRQUONTSPIKHGD)      
# 2. B (YRUHQSLDPXNGOKMIEBFZCWVJAT)      
# 3. C (FVPJIAOYEDRZXWGCTKUQSBNMHL)      
# \n:""")

# os.system("clear")

# letter_pair = input("""List any pairs of letters you wish to swap in plugboard.\n
# Example Input: AC, QZ, GS
# \n:""")

# os.system("clear")

# key = input("""Set a 3 letter key.\n
# Example Input: ABC
# \n:""")

# os.system("clear")

# message = input("""Enter secret message.\n
# Example Input: The Code is 21328
# \n:""")