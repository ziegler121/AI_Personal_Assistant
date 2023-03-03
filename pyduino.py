from ai import AI
# import cv2
# import face_recognition as FR
# font=cv2.FONT_HERSHEY_SIMPLEX
import arduino
import faceRecoghwk

import serial
arduinoData = serial.Serial("COM11", 9600)

assistant = AI()
# WAKE = "Samaritan"

def doSomething():
    command = ""
    while True:
        command = assistant.listen()
        # initial = assistant.listen()

        if (command.count("thank") > 0) or ("samaritan" in command and command.count("thank") > 0):
            assistant.say("You're welcome Sir.")

        # elif initial.count(WAKE) > 0:
        #     assistant.say("What can I do for you?")
        #     command = assistant.listen()
        #     command = command.lower()
        #     if command.count("goodbye") > 0:
        #         break

        command = command.lower()

        if "samaritan" in command and command.count("light") > 0:
            if ("all" in command and "off" in command) or ("both" in command and "off" in command):
                assistant.say("Turning off both lights")
            elif ("all" in command and "on" in command) or ("both" in command and "on" in command):
                assistant.say("Turning on both lights")
            elif "red" in command and "on" in command:
                assistant.say("Turning on the red light")
            elif "red" in command and "off" in command:
                assistant.say("Turning off the red light")
            elif "yellow" in command and "on" in command:
                assistant.say("Turning on yellow light")
            elif "yellow" in command and "off" in command:
                assistant.say("Turning off yellow light")
            arduino.send_command(arduinoData, command)
            

        elif "samaritan" in command and command.count("temperature") > 0:
            assistant.say("I am Getting live temperature updates of your room")
            arduino.send_command(arduinoData, command)
            temperature, hum = arduino.visualize(arduinoData)
            assistant.say(f"The sensor is registering a temperature of {temperature} degrees celsius and a humidity of {hum} percent")
            print(temperature, hum)

        elif "samaritan" in command and command.count("fan") > 0:
            if "on" in command:
                assistant.say("Turning on fan")
            elif "off" in command:
                assistant.say("Turning off fan")
            arduino.send_command(arduinoData, command)

        elif "samaritan" in command and command.count("door"):
            if "open" in command:
                assistant.say("Opening door")
            elif "close" in command:
                assistant.say("CLosing door")
            arduino.send_command(arduinoData, command)

        elif "samaritan" in command and command.count("goodbye")>0:
            assistant.say("Goodbye Master, I'm going to sleep now")
            break


assistant.say("Initializing Samaritan")
assistant.say("Recognizing Face")
assistant.say("Press q on the keyboard to quit the webcam")
userName = faceRecoghwk.recognizeFace()
if userName == "Jeffrey Asiedu":
    assistant.say("Access Granted. Hello Master Jeffrey, welcome back. I am at your service")
    doSomething()
else:
    assistant.say("Access Denied. Intruder detected, Shutting down system")

