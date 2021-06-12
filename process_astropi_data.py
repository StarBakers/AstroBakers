#######################################################
##################### The *Bakers #####################
#################### (AstroBakers) ####################
#######################################################
## This script will parse the data collected by the  ##
## main program, remove unnecessary text and convert ##
## them to appropriate for further processing csv    ##
## file.                                             ##
#######################################################
import csv #to store results in csv file 
import json
import argparse
import math

#this function converts dms coordinates to degrees
def dms_to_dd(d, m, s):
    dd = d + float(m)/60 + float(s)/3600
    return dd

#this function converts a string formatted in a dictionary-like format to a dictionary
def convert_string_to_dict(input_string):
    json_string = input_string.replace("'","\"",6) #we need to replace single with double quotes to have a json format string
    dictionary = json.loads(json_string) #converts automatically json string to dictionary
    return dictionary

#this function creates a tuple getting as an input 3 values
#first input is a string, which is first converted to a dictionary
#and then the values of the dictionaries are obtained, rounded, to create the tuple. 
def create_tuple(header,key1,key2,key3):
    header_dict = convert_string_to_dict(header)
    header_x = round(header_dict[key1],3)
    header_y = round(header_dict[key2],3)
    header_z = round(header_dict[key3],3)
    return header_x,header_y,header_z

def main():
    parser = argparse.ArgumentParser(description='Parse AstroPi collected data')
    parser.add_argument('-i','--input_file', dest='inputfile', action='store',default='data.csv', help='the input file to read the csv data')
    parser.add_argument('-o','--output_file', dest='outputfile', action='store',default='data_out.csv', help='the output file to write the parsed csv data')
    args = parser.parse_args()
    max_compass = None
    min_compass = None
    max_compass_x = None
    max_compass_y = None
    max_compass_z = None
    min_compass_x = None
    min_compass_y = None
    min_compass_z = None

    with open(args.inputfile, 'r') as f:
        read_csv= csv.DictReader(f)
        with open(args.outputfile, 'w') as f2:
            writer = csv.writer(f2)
            header = ("Date","Time","Latitude","Longitude","Pressure","Humidity","Temperature","Acceleration","Acceleration(x)","Acceleration(y)","Acceleration(z)","Gyroscope(x)","Gyroscope(y)","Gyroscope(z)","Magnetometer","Magnetometer(x)","Magnetometer(y)","Magnetometer(z)", "Orientation(roll)","Orientation(pitch)","Orientation(yaw)","CPU Temperature")
            writer.writerow(header)#write the CSV header
            for lines in read_csv:
                date_time = lines['Date/time'].split(' ')
                date = date_time[0]
                time = date_time[1]
                latitude_str = lines['Latitude'].split(":")
                latitude = dms_to_dd(float(latitude_str[0]),float(latitude_str[1]),float(latitude_str[2]))
                longitude_str = lines['Longitude'].split(":")
                longitude = dms_to_dd(float(longitude_str[0]),float(longitude_str[1]),float(longitude_str[2]))
                pressure = round(float(lines['Pressure']),3)
                humidity = round(float(lines['Humidity']),3)
                temperature = round(float(lines['Temperature']),3)
                accel_x,accel_y,accel_z = create_tuple(lines['Acceleration'],'x','y','z')
                gyro_x,gyro_y,gyro_z = create_tuple(lines['Gyroscope'],'x','y','z')
                compass_x, compass_y, compass_z = create_tuple(lines['Magnetometer'],'x','y','z')
                compass = math.sqrt(pow(compass_x,2)+pow(compass_y,2)+pow(compass_z,2))
                accel = math.sqrt(pow(accel_x,2)+pow(accel_y,2)+pow(accel_z,2))
                orient_x,orient_y,orient_z = create_tuple(lines['Orientation'],'roll','pitch','yaw')
                cpu_temperature = round(float(lines['CPU Temperature']),3)
                if not max_compass:
                    max_compass = compass
                    min_compass = compass
                else:
                    if max_compass < compass:
                        max_compass = compass
                    elif min_compass > compass:
                        min_compass = compass
                if not max_compass_x:
                    max_compass_x = compass_x
                    min_compass_x = compass_x
                else:
                    if max_compass_x < compass_x:
                        max_compass_x = compass_x
                    elif min_compass_x > compass_x:
                        min_compass_x = compass_x
                if not max_compass_y:
                    max_compass_y = compass_y
                    min_compass_y = compass_y
                else:
                    if max_compass_y < compass_y:
                        max_compass_y = compass_y
                    elif min_compass_y > compass_y:
                        min_compass_y = compass_y
                if not max_compass_z:
                    max_compass_z = compass_z
                    min_compass_z = compass_z
                else:
                    if max_compass_z < compass_z:
                        max_compass_z = compass_z
                    elif min_compass_z > compass_z:
                        min_compass_z = compass_z
                data = (date,time,latitude,longitude,pressure,humidity,temperature,accel,accel_x,accel_y,accel_z,gyro_x,gyro_y,gyro_z,compass,compass_x,compass_y,compass_z,orient_x,orient_y,orient_z,cpu_temperature)
                writer.writerow(data)
            print(round(min_compass,3),round(max_compass,3))
            print(min_compass_x,max_compass_x)
            print(min_compass_y,max_compass_y)
            print(min_compass_z,max_compass_z)

if __name__ == '__main__':
    main()
