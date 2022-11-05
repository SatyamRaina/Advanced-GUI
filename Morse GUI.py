#Satyam Raina

from tkinter import *                         #to access functions from tkinter
import RPi.GPIO as GPIO                       #assigning RPi.GPIO as GPIO
import time                                   #accessing time related functions

LED = 10
GPIO.setwarnings(False)                       #ignore warnings
GPIO.setmode(GPIO.BOARD)                      # Let the program know hatpin name convention BOARD referring the number of the pin in the plug
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)    #Set pin 10 as output pin with initial stage as low(off)

#Creating a window
win = Tk()
win.title("Morse LED")
win.geometry('300x300')

#Declaring String variable for storing String
text_var = StringVar()      

#Label for implementing display boxes for text input
Box = Label(win, text = "Enter your Text: ", fg="blue")
Box.place(relx = 0.1, rely = 0.1, anchor = 'nw')

#Entry widget asking for user to input text
input = Entry(win, textvariable = text_var, width=50)
input.pack()
input.place(relx = 0, rely = 0.2, anchor = 'nw')

def morseCode(x):
    print(x)
    if (x == 'a'):
        return ".-"
    elif (x == 'b'):
        return "-..."
    elif (x == 'c'):
        return "-.-."
    elif (x == 'd'):
        return "-.."
    elif (x == 'e'):
        return "."
    elif (x == 'f'):
        return "..-."
    elif (x == 'g'):
        return "--."
    elif (x == 'h'):
        return "...."
    elif (x == 'i'):
        return ".."
    elif (x == 'j'):
        return ".---"
    elif (x == 'k'):
        return "-.-"
    elif (x == 'l'):
        return ".-.."
    elif (x == 'm'):
        return "--"
    elif (x == 'n'):
        return "-."
    elif (x == 'o'):
        return "---"
    elif (x == 'p'):
        return ".--."
    elif (x == 'q'):
        return "--.-"
    elif (x == 'r'):
        return ".-."
    elif (x == 's'):
        return "..."
    elif (x == 't'):
        return "-"
    elif (x == 'u'):
        return "..-"
    elif (x == 'v'):
        return "...-"
    elif (x == 'w'):
        return ".--"
    elif (x == 'x'):
        return "-..-"
    elif (x == 'y'):
        return "-.--"
    elif (x == 'z'):
        return "--.."
    elif (x == ' '):
        return "/"
    
#Driver code
def blink():
    global text_var
    num = text_var.get()
    if len(num)>20:
        num = num[0:20]
    print(num)
    for g in num:
        temp = 0.5
        mrs = morseCode(g)
        for val in mrs:
            if(val != ' '):
                if val == '.':
                    GPIO.output(LED, GPIO.HIGH)
                    time.sleep(temp)
                    GPIO.output(LED, GPIO.LOW)
                    time.sleep(temp)
                    print("dot")
                elif(val == '-'):
                    GPIO.output(LED, GPIO.HIGH)
                    time.sleep(3*temp)
                    GPIO.output(LED, GPIO.LOW)
                    time.sleep(temp)
                    print("dash")
            elif(val == "/"):
            #code for spaces
                GPIO.output(LED, GPIO.LOW)
                time.sleep(7*temp)
            else:
            #code for spaces
                GPIO.output(LED, GPIO.LOW)
                time.sleep(3*temp)

#Creating text functions to hold the text input by user
def text():
    my_label = Label(win, text='')            #Label for implementing display boxes for placing text
    my_label.pack(pady=20)                    #using get for returning user input text as string

#Creating a button for taking text from user
get_text = Button(win, text="Blink LED", command = blink)
get_text.place(relx=0.5, rely=0.5, anchor = CENTER)      #Place resizes itself within the frame

win.mainloop()
GPIO.cleanup

#Satyam Raina