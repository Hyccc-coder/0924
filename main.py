猜拳 = 0

def on_button_pressed_a():
    music.stop_melody(MelodyStopOptions.ALL)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if 猜拳 == 1:
        basic.show_icon(IconNames.PITCHFORK)
    elif 猜拳 == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SMALL_SQUARE)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global 猜拳
    猜拳 = randint(1, 3)
basic.forever(on_forever)
