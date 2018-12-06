import pygame

pygame.init()

j=pygame.joystick.Joystick(0)
j.init()

try:
    while True:
        events = pygame.event.get()
        for event in events:
            
            if event.type==pygame.JOYBUTTONDOWN:
                print("Button Pressed")             
                if j.get_button(0):
                    print("X")
                elif j.get_button(1):
                    print("Circle")
                elif j.get_button(2):
                    print("Triangle")
                elif j.get_button(3):
                    print("Square")
                elif j.get_button(4):
                    print("L1")
                elif j.get_button(5):
                    print("R1")
                elif j.get_button(6):
                    print("L2")
                elif j.get_button(7):
                    print("R2")
                elif j.get_button(8):
                    print("Share")
                elif j.get_button(9):
                    print("Option")
                elif j.get_button(10):
                    print("PS")
                elif j.get_button(11):
                    print("Left Joy Press")
                elif j.get_button(12):
                    print("Right Joy Press")
                elif j.get_button(13):
                    print("13")
                elif j.get_button(14):
                    print("14")
                elif j.get_button(15):
                    print("15")
            elif event.type == pygame.JOYBUTTONUP:
                print("Button Released")
            
            if event.type == pygame.JOYAXISMOTION:
                print(event.dict, event.joy, event.axis, event.value)
            if event.type == pygame.JOYBALLMOTION:
                print(event.dict, event.joy, event.ball, event.rel)
                print(event.rel)
            #elif event.type == pygame.JOYBUTTONDOWN:
            #    print(event.dict, event.joy, event.button, 'pressed')
            #elif event.type == pygame.JOYBUTTONUP:
            #    print(event.dict, event.joy, event.button, 'released')
            elif event.type == pygame.JOYHATMOTION:
                #print(event.dict, event.joy, event.hat, event.value)
                print("HAT Pressed")
                if event.value==(0,1):
                    print("Up")
                elif event.value==(1,0):
                    print("Right")
                elif event.value==(0,-1):
                    print("Down")
                elif event.value==(-1,0):
                    print("Left")
                elif event.value==(0,0):
                    print("HAT Released")
                   

except KeyboardInterrupt:
    print("Exiting Now")
    j.quit()