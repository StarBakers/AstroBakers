# AstroBakers (*Bakers)
#This is the github repository of the AstroBakers team (nickname: *Bakers, also known as StarBakes) from the participation in AstroPi 2021 Mission Space Lab competition (https://astro-pi.org/mission-space-lab/)

In this repository we publish all the code we created and used during our participation in this competion. 
The code is released under the MIT Licence. 

The code includes the following parts:  
A. Code used for performing measurements at International Space Station (ISS); this code was used to achieve the flight status. Therefore, it was minimised to the bare minimum.  
B. Code used for parsing the data we received after our code run at ISS; parsing includes e.g. splitting vector data in x,y,z, converting Lat Long coordinates, etc.   
C. Code used to analyse the data and produce the various graphs for our study. Part of the graphs is included in the report.  

A. Code used to perform measurements at ISS
-------------------------------------------
Program name: main.py
This is a Python 3 program. 

Libraries needed: 
- ephem     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#to track ISS trajectory
- gpiozero  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#to measure CPU Temperature during program execution 
- datetime  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#to record date/time and calculate running time
- time      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#for "pausing" between measurements
- sense_hat &nbsp;&nbsp;&nbsp;&nbsp;#to interact with SenseHat
- pathlib   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#to obtain current path
- csv       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#to store results in csv file 
- logzero   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#to log errors (if any)

The program starts automatically at ISS. No arguments required. 

B. Code used to parse/process the collected AstroPi data
--------------------------------------------------------
Program name: process_astropi_data.py
This is a Python 3 program.

Libraries needed:
- csv       &emsp;&emsp;&emsp;#to read stored csv data
- math      &emsp;&emsp;&emsp;#for math functions
- argparse  &emsp;&emsp;#for providing arguments to the program
- json      &emsp;&emsp;&emsp;#json library - useful to convert automatically json formatted strings to dictionary

usage: process_astropi_data.py [-h] [-i INPUTFILE] [-o OUTPUTFILE]
<br /> 
Parse AstroPi collected data<br /> 
<br /> 
optional arguments:<br /> 
  -i INPUTFILE, --input_file INPUTFILE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the input file to read the csv data<br /> 
  -o OUTPUTFILE, --output_file OUTPUTFILE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the output file to write the parsed csv data

