import machine
import utime
import _thread

ButtonA = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)
ButtonB = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_DOWN)

Red = machine.Pin(10, machine.Pin.OUT)
Yellow = machine.Pin(11, machine.Pin.OUT)
Green = machine.Pin(12, machine.Pin.OUT)
PedestrianRed = machine.Pin(6, machine.Pin.OUT)
PedestrianWait = machine.Pin(7, machine.Pin.OUT)
PedestrianGreen = machine.Pin(8, machine.Pin.OUT)

Buzzer = machine.PWM(machine.Pin(15))
Buzzer.duty_u16(0)
Frequency = 1000

CrossRequested = False

def PedestrianCross():
    global CrossRequested
    PedestrianRed(0)
    PedestrianGreen(1)
    PedestrianWait(0)
    OnTime = 50
    print("Beeping")
    for Beeping in range (10):
        Buzzer.duty_u16(32767)
        utime.sleep_ms(OnTime)
        Buzzer.duty_u16(0)
        utime.sleep_ms(1000-OnTime)
    print("End Beeping Thread")
    PedestrianRed(1)
    PedestrianGreen(0)
    CrossRequested = False

def ButtonIRQHandler(pin):
    global CrossRequested
    if CrossRequested == False:
        print("Button Pressed")
        CrossRequested = True
        PedestrianWait.value(1)
        
ButtonA.irq(trigger = machine.Pin.IRQ_RISING, handler = ButtonIRQHandler)
ButtonB.irq(trigger = machine.Pin.IRQ_RISING, handler = ButtonIRQHandler)

Red.value(1)
Yellow.value(0)
Green.value(0)
PedestrianRed.value(1)
PedestrianGreen.value(0)
PedestrianWait.value(0)
utime.sleep(2)

while True:
    if CrossRequested == True:
        _thread.start_new_thread(PedestrianCross,())
        while CrossRequested:
            utime.sleep(1)
    else:
        Yellow.value(1)
        utime.sleep(1)
        Red.value(0)
        Yellow.value(0)
        Green.value(1)
        utime.sleep(2)
        Yellow.value(1)
        Green.value(0)
        utime.sleep(1)
        Red.value(1)
        Yellow.value(0)
        utime.sleep(2)
        