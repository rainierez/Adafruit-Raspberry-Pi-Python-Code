#!/usr/bin/python
#----------------------------------------------------------------
# Author: Chris Crumpacker                               
# Date: May 2013
#
# Testing a data table on an 20x4 LCD, 
# using a RaspberyPi and an MCP23017 I2C port expander
# 
# Using Adafruit_CharLCD code with the I2C and MCP230xx code as well
#----------------------------------------------------------------

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from EoL_HandlingAnd4LineSupport import LCD_EoL_Handling

class LCD_DataTable(Adafruit_CharLCDPlate):
    # Limited to 4 characters, 
    # position is left or right, 
    # line is 1-4
    def labelHalf(self, text, position, line):
        if position == "left":
            lcd.setCursor(0,line)
            eol.message("    :")
            lcd.setCursor(0,line)
            eol.message(text[0:4]+':')        
        elif position == "right":
            lcd.setCursor(10,line)
            eol.message("    :")
            lcd.setCursor(10,line)
            eol.message('|'+text[0:4]+':')
            
    # Limited to 4 characters, 
    # position is left or right, 
    # line is 1-4
    def valueHalf(self, text, position, line):
        if position == "left":
            lcd.setCursor(5,line)
            eol.message("    ")
            lcd.setCursor(5,line)
            eol.message(text[0:4])        
        elif position == "right":
            lcd.setCursor(16,line)
            eol.message("    ")
            lcd.setCursor(16,line)
            eol.message(text[0:4])
    
    # Writes up to a 9 character lable and value to a full line
    def wholeLine(self, label, value, line):
        self.clearLine(line)
        lcd.setCursor(0,line)
        eol.message(label[0:10] + ': ')
        lcd.setCursor(11,line)
        eol.message(value[0:10])
    
    #Clears an entire line
    def clearLine(self, line):
        lcd.setCursor(0,line)
        eol.message(" " * columns)
        
    # Clears just a half data set, label and value   
    def clearDataSet(self, position,line):
        if position == "left":
            lcd.setCursor(0,line)
            eol.message(" " * 10)
        elif position == "right":
            lcd.setCursor(10,line)
            eol.message(" " * 10)
    
    # Clears just the value portion for a half data set
    def clearHalfValue(self, position,line):
        if position == "left":
            lcd.setCursor(5,line)
            eol.message("    ")      
        elif position == "right":
            lcd.setCursor(16,line)
            eol.message("    ")

#----------------------------------------------------------------
# Main program, just trowing bogus data "against the wall"
#----------------------------------------------------------------
if __name__ == '__main__':
    
    #lcd size reference
    columns = 20
    rows = 4
    
    eol = LCD_EoL_Handling()
    lcd = Adafruit_CharLCDPlate()
    dt = LCD_DataTable()
    
    lcd.begin(columns, rows)
    lcd.backlight(lcd.ON)
    lcd.clear()
    
    lcd.message("20x4 Table Testing")
    sleep(2)
    
    #Filling the table with bogus info
    lcd.clear()
    dt.labelHalf("Temp","left",0)
    dt.labelHalf("Mode","right",0)
    dt.labelHalf("Targ","left",1)
    dt.labelHalf("Fan","right",1)
    dt.valueHalf("Cool","right",0)
    dt.valueHalf("75.5","left",0)
    dt.valueHalf("Auto","right",1)
    dt.valueHalf("74.0","left",1)
    dt.wholeLine("Tempurature", "Too Hot",2)
    
    #Start testing updating and clearing parts
    sleep(5)
    dt.clearLine(0)
    sleep(2)
    dt.labelHalf("Temp","left",0)
    dt.valueHalf("76.0","left",0)
    sleep(2)
    dt.valueHalf("74.75","left",0)
    sleep(2)
    dt.labelHalf("Mode","right",0)
    dt.valueHalf("Both","right",0)
    sleep(2)
    dt.valueHalf("On","right",0)
    sleep(2)
    dt.clearDataSet("left",0)
    sleep(2)
    dt.labelHalf("Tempurature","left",0)
    dt.valueHalf("85","left",0)
    sleep(5)
