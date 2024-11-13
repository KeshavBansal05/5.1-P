# Import required libraries
from tkinter import *            # Import everything from the tkinter library for GUI
import tkinter.font as FONT       # Import font module from tkinter for customizing fonts
import RPi.GPIO as GPIO           # Import RPi.GPIO to control GPIO pins
from gpiozero import LED          # Import LED from gpiozero for easy LED control

# Setup GPIO mode to BCM numbering
GPIO.setmode(GPIO.BCM)

# Define LEDs on specific GPIO pins
red_led = LED(26)                 # Red LED connected to GPIO pin 26
blue_led = LED(13)                # Blue LED connected to GPIO pin 13
green_led = LED(19)               # Green LED connected to GPIO pin 19

# Initialize the tkinter window
win = Tk()
win.title("LED FLASHER")           # Set window title
myFont = FONT.Font(family='Helvetica', size=14, weight='bold')  # Set font style for buttons

# Define function to toggle the red LED on/off
def redLedToggle():
    if red_led.is_lit:             # Check if the red LED is currently on
        red_led.off()              # Turn off red LED
        redLedButton["text"] = "RED LED ON"  # Update button text
    else:
        red_led.on()               # Turn on red LED
        redLedButton["text"] = "RED LED OFF" # Update button text
    # Ensure other LEDs are turned off when red LED is toggled
    blue_led.off()
    blueLedButton["text"] = "BLUE LED ON"
    green_led.off()
    greenLedButton["text"] = "GREEN LED ON"

# Define function to toggle the blue LED on/off
def blueLedToggle():
    if blue_led.is_lit:            # Check if the blue LED is currently on
        blue_led.off()             # Turn off blue LED
        blueLedButton["text"] = "BLUE LED ON"  # Update button text
    else:
        blue_led.on()              # Turn on blue LED
        blueLedButton["text"] = "BLUE LED OFF" # Update button text
    # Ensure other LEDs are turned off when blue LED is toggled
    red_led.off()
    redLedButton["text"] = "RED LED ON"
    green_led.off()
    greenLedButton["text"] = "GREEN LED ON"

# Define function to toggle the green LED on/off
def greenLedToggle():
    if green_led.is_lit:           # Check if the green LED is currently on
        green_led.off()            # Turn off green LED
        greenLedButton["text"] = "GREEN LED ON" # Update button text
    else:
        green_led.on()             # Turn on green LED
        greenLedButton["text"] = "GREEN LED OFF" # Update button text
    # Ensure other LEDs are turned off when green LED is toggled
    red_led.off()
    redLedButton["text"] = "RED LED ON"
    blue_led.off()
    blueLedButton["text"] = "BLUE LED ON"

# Define function to close the application and clean up GPIO
def close():
    GPIO.cleanup()                 # Reset GPIO pins to default state
    win.destroy()                  # Close the tkinter window

# Create buttons to control each LED and exit the application
redLedButton = Button(win, text="RED LED ON", font=myFont, command=redLedToggle, bg='red', height=2, width=30)
redLedButton.grid(row=0, column=1)  # Place red LED button in the GUI

blueLedButton = Button(win, text="BLUE LED ON", font=myFont, command=blueLedToggle, bg='blue', height=2, width=30)
blueLedButton.grid(row=1, column=1) # Place blue LED button in the GUI

greenLedButton = Button(win, text="GREEN LED ON", font=myFont, command=greenLedToggle, bg='green', height=2, width=30)
greenLedButton.grid(row=2, column=1) # Place green LED button in the GUI

exitButton = Button(win, text="EXIT", font=myFont, command=close, bg='yellow', height=2, width=30)
exitButton.grid(row=3, column=1)     # Place exit button in the GUI

# Handle window close event
win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()                       # Run the tkinter main loop to display the window
