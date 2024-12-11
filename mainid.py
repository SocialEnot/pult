import toga
from colosseum import CSS
from pyviera import Viera

tvs = Viera.discover()

def set_channel(widget):
    global tvs
    channel = int(widget.label)
    print("Changing to channel {0}".format(channel))
    tvs[0].num(channel)

def mute(widget):
    global tvs
    tvs[0].mute()

def build(app):
    row_c = toga.Box()
    
    row_c.add(toga.Button('mute', on_press=mute))
    row_c.style.set(flex_direction='row', margin=5, padding_left=60)


    row_0 = toga.Box()
    
    row_0.add(toga.Button('1', on_press=set_channel))
    row_0.add(toga.Button('2', on_press=set_channel))
    row_0.add(toga.Button('3', on_press=set_channel))
    row_0.style.set(flex_direction='row', margin=5)
    
    row_1 = toga.Box()
    
    row_1.add(toga.Button('4', on_press=set_channel))
    row_1.add(toga.Button('5', on_press=set_channel))
    row_1.add(toga.Button('6', on_press=set_channel))
    row_1.style.set(flex_direction='row', margin=5)
    
    row_2 = toga.Box()
    
    row_2.add(toga.Button('7', on_press=set_channel))
    row_2.add(toga.Button('8', on_press=set_channel))
    row_2.add(toga.Button('9', on_press=set_channel))
    row_2.style.set(flex_direction='row', margin=5)
    
    row_3 = toga.Box()
    
    row_3.add(toga.Button('0', on_press=set_channel))
    row_3.style.set(flex_direction='row', margin=5, padding_left=60)
    
    box = toga.Box()
    box.style.set(flex_direction='column', padding_top=60, padding_left=100)
    box.add(row_c)
    box.add(row_0)
    box.add(row_1)
    box.add(row_2)
    box.add(row_3)
    return box


if __name__ == '__main__':
    app = toga.App('TV Remote', 'org.tv.remote', startup=build)
    app.main_loop()