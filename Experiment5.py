import machine

LED1 = machine.Pin(25,machine.Pin.OUT)
LED2 = machine.Pin(10,machine.Pin.OUT)

ButtonA = machine.Pin(0,machine.Pin.IN,machine.Pin.PULL_DOWN)
ButtonB = machine.Pin(1,machine.Pin.IN,machine.Pin.PULL_DOWN)

LEDstate1 = False
LEDstate2 = False

def ButtonAIRQHandler(pin):
    global LEDstate1
    if pin == ButtonA:
        if LEDstate1 == True:
            LEDstate1 = False
        else:
            LEDstate1 = True
            
def ButtonBIRQHandler(pin):
    global LEDstate2
    if pin == ButtonB:
        if LEDstate2 == True:
            LEDstate2 = False
        else:
            LEDstate2 = True

ButtonA.irq(trigger = machine.Pin.IRQ_RISING,
            handler = ButtonAIRQHandler)
ButtonB.irq(trigger = machine.Pin.IRQ_RISING,
            handler = ButtonBIRQHandler)

while True:
    LED1.value(LEDstate1)
    LED2.value(LEDstate2)