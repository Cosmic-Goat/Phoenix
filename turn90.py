'''import time
import ps_drone                # Imports the PS-Drone-API

drone = ps_drone.Drone()       # Initializes the PS-Drone-API
drone.startup()                # Connects to the drone and starts subprocesses

drone.trim()

drone.takeoff()                # Drone starts
time.sleep(7.5)                # Gives the drone time to start


drone.setSpeed(1.0)            # Sets default moving speed to 1.0 (=100%)
print drone.setSpeed()         # Shows the default moving speed


print "Drone turns 120 degree to the left"
drone.turnAngle (-90, 0.2, 1)


drone.turnLeft()               # Drone moves full speed to the left...
time.sleep(2)                  # ... for two seconds



drone.stop()                   # Drone stops
time.sleep(2)




drone.land()                   # Drone lands'''



import time, sys
import ps_drone  
import json                                   # Import PS-Drone-API

drone = ps_drone.Drone()                           # Start using drone
drone.startup()                                    # Connects to drone and starts subprocesses

drone.reset()                                      # Sets drone's status to good
while (drone.getBattery()[0]==-1): time.sleep(0.1) # Wait until drone has done its reset
print "Battery: "+str(drone.getBattery()[0])+"% "+str(drone.getBattery()[1]) # Battery-status
drone.useDemoMode(False)                           # Give me everything...fast
drone.getNDpackage(["demo","pressure_raw","altitude","magneto","wifi"]) # Packets to decoded
time.sleep(0.5)  
reset   






NDC = drone.NavDataCount
end = False
while not end:
    while drone.NavDataCount==NDC:  time.sleep(0.001) # Wait until next time-unit
    if drone.getKey():              end = True        # Stop if any key is pressed
    NDC=drone.NavDataCount
    print "-----------"
  
    print json.dump("Altitude: "+str(drone.NavData["altitude"][3]))) 

    print json.dump("Battery: "+str(drone.getBattery()[0])+"% "+str(drone.getBattery()[1])) #battery percentage, if battery is too low or not 

    print json.dump( "Windspeed: " +str(drone.getwind_speed()[0])) 


    


    








   


