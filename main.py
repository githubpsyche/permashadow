# # permashadow
# Keeping Shadow From Automatically Shutting Down by Imitating User Activity
#
# ## Strategy
# On the client system, we'll use PyUserInput's PyMouse to check the mouse's current position, automatically click a location on the screen (chosen somewhere the Shadow client window is bound to be open) at some specified time interval, and then return the mouse back to the position it was at before the click. We'll keep this loop going only for a while; it's rude and could potentially get me in trouble if I keep my Shadow running indefinitely.
#
# ## Dependencies

# +
# for displaying "progress"
from IPython.display import display, clear_output

# for tracking time
import time
from datetime import timedelta

# for tracking and automating control of mouse
from pymouse import PyMouse

# mouse controls
mouse = PyMouse()

# helper functions
def waitfor(seconds, annotation=''):
    "wait for an arbitrary number of seconds"
    if type(seconds) is not int and type(seconds) is not float:
        seconds = seconds.seconds
    timeout = time.time() + seconds
    current = time.time()
    clear_output(wait=True)
    if annotation:
        display('{} minutes left with annotation: {}'.format((timeout-time.time())/60, annotation))
    while time.time() < timeout:
        if current + display_update < time.time():
            clear_output(wait=True)
            display('{} minutes left with annotation: {}'.format((timeout-time.time())/60, annotation))
            current = time.time()
    
def click(x, y):
    "click a point on the screen"
    mouse.press(x,y,1)
    waitfor(.25)
    mouse.release(x,y,1)
    waitfor(.25)
    
# parameters
target_position_A = (4120, 530)
target_position_B = (3371, 1186)
click_interval_A = 10 * 60
click_interval_B = 1 * 20
duration = 3 * 60 * 60
display_update = 10
# -

# ## Main Loop

# +
timeout = time.time() + duration

while time.time() < timeout:
    waitfor(click_interval_A, 'A')
    current_position = mouse.position()
    click(*target_position_A)
    print(mouse.position())
    mouse.move(*current_position)
    
    waitfor(click_interval_B, 'B')
    current_position = mouse.position()
    click(*target_position_B)
    click(*target_position_B)
    print(mouse.position())
    mouse.move(*current_position)
# -

# ## Testing
# To test, we must first figure out how long it takes for shadow to attempt to close (presumably 30 minutes). It's 2:45 now. Note when the timeout menu appears.


