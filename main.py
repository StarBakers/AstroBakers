##############################################################
########################## The *Bakers #######################
######################### (AstroBakers) ######################
#########################      2021    ####################### 
##############################################################
##  We reduce processing in the program to reduce the load  ##
##  we perform no conversion in the program itself          ##
##  Any required processing will be done offline by         ##
##  already developed appropriate parser                    ##
##  keeping main program as simple as possible              ##
##############################################################
##         We use all the sensors but the camera            ##
# (we found it miningless due to the usage of the LED display#
##  In addition to our main mission (plot/study of earth's ###
## magnetic field from AstroPi measurements), we will take  ##
# pressure/humidity/tempature measurements to assess life in #
# space (ISS) and acceleration/gyro measurements to assess  ##
##     ISS trajectory accuacy.                              ##
## Data will be stored in data.csv file in current directory #
##               same for errors.log file                   ##
##############################################################
##     This program is released under the MIT Licence       ##
##############################################################

#Import required libraries
from ephem import readtle,degree #to track ISS trajectory
from gpiozero import CPUTemperature #to measure CPU Temperature - will be used to assess its influence in temperature measuremennts 
import datetime #to record date/time and calculate running time
from time import sleep #for "pausing" between measurements
from sense_hat import SenseHat #to interact with SenseHat
from pathlib import Path#to obtain current path
import csv #to store results in csv file 
from logzero import logger, logfile #to log errors (if any)

#Initialise ephemeral data with latest TLE data for ISS location - last updated 22/01
name = "ISS (ZARYA)"             
ephem1 = "1 25544U 98067A   21022.22515229 -.00006244  00000-0 -10577-3 0  9996"
ephem2 = "2 25544  51.6469 344.6609 0002238 275.3350 157.6252 15.48872772265973"

#color variables attributed to be used to LED display
#bright colours (eg white) have been deliberately avoided
G = (0, 255, 0) #Green
B = (0, 0, 255) #Blue
R = (255, 0, 0) #Red
O = (0,0,0)     #no light will be emitted here

#code below is the mapping of the LED lighting
def Terminate():# Will display a red X when program terminates
    logo = [
    R, O, O, O, O, O, O, R,
    O, R, O, O, O, O, R, O,
    O, O, R, O, O, R, O, O,
    O, O, O, R, R, O, O, O,
    O, O, O, R, R, O, O, O,
    O, O, R, O, O, R, O, O,
    O, R, O, O, O, O, R, O,
    R, O, O, O, O, O, O, R,
    ]
    return logo

#same function as above, but indicates the program is working
#it will display an arrow
def Working1():
    logo = [
    O, O, O, B, B, O, O, O,
    O, O, O, B, B, O, O, O,
    O, O, O, B, B, O, O, O,
    O, B, B, G, G, B, B, O,
    O, B, B, G, G, B, B, O,
    O, O, B, B, B, B, O, O,
    O, O, O, B, B, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

#same function as above, but it will display an arrow to the opposite direction
#the two arrows will be interghanged while program runs to indicate ongoing execution
def Working2():
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, B, B, O, O, O,
    O, O, B, B, B, B, O, O,
    O, B, B, G, G, B, B, O,
    O, B, B, G, G, B, B, O,
    O, O, O, B, B, O, O, O,
    O, O, O, B, B, O, O, O,
    O, O, O, B, B, O, O, O,
    ]
    return logo

#The function to identify ISS location
def iss_location(iss):
    iss.compute()
    return(iss.sublat,iss.sublong)

#will be used to append data in csv file
def add_data_in_csv(csv_file,data):
    with open(csv_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

# the main function
def main():
    start_time = datetime.datetime.now() #create a datetime variable to store the start time - will be used for comparative reasons
    sleep_time = 1 #time between measurements - in seconds - easier to spot it for changes if here
    ## we found that measurements per 1 sec still produce csv file well beyond the limit
    ## plus they provide more accurate trajectory of the ISS
    
    dir_path = Path(__file__).parent.resolve() #get the current path; will be used for csv and error log files 
    
    #Config the error logginf file
    logfile(dir_path/'errors.log',maxBytes=1e6, backupCount=10)#rotating log file - normaly won't be needed
   
    #read ISS TLE data
    iss = readtle(name, ephem1, ephem2)

    # Set up Sense Hat
    sensors = SenseHat()
    sensors.set_imu_config(True, True, True)  # Enable compass, gyroscope and accelerometer

    #create csv file and open it (write at first)
    data_file = dir_path/'data.csv'
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = ("Date/time","Latitude","Longitude","Pressure","Humidity","Temperature","Acceleration","Gyroscope","Magnetometer","Orientation","CPU Temperature") # these will be the headers of the csv
        writer.writerow(header)#write the CSV header

    # create a datetime variable to store the current time - will also be used for checking running time
    current_time = datetime.datetime.now()

    images = [Working1, Working2]#the two images to be displayed interchagably while the program runs
    count = 0#sets the count variable to 0, essential to interchange image on LED display while program runs

    while (current_time < start_time + datetime.timedelta(minutes=175)):#5 min margin - is more than enough 
        try:
            sensors.set_pixels(images[count % len(images)]())#using modulo we interchange the LED display as program runs
            latitude, longitude = iss_location(iss) #get the ISS coordinates
            pressure = sensors.get_pressure() #pressure in millibars
            humidity = sensors.get_humidity() #percentage (%) of relative humidity
            temperature_p = sensors.get_temperature_from_pressure() #temperature in Celcius degrees, obtained from pressure sensor - testing showd is closer to real tempersture
            acceleration = sensors.get_accelerometer_raw() ##acceleration (x,y,z) in standard gravities (9.80665m/s²)
            gyroscope = sensors.get_gyroscope_raw() #gyrsocope values in radians per second
            magnetometer = sensors.get_compass_raw() #magnetometer values in micro-Teslas
            orientation = sensors.get_orientation_degrees()#orientation measured in degrees
            row = (current_time,latitude,longitude,pressure,humidity,temperature_p,acceleration,gyroscope,magnetometer,orientation,CPUTemperature().temperature) #a record of data to be appended to the CSV file
            add_data_in_csv(data_file,row)#better safe than sorry - append new data to the file continuously
        except Exception as e: #catch any exceptions
            logger.error(f'{e.__class__.__name__}: {e})') #log errors - if any - to understand what happened
        sleep(sleep_time) ##Sleep for <sleep_time> between measurements
        count += 1#increases the count - is used for interchanging image on LED display only - see 1st line after try
        current_time = datetime.datetime.now() #update the current time
    sensors.set_pixels(Terminate()) # now we are outside while loop, display the Terminate (X) image
    
if __name__ == '__main__':
    main()
