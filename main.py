from djitellopy import Tello
import time

drone = Tello()
drone.connect()

print("Battery: " + str(drone.get_battery()) + "%")

drone.takeoff()
# 230 cm height
# circle diameter: 210
drone.move_up(50)
drone.move_forward(100)
drone.move_down(110)
drone.land()

print("Flight Time: " + str(drone.get_flight_time()) )
