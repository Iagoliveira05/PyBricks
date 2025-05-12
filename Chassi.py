from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

class Chassi:
    def __init__(self):
        self.hub = PrimeHub()
        self.LEFT_MOTOR = Motor(port=Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
        self.RIGHT_MOTOR = Motor(port=Port.B)
        self.LEFT_COLOR_SENSOR = ColorSensor(port= Port.C)
        self.RIGHT_COLOR_SENSOR = ColorSensor(port= Port.D)
        ULTRASSONIC_SENSOR = UltrasonicSensor(port= Port.E)
        self.kP = 1
        self.kI = 0.0
        self.kD = 0
        self.last_error = 0.0

        self.chassi = DriveBase(
            left_motor= self.LEFT_MOTOR,
            right_motor= self.RIGHT_MOTOR,
            wheel_diameter= 5.6, # Centimetros
            axle_track= 11.1 # Centimetros
        )
        self.chassi.use_gyro(use_gyro= True)
        self.chassi.heading_control.pid(kp=10,ki=2)
        self.chassi.distance_control.pid(kp=2)
        self.chassi.settings(straight_speed=80,turn_acceleration=800, turn_rate=800)

    def getLeftReflection(self):
        return self.LEFT_COLOR_SENSOR.reflection()

    def getRightReflection(self):
        return self.RIGHT_COLOR_SENSOR.reflection()

    def resetLastError(self):
        self.last_error = 0

    def calculatePID(self, error):
        pGain = error * self.kP
        dGain = (error - self.last_error) * self.kD
        self.last_error = error
        return (pGain + dGain)
 
    def seguirLinha(self, speed=12):
        error = self.getLeftReflection() - self.getRightReflection()
        outputDirection = self.calculatePID(error= error)
        self.chassi.drive(speed, outputDirection)
        print(self.getLeftReflection())

    def virar(self, angulo):
        self.chassi.use_gyro(use_gyro= True)
        
        self.chassi.turn(
            angle= angulo,
            then= Stop.BRAKE
        )
        print(self.chassi.angle())

    def seguirReto(self, distancia): 
        self.chassi.use_gyro(use_gyro= True)
        self.chassi.straight(
            distance= distancia,
            then= Stop.BRAKE
        )
        print(self.chassi.distance())

    def getColorLeft(self):
        return self.LEFT_COLOR_SENSOR.color(surface= True)

    
    def getColorRight(self):
        return self.RIGHT_COLOR_SENSOR.color(surface= True)

    def getHSVColor(self):
        return self.LEFT_COLOR_SENSOR.hsv(surface= True)
