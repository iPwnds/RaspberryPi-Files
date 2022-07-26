import machine

LED = machine.Pin(25,machine.Pin.OUT)
Button = machine.Pin(0,machine.Pin.IN,machine.Pin.PULL_DOWN)
LEDstate = False

def ButtonIRQHandler(pin):
    global LEDstate
    if LEDstate == True:
        LEDstate = False
    else:
        LEDstate = True
        
Button.irq(trigger = machine.Pin.IRQ_RISING,
            handler = ButtonIRQHandler)
while True:
    LED.value(LEDstate)