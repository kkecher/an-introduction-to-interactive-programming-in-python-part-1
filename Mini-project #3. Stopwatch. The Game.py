# template for "Stopwatch: The Game"
import simplegui

# define global variables
global time
global is_running_timer
global success_click
global total_click

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    minutes = time // 1000 // 60
    minutes_str = str(minutes)
    
    seconds = (time // 1000) % 60
    seconds_str = '0' + str(seconds)
    
    mseconds = (time % 1000) / 100
    mseconds_str = str(mseconds)
    
    time_str = minutes_str + ':' + seconds_str[-2:] + '.' + mseconds_str
    return time_str
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global is_running_timer
    
    timer.start()
    is_running_timer = 1
    
def stop():
    global is_running_timer
    global success_click
    global total_click
    
    if time % 1000 == 0 and is_running_timer:
        success_click += 1
    if is_running_timer:
        total_click += 1
    timer.stop()
    is_running_timer = 0
    
def reset():
    global time
    global is_running_timer
    global success_click
    global total_click
    
    timer.stop()
    time = 0
    is_running_timer = 0
    success_click = 0
    total_click = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 100

# define draw handler
def draw_handler(canvas):
    global time
    global success_click
    global total_click
    
    time_str = format(time)
    canvas.draw_text(time_str, [90, 100], 50, 'white')
    score_str = str(success_click) + '/' + str(total_click)
    canvas.draw_text(score_str, [220, 25], 30, 'white')
    
# create frame
frame = simplegui.create_frame('Stopwatch: The Game', 300, 200)
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)

# register event handlers
start_button = frame.add_button('Start', start, 100)
stop_button = frame.add_button('Stop', stop, 100)
reset_button = frame.add_button('Reset', reset, 100)

# start frame
frame.start()
reset()

# Please remember to review the grading rubric
