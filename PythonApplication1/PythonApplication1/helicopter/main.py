from map import Map
from helicopter import Helicopter as Helico
from clouds import Clouds
import time
import os
from pynput import keyboard

TICK_SLEEP = 0.4
TREE_UPDATE = 50
FIRE_UPDATE = 100
CLOUDS_UPDATE = 100
MAP_W, MAP_H = 10, 6

field = Map(MAP_W, MAP_H)
fl = False
while not fl:
    fl = field.add_fire()

helico = Helico(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)

MOVES = {'w':(-1, 0), 'd':(0, 1), 's':(1, 0), 'a':(0, -1)}
def process_key(key):
    global helico
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
#   if key == keyboard.Key.esc:
#        #Stop listener
#        return False

listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()

tick = 1
while True:
    print(helico.x, helico.y)
    os.system("cls")
    helico.print_stats()
    field.print_map(helico, clouds)
    print("TICK:", tick)
    field.process_helico(helico, clouds)
    tick += 1
    time.sleep(TICK_SLEEP)
    if tick % TREE_UPDATE == 0:
        field.generate_tree()
    if tick % FIRE_UPDATE == 0:
        field.update_fires()
    if tick % CLOUDS_UPDATE == 0:
        clouds.update()

#    exit(0)
