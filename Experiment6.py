import machine
import utime
import _thread

ButtonA = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)

Red = machine.Pin(10, machine.Pin.OUT)
Yellow = machine.Pin(11, machine.Pin.OUT)
Green = machine.Pin(12, machine.Pin.OUT)

Buzzer = machine.PWM(machine.Pin(15))
Buzzer.duty_u16(0)
Frequency = 1000

Beeping = False

def Beep():
    global Beeping
    OnTime = 50
    print("Start Beeping Thread")
    while Beeping:
        Buzzer.duty_u16(32767)
        utime.sleep_ms(OnTime)
        Buzzer.duty_u16(0)
        utime.sleep_ms(1000-OnTime)
    print("End Beeping Thread")

def ButtonAIRQHandler(pin):
    global Beeping
    if Beeping == False:
        print("Start Beep")
        Beeping = True
        _thread.start_new_thread(Beep,())
    else:
        Beeping = False
        print("Stop Beep")
        
ButtonA.irq(trigger = machine.Pin.IRQ_RISING, handler = ButtonAIRQHandler)

while True:
    Red.toggle()
    utime.sleep_ms(100)
    Yellow.toggle()
    utime.sleep_ms(100)
    Green.toggle()
    utime.sleep_ms(100)