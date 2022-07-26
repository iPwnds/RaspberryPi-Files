import machine

ButtonA = machine.Pin(0,machine.Pin.IN,machine.Pin.PULL_DOWN)
ButtonB = machine.Pin(1,machine.Pin.IN,machine.Pin.PULL_DOWN)

Buzzer = machine.PWM(machine.Pin(15))
Buzzer.duty_u16(32767)
Frequency = 1000

def ButtonIRQHandler(pin):
    global Frequency
    if pin == ButtonA:
        if Frequency < 2000:
            Frequency += 50
    elif pin == ButtonB:
        if Frequency > 100:
            Frequency -= 50
            
ButtonA.irq(trigger = machine.Pin.IRQ_RISING,
            handler = ButtonIRQHandler)
ButtonB.irq(trigger = machine.Pin.IRQ_RISING,
            handler = ButtonIRQHandler)

while True:
    Buzzer.freq(Frequency)