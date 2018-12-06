#for ps4 controller
import pygame

import time

# Import the Robot.py file (must be in the same directory as this file!).
import Robot

LEFT_TRIM   = 0
RIGHT_TRIM  = 0
robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

pygame.init()
j=pygame.joystick.Joystick(0)
j.init()

speed = 100 # value from 0-255



try:
    while True:
        events = pygame.event.get()
        for event in events:
            
            if event.type==pygame.JOYBUTTONDOWN:
                print("Button Pressed")             
                if j.get_button(0):
                    speed = 50
                    #print("X")
                elif j.get_button(1):
                    print("Circle")
                elif j.get_button(2):
                    speed = 250
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
                speed = 100
            
            if event.type == pygame.JOYAXISMOTION:
                #print(event.dict, event.joy, event.axis, event.value)
                #print('Joy Axis Motion')
                pass
            if event.type == pygame.JOYBALLMOTION:
                #print(event.dict, event.joy, event.ball, event.rel)
                #print(event.rel)
                print('Joy Ball Motion')
            #elif event.type == pygame.JOYBUTTONDOWN:
            #    print(event.dict, event.joy, event.button, 'pressed')
            #elif event.type == pygame.JOYBUTTONUP:
            #    print(event.dict, event.joy, event.button, 'released')
            elif event.type == pygame.JOYHATMOTION:
                #print(event.dict, event.joy, event.hat, event.value)
                #print("HAT Pressed")
                if event.value==(0,1):
                    #robot.forward(speed, 1.0)   # Move forward at speed 150 for 1 second.
                    robot.forward(speed) #to run without time limit
                    #print("Up")
                elif event.value==(1,0):
                    #print("Right")
                    robot.right(speed)
                elif event.value==(0,-1):
                    #print("Down")
                    robot.backward(speed)
                elif event.value==(-1,0):
                    #print("Left")
                    robot.left(speed)
                elif event.value==(0,0):
                    #print("HAT Released")
                    robot.stop()
                   

except KeyboardInterrupt:
    print("Exiting Now")
    robot.stop()
    j.quit()
