from map import Map
from helicopter import Helicopter as Helico
from clouds import Clouds
import time
import os
from pynput import keyboard
import json

TICK_SLEEP = 0.1
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
tick = 1

MOVES = {'w':(-1, 0), 'd':(0, 1), 's':(1, 0), 'a':(0, -1)}
#f- save; g - restore
def process_key(key):
    global helico, tick, clouds, field
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
    elif c == 'f':
        data = {"helicopter": helico.export_data(),
                "clouds": clouds.export_data(),
                "field": field.export_data(),
                "tick": tick}
        with open("level.json", "w") as lvl:
            json.dump(data, lvl)
    elif c == 'g':
        with open("level.json", "r") as lvl:
            data = json.load(lvl)
            helico.import_data(data["helicopter"])
            tick = data["tick"] or 0
            field.import_data(data["field"])
            clouds.import_data(data["clouds"])


#   if key == keyboard.Key.esc:
#        #Stop listener
#        return False

listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()


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
        field.update_fires(helico)
    if tick % CLOUDS_UPDATE == 0:
        clouds.update()

#    exit(0)dddddwwwwwsssssfg
