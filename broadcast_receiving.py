from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Color, Port
from pybricks.tools import wait
from Chassi import Chassi
# Initialize the hub.
chassi = Chassi()

hub = PrimeHub(observe_channels=[1])

while True:
    # Receive broadcast from the other hub.

    data = hub.ble.observe(1)

    if data is None:
        # No data has been received in the last 1 second.
        hub.light.on(Color.RED)
        chassi.drive(velocidade=0, turn=0, buzina=False, seta="")
    else:
        # Data was received and is less that one second old.
        hub.light.on(Color.GREEN)
        chassi.drive(
            velocidade=data[0],
            turn=data[1],
            buzina=data[2],
            seta=data[3]
        )
        

    # Broadcasts are only sent every 100 milliseconds, so there is
    # no reason to call the observe() method more often than that.
    wait(100)


