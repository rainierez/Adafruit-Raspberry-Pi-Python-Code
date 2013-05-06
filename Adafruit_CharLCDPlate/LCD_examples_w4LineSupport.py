#!/usr/bin/python

#----------------------------------------------------------------
# Author: Chris Crumpacker                               
# Date: May 2013
#
# A demo of some of the built in helper functions of 
# the Adafruit_CharLCDPlate.py and Using the EoL_HandlingAnd4LineSupport.py
# 
# Using Adafruit_CharLCD code with the I2C and MCP230xx code as well
#----------------------------------------------------------------

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from LCD_EoL_HandlingAnd4LineSupport import LCD_EoL_Handling

lcd = Adafruit_CharLCDPlate()
eol = LCD_EoL_Handling()

numcolumns = 20
numrows = 4

lcd.begin(numcolumns, numrows)

lcd.backlight(lcd.ON)
eol.message("LCD 20x4\nDemonstration")
sleep(2)

while True:
    #Text on each line alone.
    lcd.clear()
    lcd.setCursor(0,0)
    eol.message("Line 1")
    sleep(1)
    
    lcd.clear()
    lcd.setCursor(0,1)
    eol.message("Line 2")
    sleep(1)
    
    lcd.clear()
    lcd.setCursor(0,2)
    eol.message("Line 3")
    sleep(1)
    
    lcd.clear()
    lcd.setCursor(0,3)
    eol.message("Line 4")
    sleep(1)
    
    # Using the "\n" new line marker
    lcd.clear()
    lcd.setCursor(0,0)
    eol.message("Line 1")
    sleep(1)
    
    lcd.clear()
    lcd.setCursor(0,0)
    eol.message("Line 1\nLine 2")
    sleep(1)
    
    lcd.clear()
    lcd.setCursor(0,0)
    eol.message("Line 1\nLine 2\nLine 3")
    sleep(1)
    
    lcd.clear()
    lcd.setCursor(0,0)
    eol.message("Line 1\nLine 2\nLine 3\nLine 4")
    sleep(1)
        
    # Auto line limiting by length as to not overflow the display
    # This is line by line and does not to any caraige returns
    lcd.clear()
    lcd.setCursor(0,0)
    eol.message("This String is 33 Characters long",1)
    sleep(2)    
    
    lcd.clear()
    lcd.setCursor(0,0)
    eol.message("This String has elpise",2)
    sleep(2)    
    
    #Scroll text to the right
    messageToPrint = "Scrolling Right"
    i=0
    while i<20:
        lcd.clear()
        lcd.setCursor(0,0)
        suffix = " " * i
        eol.message(suffix + messageToPrint,0)
        sleep(.25)
        i += 1
    
    # Scroll test in from the Left
    messageToPrint = "Scrolling Left"
    i=20
    while i>=0:
        lcd.clear()
        lcd.setCursor(0,0)
        suffix = " " * i
        eol.message(suffix + messageToPrint,0)
        sleep(.25)
        i -= 1
    sleep(2) 
    
    # Printing text backwards, NOT right justified
    lcd.clear()
    lcd.setCursor(0,0)
    eol.message("Right to left:")
    lcd.setCursor(10,1)
    lcd.rightToLeft()
    eol.message("Testing")
    sleep(2)
    
    # Printing normally from the middle of the line
    lcd.clear()
    lcd.setCursor(0,0)
    eol.message("Left to Right:")
    lcd.setCursor(10,1)
    lcd.message("Testing")
    sleep(2)
    
    # Enabling the cursor and having it blink
    lcd.clear()
    lcd.setCursor(0,0)
    lcd.cursor()
    lcd.blink()
    eol.message("Cursor is blinking")
    lcd.setCursor(0,1)
    sleep(3)
    lcd.noCursor()
    lcd.noBlink()
    
    # Turning the backlight off and showing a simple count down
    lcd.clear()
    lcd.setCursor(0,0)
    eol.message("Backlight off in")
    lcd.setCursor(0,3)
    eol.message("Back on in 3sec")
    lcd.setCursor(17,0)             #Reseting the cursor here keeps us from having to clear the screen, this over writes the previous character
    eol.message("3")
    sleep(1)
    
    lcd.setCursor(17,0)
    eol.message("2")
    sleep(1)
    
    lcd.setCursor(17,0)
    eol.message("1")
    sleep(1)
    
    lcd.backlight(lcd.OFF)
    lcd.clear()
    lcd.setCursor(0,0)
    sleep(3)
    lcd.backlight(lcd.ON)
    eol.message("Backlight on")    
