##############################################################
########################## The *Bakers #######################
######################### (AstroBakers) ######################
#########################      2021    ####################### 
##############################################################
##     This program is released under the MIT Licence       ##
##############################################################

from mpl_toolkits.basemap import Basemap
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import argparse
import csv

def main():
    parser = argparse.ArgumentParser(description='Plot magnetic measurements vs ISS trajectory')
    parser.add_argument('-i','--input_file', dest='inputfile', action='store',default='data_out.csv', help='the input file to read the csv data')
    args = parser.parse_args()

    # miller projection 
    #map = Basemap(projection='mill',llcrnrlat=-90,urcrnrlat=90,llcrnrlon=-180,urcrnrlon=180,resolution='h')
    #map = Basemap(projection='mill',llcrnrlat=-90,urcrnrlat=90,llcrnrlon=-180,urcrnrlon=180,resolution='f')
    map = Basemap(projection='mill',llcrnrlat=-90,urcrnrlat=90,llcrnrlon=-180,urcrnrlon=180,resolution='l')
    map.shadedrelief()
    
    # plot coastlines, draw label meridians and parallels.
    map.drawcoastlines()
    map.drawparallels(np.arange(-90,91,30),labels=[1,0,0,0])
    map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,60),labels=[0,0,0,1])
    
    cmap = plt.cm.hot_r
    norm = colors.Normalize(vmin=29.64, vmax=69.401)
    plt.title('ISS trajectory',fontsize=20)

    with open(args.inputfile, 'r') as f:
        read_csv= csv.DictReader(f)
        for lines in read_csv:
            lat = float(lines['Latitude'])
            lon = float(lines['Longitude'])
            magnetometer = float(lines['Magnetometer'])

            # convert to map projection coords.
            # Note that lon,lat can be scalars, lists or numpy arrays.
            xpt,ypt = map(lon,lat)

            map.plot(xpt,ypt,norm(magnetometer),color=plt.cm.hot_r(norm(magnetometer)),marker='.',markersize=3)  # plot a dot there
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    cbar=plt.colorbar(sm)
    cbar.set_label('measured magnetic field (microTesla)',fontsize=16)
    plt.show()

if __name__ == '__main__':
    main()
