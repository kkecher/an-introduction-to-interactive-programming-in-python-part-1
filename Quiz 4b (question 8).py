import simplegui

space_pos = [0, 0]
space_vel = [0.1, 0.1]
space_acc = [0, 0]

def key_down_handler(key):
    if key == simplegui.KEY_MAP['up']:
        space_acc[0]+=0.08
        space_acc[1]+=0.02
    space_vel[0]+=space_acc[0]
    space_vel[1]+=space_acc[1]
        
def draw_handler(canvas):
    space_pos[0]+= space_vel[0]
    space_pos[1]+= space_vel[1]
    canvas.draw_circle(space_pos, 5, 1, 'Orange', 'Yellow')

frame = simplegui.create_frame('Where is your rocket, cowboy', 800, 800)
frame.set_draw_handler(draw_handler)
frame.start()
frame.set_keydown_handler(key_down_handler)
