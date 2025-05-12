from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task

from Chassi import Chassi
from Anexo import Anexo

async def quadrado():
    for i in range(4):
        await chassi.seguirReto(distancia= 10)
        await chassi.virar(angulo= 90)

def main():
    while True:
        chassi.seguirLinha(speed=12)

chassi = Chassi()


hub = PrimeHub()
hub.imu.reset_heading(0)

run_task(main())


