import simplegui

circle_pos = [10, 20]
circle_move = [0, 0]

def key_down_handler(key):
    global circle_move
    if key == simplegui.KEY_MAP['up']:
        circle_move = [3, 0.7]
    if key == simplegui.KEY_MAP['down']:
        circle_move = [-3, -0.7]
        
def key_up_handler(key):
    global circle_move
    if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']:
        circle_move = [0, 0]
    

def draw_handler(canvas):
    circle_pos[0]+= circle_move[0]
    circle_pos[1]+= circle_move[1]
    canvas.draw_polygon([(50, 50), (180, 50), (180,140), (50, 140)],
                        3, 'Blue', 'Lime')
    canvas.draw_circle(circle_pos, 5, 1, 'Orange', 'Yellow')
    if int(circle_pos[0]) in range(50, 180) and int(circle_pos[1]) in range(50, 140):
        canvas.draw_text('Boom!', (75, 100), 30, 'Red')


frame = simplegui.create_frame('Do they match?', 300, 300)
frame.set_draw_handler(draw_handler)
frame.start()
frame.set_keydown_handler(key_down_handler)
frame.set_keyup_handler(key_up_handler)
