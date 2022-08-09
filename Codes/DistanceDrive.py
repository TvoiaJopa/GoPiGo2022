# import the modules
from di_sensors.easy_distance_sensor import EasyDistanceSensor
from time import sleep
import time
from easygopigo3 import EasyGoPiGo3
import enum


# creating enumerations using class
class coordinateAxes(enum.Enum):
	x = 1
	y = 2
	xNeg = 3
	yNeg = 4


class Coordinate(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return 'Coordinate({0.x:d},{0.y:d})'.format(self)


gpg = EasyGoPiGo3()
coorAxes = coordinateAxes.x

def MoveForward(num):
	gpg.drive_cm(num)
	if coorAxes == coordinateAxes.x:
		coordinate.x = coordinate.x + num
	elif coorAxes == coordinateAxes.y:
		coordinate.y = coordinate.y + num
	elif coorAxes == coordinateAxes.xNeg:
		coordinate.x = coordinate.x - num
	elif coorAxes == coordinateAxes.yNeg:
		coordinate.y = coordinate.y - num
	print("coordinate: {} cm".format(coordinate))

def CoordinateTurn():
	if coorAxes == coordinateAxes.x:
		coorAxes = coordinateAxes.y
	elif coorAxes == coordinateAxes.y:
		coorAxes = coordinateAxes.xNeg
	elif coorAxes == coordinateAxes.xNeg:
		coorAxes = coordinateAxes.yNeg
	elif coorAxes == coordinateAxes.yNeg:
		coorAxes = coordinateAxes.x
	gpg.turn_degrees(90)



normal_speed = 250
noob_speed = 100
# rotate the servo at 160 degrees

# instantiate the distance object
my_sensor = EasyDistanceSensor()
# and read the sensor iteratively

coordinate = Coordinate(0, 0)

print("VLotage:{} ".format(gpg.volt()))

while True:
    read_distance = my_sensor.read()
    print("distance from object: {} cm".format(read_distance))

    if read_distance > 50:
        gpg.set_speed(normal_speed)
        MoveForward(10)

    elif read_distance > 20:
        gpg.set_speed(noob_speed)
        MoveForward(10)

    else:
        CoordinateTurn()

    sleep(0.1)