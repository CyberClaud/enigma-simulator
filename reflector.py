import pygame

class Reflector:

    def __init__(self, wiring):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring

    def reflect(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def draw(self, screen, x, y, w, h, font):

        # Rectangle
        r = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, "white", r, width=2, border_radius=15)

        # Letters
        for i in range(26):

            # Left Side

            letter = self.left[i]
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center = (x+w/4, y+(i+1)*h/27))
            screen.blit(letter, text_box)


            # Right Side
            
            letter = self.right[i]
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center = (x+w*3/4, y+(i+1)*h/27))
            screen.blit(letter, text_box)