from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Mestre
# Sending



def sendData(data):
    hub.ble.broadcast(data=data)


hub = PrimeHub(broadcast_channel=1)
sendData(10)