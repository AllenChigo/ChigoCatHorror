import time
import random

def creepy_cat_logic():
    distance = 15.0
    while distance > 0:
        event = random.choice(["STALK", "HISS", "FREEZE"])
        
        if event == "STALK":
            move = random.uniform(1.5, 3.5)
            distance -= move
            yield f"👣 ...creak... It's {max(0, distance):.1f}m away."
        elif event == "HISS":
            yield "🐍 HHHHHHHHH!! It arches its back in the dark."
        else:
            yield "👁️  It stops. Total silence in the hallway."
            time.sleep(1)
            
    yield "🦴 COLD CONTACT. It's got your ankle."

# To run it:
for moment in creepy_cat_logic():
    print(moment)
    time.sleep(0.8)
