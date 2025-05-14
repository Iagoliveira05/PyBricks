from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


# Escravo
# Receiving

def receiveData():
    data = hub.ble.observe(1)
    if (data is not None):
        print(data)

hub = PrimeHub(observe_channels=[1, 2])