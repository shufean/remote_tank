#for ps4 controller
import pygame

import time

# Import the Robot.py file (must be in the same directory as this file!).
import Robot4Motors

LEFT_TRIM   = 0
RIGHT_TRIM  = 0
LEFT_2_TRIM   = 0
RIGHT_2_TRIM  = 0
robot = Robot4Motors.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM, left_2_trim=LEFT_2_TRIM, right_2_trim=RIGHT_2_TRIM)

pygame.init()

# Initialize speed values
speed = 100 # value from 0-255
HIGH = 250
LOW = 50
REGULAR = 100

try:
    
    j=pygame.joystick.Joystick(0)
    j.init()
    
    while True:
        events = pygame.event.get()
        for event in events:
            
            if event.type==pygame.JOYBUTTONDOWN:
                print("Button Pressed")             
                if j.get_button(0):
                    speed = LOW
                    #print("X")
                elif j.get_button(1):
                    print("Circle")
                elif j.get_button(2):
                    speed = HIGH
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
                speed = REGULAR
            
            if event.type == pygame.JOYAXISMOTION:
                #print(event.dict, event.joy, event.axis, event.value)
                #print('Joy Axis Motion')
                '''
                #Left Joystick (event.axis == 0 or event.axis == 1)
                if event.axis == 0 and event.value<-.5:
                    #print("Left Joy - Left")
                    robot.left(speed)
                if event.axis == 0 and event.value>.5:
                    #print("Left Joy - Right")
                    robot.right(speed)
                if event.axis == 1 and event.value<-.5:
                    #print("Left Joy - Up")
                    robot.forward(speed)
                if event.axis == 1 and event.value>.5:
                    #print("Left Joy - Down")
                    robot.backward(speed)                
                '''
                
                #Right Joystick (event.axis == 3 or event.axis == 4)
                if event.axis == 3 and event.value<-.5:
                    print("Right Joy - Left")
                if event.axis == 3 and event.value>.5:
                    print("Right Joy - Right")
                if event.axis == 4 and event.value<-.5:
                    print("Right Joy - Up")
                if event.axis == 4 and event.value>.5:
                    print("Right Joy - Down")
                    
                #L2 Button Hardness (event.axis == 2)
                if event.axis == 2 and event.value<-.5:
                    print("L2 - Soft")
                if event.axis == 2 and event.value>.5:
                    print("L2 - Hard")
                    
                #R2 Button Hardness (event.axis == 5)
                if event.axis == 5 and event.value<-.5:
                    print("R2 - Soft")
                if event.axis == 5 and event.value>.5:
                    print("R2 - Hard")
            else:
                robot.stop()
                    
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
                    robot.right(speed=HIGH)
                elif event.value==(0,-1):
                    #print("Down")
                    robot.backward(speed)
                elif event.value==(-1,0):
                    #print("Left")
                    robot.left(speed=HIGH)
                elif event.value==(0,0):
                    #print("HAT Released")
                    robot.stop()
                   

except KeyboardInterrupt:
    print("Exiting Now")
    robot.stop()
    j.quit()
