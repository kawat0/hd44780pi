import RPi.GPIO as GPIO
from time import sleep
import datetime


class HD44780:

    def __init__(self, pin_rs=7, pin_e=8, pins_db=[25, 24, 23, 18]):
        sleep(0.1)
        GPIO.setwarnings(False)
        self.pin_rs = pin_rs
        self.pin_e = pin_e
        self.pins_db = pins_db
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin_rs, GPIO.OUT)
        GPIO.setup(pin_e, GPIO.OUT)

        for pin in self.pins_db:
            GPIO.setup(pin, GPIO.OUT)

        self.clear()

    def clear(self):

        self.cmd(0x33)
        self.cmd(0x32)
        self.cmd(0x28)
        self.cmd(0x0C)
        self.cmd(0x06)
        self.cmd(0x01)

    def cmd(self, bits, char_mode=False):
        """
        bits -- data
        char_mode -- False for command, True for character
        """
        GPIO.output(self.pin_rs, char_mode)

        for pin in self.pins_db:
            GPIO.output(pin, False)

        if bits&0x10==0x10:
            GPIO.output(self.pins_db[0], True)
        if bits&0x20==0x20:
            GPIO.output(self.pins_db[1], True)
        if bits&0x40==0x40:
            GPIO.output(self.pins_db[2], True)
        if bits&0x80==0x80:
            GPIO.output(self.pins_db[3], True)

        GPIO.output(self.pin_e, True)
        GPIO.output(self.pin_e, False)

        for pin in self.pins_db:
            GPIO.output(pin, False)

        if bits&0x01==0x01:
            GPIO.output(self.pins_db[0], True)
        if bits&0x02==0x02:
            GPIO.output(self.pins_db[1], True)
        if bits&0x04==0x04:
            GPIO.output(self.pins_db[2], True)
        if bits&0x08==0x08:
            GPIO.output(self.pins_db[3], True)

        GPIO.output(self.pin_e, True)
        GPIO.output(self.pin_e, False)

        sleep(0.0015)

    def message(self, text, lcd_line):
        """Define lcd line 1-4 in range"""
        lcd_lines = [0x80, 0xC0, 0x94, 0xD4]
        self.cmd(lcd_lines[lcd_line-1])
        text = text.ljust(20, " ")
        for i in range(20):
            self.cmd(ord(text[i]), True)

if __name__ == '__main__':
    lcd = HD44780()
    def main():

        sleep(1)
        lcd.message("Testing line 1", 1)
        sleep(1)
        lcd.message("Testing line 2", 2)
        sleep(1)
        lcd.message("Testing line 3", 3)
        sleep(1)
        lcd.message("Testing line 4", 4)
        sleep(5)

    try:
        main()
    finally:
        GPIO.cleanup()










