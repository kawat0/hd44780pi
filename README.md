hd44780pi
=========

Python3 library for sending text strings to a 4x20 HD44780 LCD display with Raspberry Pi

##Usage

```python
    from hd44780pi import HD44780
    
    lcd = HD44780()
    
    sleep(1)
    lcd.message("Testing line 1", 1)
    sleep(1)
    lcd.message("Testing line 2", 2)
    sleep(1)
    lcd.message("Testing line 3", 3)
    sleep(1)
    lcd.message("Testing line 4", 4)
    sleep(5)
```
