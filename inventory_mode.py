import game_framework
import game_world
from pico2d import *

image = None


def init():
    global image
    image = load_image('item_select.png')

def finish():
    global image
    del(image)

def update():
    game_world.update()

def render():
    clear_canvas()
    game_world.render()
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.pop_mode()

def pause():
    pass

def resume():
    pass
