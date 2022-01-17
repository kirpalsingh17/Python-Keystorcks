# Importing libraries
from pynput.keyboard import Key, Controller
# Importing Time
import time
# Importing Random number
import random

'''
 Sleep time in time module.
 Execution will be start after 2 second.
 You can increase or decrease it accordingly.
'''
time.sleep(2) 

# Instance of Controller
kb = Controller()

'''
Define function and execution of function
'''
def press(button):
    kb.press(button)
    kb.release(button)

'''
For loop for some specific range
function execution
setting delay of execution
time to sleep
'''
for x in range(10000):
    press(Key.right)
    delay = random.uniform(1, 1)
    time.sleep(delay)