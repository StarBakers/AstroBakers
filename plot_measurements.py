##############################################################
########################## The *Bakers #######################
######################### (AstroBakers) ######################
#########################      2021    ####################### 
##############################################################
##     This program is released under the MIT Licence       ##
##############################################################

import matplotlib.pyplot as plt
import matplotlib as mpl
import argparse
import csv
import matplotlib.dates as mdates
import datetime
from scipy.ndimage.filters import uniform_filter1d

def main():
    parser = argparse.ArgumentParser(description='Plot collected measurements')
    parser.add_argument('-i','--input_file', dest='inputfile', action='store',default='data_out.csv', help='the input file to read the csv data')
    args = parser.parse_args()

    #create the lists that will store the data to be plotted
    isstime = []
    humidity = []
    temperature = []
    cpu_temperature = []
    pressure = []
    acceleration = []
    yaw = []

    #read the csb file with the data and populate the lists with the corresponding data
    with open(args.inputfile, 'r') as f:
        read_csv= csv.DictReader(f)
        for lines in read_csv:
            date_time_obj = datetime.datetime.strptime(lines['Time'],'%H:%M:%S.%f')
            #print('Time:', date_time_obj.time())
            isstime.append(date_time_obj)
            humidity.append(float(lines['Humidity']))
            temperature.append(float(lines['Temperature']))
            cpu_temperature.append(float(lines['CPU Temperature']))
            pressure.append(float(lines['Pressure']))
            acceleration.append(float(lines['Acceleration']))
            yaw.append(float(lines['Orientation(yaw)']))

    #create the rolling averages for some of the data
    humidity_uniform = uniform_filter1d(humidity, size=100)
    cpu_temperature_uniform = uniform_filter1d(cpu_temperature, size=100)
    pressure_uniform = uniform_filter1d(pressure, size=100)

    # create figures and their axes
    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
    fig3, ax3 = plt.subplots()
    fig4, ax4 = plt.subplots()
    fig5, ax5 = plt.subplots()
    
    # setting title to each figure
    ax1.set_title('ISS Humidity versus time',fontsize=20)
    ax2.set_title('ISS Temperature versus time',fontsize=20)
    ax3.set_title('ISS Pressure versus time',fontsize=20)
    ax4.set_title('ISS Acceleration versus time',fontsize=20)
    ax5.set_title('ISS Orentation (yaw) versus time',fontsize=20)

    ##plot the various lines
    ##----------------------
    #fifure 1
    ax1.plot(isstime, humidity,linewidth=1, label='Humidity')
    ax1.plot(isstime, humidity_uniform,linewidth=1,label='Humidity rolling average')
    #figure 2
    ax2.plot(isstime, temperature,linewidth=1, label = 'temperature')
    ax2.plot(isstime, cpu_temperature,linewidth=1, label = 'CPU temperature')
    ax2.plot(isstime, cpu_temperature_uniform,linewidth=1, label = 'CPU temperature rolling average')
    #figure 3
    ax3.plot(isstime, pressure,linewidth=1, label='pressure')
    ax3.plot(isstime, pressure_uniform,linewidth=1, label = 'pressure rolling average')
    #figure 4
    ax4.plot(isstime, acceleration,linewidth=1)
    #figure 5 
    ax5.plot(isstime, yaw,linewidth=1)

    #add legends
    ax1.legend()
    ax2.legend()
    ax3.legend()

    # label plotted data
    ax1.set_ylabel('Humidity (%)')
    ax1.set_xlabel('Time')
    ax2.set_ylabel('Temperature (oC)')
    ax2.set_xlabel('Time')
    ax3.set_ylabel('Pressure')
    ax3.set_xlabel('Time')
    ax4.set_ylabel('Acceleration')
    ax4.set_xlabel('Time')
    ax5.set_xlabel('Time')
    ax5.set_ylabel('Orientation (yaw)')
    
    #Format x-axis format to depict only hours and minutes in the scale
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax4.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax5.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    #plt.gcf().autofmt_xdate()

    #draw grids 
    ax1.grid('True')
    ax2.grid('True')
    ax3.grid('True')

    #Now draw all the figures/diagrams
    plt.show()

if __name__ == '__main__':
    main()
