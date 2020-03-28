# # permashadow
# Keeping Shadow From Automatically Shutting Down by Imitating User Activity
#
# ## Strategy
# We'll use PyUserInput's PyMouse to check the mouse's current position, automatically click a location on the screen at some specified time interval, and then return the mouse back to the position it was at before the click. We'll keep this loop going only for a while; it's rude and could potentially get me in trouble if I keep my Shadow running indefinitely.
#
# ## Dependencies

# +
# for tracking time
import time
from datetime import timedelta

# for tracking and automating control of mouse
from pymouse import PyMouse

# mouse controls
mouse = PyMouse()

# helper functions
def waitfor(seconds):
    "wait for an arbitrary number of seconds"
    if type(seconds) is not int and type(seconds) is not float:
        seconds = seconds.seconds
    timeout = time.time() + seconds
    while time.time() < timeout:
        pass
    
def click(x, y):
    "click a point on the screen"
    mouse.press(x,y,1)
    waitfor(.25)
    mouse.release(x,y,1)
    waitfor(.25)

# parameters
target_position = (1364, 1131)
click_interval = 30
duration = 3 * 60 * 60
# -

# ## Main Loop

# +
timeout = time.time() + duration

while time.time() < timeout:
    waitfor(click_interval)
    current_position = mouse.position()
    click(*target_position)
    mouse.move(*current_position)
# -

# ## Testing
# To test, we must first figure out how long it takes for shadow to attempt to close (presumably 30 minutes). It's 2:45 now. Note when the timeout menu appears.


