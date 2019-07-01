import simplegui

var = 5

def key_down_handler(key):
    global var
    if key == simplegui.KEY_MAP['down']:
        var*=2

def key_up_handler(key):
    global var
    if key == simplegui.KEY_MAP['up']:
        var-=3

def draw_handler(canvas):
    canvas.draw_text(str(var), (100, 170), 100, 'White')

frame = simplegui.create_frame('Guess the what?', 300, 300)
frame.set_draw_handler(draw_handler)
frame.start()
frame.set_keydown_handler(key_down_handler)
frame.set_keyup_handler(key_up_handler)
