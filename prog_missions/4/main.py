# -*- coding: utf-8 -*-
"""
Created on Wed Oct 07 22:10:39 2015

@author: Marcus Therkildsen
"""
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

def deg2rad(deg_in):
    return deg_in*np.pi/180

def xy(r,phi):
    return r*np.cos(phi), r*np.sin(phi)

if __name__ == '__main__':

    # Load the xml file
    xml = np.genfromtxt('plotMe.xml', delimiter=',', dtype='str',autostrip = True)

    # Number of line elements
    num_lines = list(xml).count('<Line>')

    # Number of arc elements
    num_arcs = list(xml).count('<Arc>')

    # Prepare arrays
    lines = np.zeros([num_lines,4]) # (x_start,x_end,y_start,y_end)
    c_lines = np.empty(num_lines,dtype='str')
    arcs = np.zeros([num_arcs,5]) # (x_center,y_center, arc_start (in degrees), arc_extend (in degrees), radius)
    c_arcs = np.empty(num_arcs,dtype='str')

    # Go through xml document
    tj_lines = -1
    tj_arcs = -1
    for i in xrange(len(xml)):

        if '<Line>' in xml[i]:
            tj_lines+=1

            # In case no color is defined, predefine it to be white
            color_ = 'w'

            for k in xrange(5):
                if 'YEnd' in xml[i+k+1]:
                    y_end = float(xml[i+k+1][6:-7])

                elif 'YStart' in xml[i+k+1]:
                    y_start = float(xml[i+k+1][8:-9])

                elif 'XEnd' in xml[i+k+1]:
                    x_end = float(xml[i+k+1][6:-7])

                elif 'XStart' in xml[i+k+1]:
                    x_start = float(xml[i+k+1][8:-9])

                elif 'Color' in xml[i+k+1]:
                    color_ = xml[i+k+1][7:-8]

            lines[tj_lines,:] = [x_start, x_end, y_start, y_end]
            c_lines[tj_lines] = color_

        if '<Arc>' in xml[i]:
            tj_arcs+=1

            # In case no color is defined, predefine it to be white
            color_ = 'w'

            for k in xrange(6):

                if 'XCenter' in xml[i+k+1]:
                    x_center = float(xml[i+k+1][9:-10])

                elif 'YCenter' in xml[i+k+1]:
                    y_center = float(xml[i+k+1][9:-10])

                elif 'ArcStart' in xml[i+k+1]:
                    arc_start = float(xml[i+k+1][10:-11])

                elif 'ArcExtend' in xml[i+k+1]:
                    arc_extend = float(xml[i+k+1][11:-12])

                elif 'Radius' in xml[i+k+1]:
                    radius = float(xml[i+k+1][8:-9])

                elif 'Color' in xml[i+k+1]:
                    color_ = xml[i+k+1][7:-8]

            arcs[tj_arcs,:] = [x_center,y_center,arc_start,arc_extend,radius]
            c_arcs[tj_arcs] = color_

    """
    Plot
    """

    fig, ax =plt.subplots()

    # Color background black
    ax.set_axis_bgcolor('k')

    [ax.plot(lines[i,:2],lines[i,2:],color = c_lines[i]) for i in xrange(num_lines)]

    # Plot the arcs. Remember that the arc should begin at arc_start and end at arc_start + arc_extend
    for i in xrange(num_arcs):
        stuff = np.array(xy(arcs[i,4],np.arange(deg2rad(arcs[i,2]),deg2rad(arcs[i,2])+deg2rad(arcs[i,3]),0.1))).T
        x_ = stuff[:,0]+arcs[i,0]
        y_ = stuff[:,1]+arcs[i,1]
        ax.plot(x_,y_,color = c_arcs[i])

    # Remove labels
    plt.setp( ax.get_xticklabels(), visible=False)
    plt.setp( ax.get_yticklabels(), visible=False)
    plt.savefig('done.png',dpi=400,bbox_inches='tight')
    plt.show()