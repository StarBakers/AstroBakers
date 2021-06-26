# AstroBakers (*Bakers)
This is the github repository of the AstroBakers team (nickname: *Bakers, also known as StarBakes) from the participation in AstroPi 2021 Mission Space Lab competition (https://astro-pi.org/mission-space-lab/)

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
- ephem &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#to track ISS trajectory
- gpiozero &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#to measure CPU Temperature during program execution 
- datetime &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#to record date/time and calculate running time
- time &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#for "pausing" between measurements
- sense_hat &nbsp;&nbsp;&nbsp;&nbsp;#to interact with SenseHat
- pathlib &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#to obtain current path
- csv &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#to store results in csv file 
- logzero &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#to log errors (if any)

The program starts automatically at ISS. No arguments required. 

B. Code used to parse/process the collected AstroPi data
--------------------------------------------------------
Program name: process_astropi_data.py
This is a Python 3 program.

Libraries needed:
- csv&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#to read stored csv data
- math&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#for math functions
- argparse&nbsp;&nbsp;&nbsp;&nbsp;#for providing arguments to the program
- json&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#json library - useful to convert automatically json formatted strings to dictionary

usage: python process_astropi_data.py [-h] [-i INPUTFILE] [-o OUTPUTFILE]
<br /> 
optional arguments:<br /> 
  -i INPUTFILE, --input_file INPUTFILE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the input file to read the csv data<br /> 
  -o OUTPUTFILE, --output_file OUTPUTFILE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the output file to write the parsed csv data

Note: The input file must be the one that contains that data collected from the ISS using our program above. 

C.1 Code used to plot ISS trajectory vs measured magnetic field
---------------------------------------------------------------
Program name: map_trajectory.py
This is a Python 3 program. 

Libraries needed:
- matplotlib
- numpy
- csv
- argparse
- mpl_toolkits.basemap

usage: python map_trajectory.py [-h] [-i INPUTFILE] 

Note: The input file must be the output file of the process_astropi_data.py program.

C.2 Code used to plot enviromental, acceleration and orientation measurements  
-----------------------------------------------------------------------------
Program name: plot_measurements.py
This is a Python 3 program. 

Libraries needed:
- matplotlib
- argparse
- csv
- datetime
- scipy

usage: python plot_measurements.py [-h] [-i INPUTFILE]

Note: The input file must be the output file of the process_astropi_data.py program.

C.3 Code used to create contour maps of magnetic measurements  
-------------------------------------------------------------
Program name: MagnoDataReal.Rmd
This is an R program. 

- The program is under a .RMD format
- The output maps are HTML Documents
- Please make sure all files included are found within the same folder
- The program was made on [RStudio](https://www.rstudio.com/products/rstudio/download)
- You may need to download the language [R](https://www.r-project.org/) once RStudio is launched (it will request it)
- To run the program, select "RUN" -> "RUN ALL CHUNKS"
