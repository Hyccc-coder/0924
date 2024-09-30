let 猜拳 = 0
input.onButtonPressed(Button.A, function () {
    music.stopMelody(MelodyStopOptions.All)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    if (猜拳 == 1) {
        basic.showIcon(IconNames.Pitchfork)
    } else if (猜拳 == 2) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.SmallSquare)
    }
})
basic.forever(function () {
    猜拳 = randint(1, 3)
})
