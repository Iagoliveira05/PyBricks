from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ForceSensor
from pybricks.parameters import Port, Button
from pybricks.tools import wait

# Initialize the hub.
hub = PrimeHub(broadcast_channel=1)
leftTrigger = ForceSensor(port=Port.A)
rightTrigger = ForceSensor(port=Port.E)
buzinaTrigger = ForceSensor(port=Port.C)


velocidade = 0
curva = 0
buzina = False
seta = ""
hub.imu.reset_heading(0)

print("\x1b[H\x1b[3J", end="")
print("\x1b[H\x1b[2J", end="")

while True:
    # Buzina
    if (buzinaTrigger.pressed()):
        buzina = True
    else:
        buzina = False

    if (leftTrigger.pressed(force=1)): # Ré
        velocidade = leftTrigger.force() * -200

    elif (rightTrigger.pressed()): # Frente
        velocidade = rightTrigger.force() * 200

    else: # Parado
        velocidade = 0


    if (Button.LEFT in hub.buttons.pressed()):
        seta = "left"
    elif (Button.RIGHT in hub.buttons.pressed()):
        seta = "right"
    else:
        seta = ""

    curva = hub.imu.heading() * 2

    data = (velocidade, curva, buzina, seta)

    
    hub.ble.broadcast(data)

    # Broadcasts are only sent every 100 milliseconds, so there is no reason
    # to call the broadcast() method more often than that.
    wait(100)
