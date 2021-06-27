from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT
from datetime import datetime
import time
import os
import subprocess






import tkinter as tk    
import time  
import threading  
import os  
switch = True  
root = tk.Tk()  
  
  
def ClearScreen():    
    global switch  
    switch = True
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=4, block_orientation=-90, blocks_arranged_in_reverse_order=True)
    device.contrast(16)
    device.cleanup
    

def speak():    
    subprocess.Popen(["nohup","python3", "/home/pi/max7219/ledmatrix2.py"])
    global switch  
    switch = False

def stop():
    os.system('sudo pkill -f /home/pi/max7219/ledmatrix2.py')
    global switch  
    switch = False


      
        
def kill():    
    root.destroy()    
        
clearbutton = tk.Button(root, text = "Clear Screen", command =  ClearScreen)   
clearbutton.pack() 


speakbutton =  tk.Button(root, text = "speak", command = speak)    
speakbutton.pack() 

stopbutton =  tk.Button(root, text = "stop", command = stop)    
stopbutton.pack() 
   
killbutton = tk.Button(root, text = "EXIT", command = kill)    
killbutton.pack()    
        
root.mainloop() 
