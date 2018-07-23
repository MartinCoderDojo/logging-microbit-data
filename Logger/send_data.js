basic.showString("Starting")
basic.forever(() => {
    serial.writeLine("" + input.temperature() + " " + input.lightLevel())
    basic.pause(100)
})
