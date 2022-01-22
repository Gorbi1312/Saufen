import pyautogui as pg
import time

print ("Hello World")

time.sleep(10)

txt = open('Saufen.txt')

a = "Heute wird richtig"

for i in txt:
    pg.write(a+' '+i)
    pg.press('Enter')
