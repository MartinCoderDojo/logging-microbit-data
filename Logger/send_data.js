let item = 0
basic.showString("Starting")
item = 0
basic.forever(() => {
    serial.writeLine("" + item + " " + input.temperature() + " " + input.lightLevel())
    item += 1
    basic.pause(100)
})
