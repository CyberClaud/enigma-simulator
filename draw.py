import pygame

def draw(engima, path, screen, width, height, margins, gap, font):

    # Width and Height of Components
    w = (width - margins["left"] - margins["right"] - 5*gap) / 6
    h = height - margins["top"] - margins["bottom"]

    # Path Coordinates
    y = [margins["top"]+(signal+1)*h/27 for signal in path]
    x = [width-margins["right"]-w/2] # Keyboard
    for i in [4,3,2,1,0]: # Forward Pass
        x.append(margins["left"]+i*(w+gap)+w*3/4)
        x.append(margins["left"]+i*(w+gap)+w*1/4)
    x.append(margins["left"]+w*3/4) # Reflector

    for i in [1,2,3,4]: # Backward Pass
        x.append(margins["left"]+i*(w+gap)+w*1/4)
        x.append(margins["left"]+i*(w+gap)+w*3/4)
    x.append(width-margins["right"]-w/2) # Lampboard

    # Draw Path
    if len(path) > 0:
        for i in range(1, 21):
            if i < 10:
                color = "#43aa8b"
            elif i < 12:
                color = "#f9c74f"
            else:
                color = "#e63946"
            start = (x[i-1], y[i-1])
            end = (x[i], y[i])
            pygame.draw.line(screen, color, start, end, width=5)

    # Coordinates Setup
    x = margins["left"]
    y = margins["top"]

    # Enigma Components
    for component in [engima.re, engima.r1, engima.r2, engima.r3, engima.pb, engima.kb]:
        component.draw(screen, x, y, w, h, font)
        x += w + gap

    # Add names
    names = ["Reflector", "Left", "Middle", "Right", "Plugboard", "Key/Lamp"]
    y = margins["top"]*0.8
    for i in range(6):
        x = margins["left"] + w/2 + i*(w+gap)
        title = font.render(names[i], True, "white")
        text_box = title.get_rect(center = (x, y))
        screen.blit(title, text_box)