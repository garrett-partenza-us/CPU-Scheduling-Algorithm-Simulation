import copy
import collections
import sys
import random
import time
import numpy as np
import matplotlib.pyplot as plt

def display(results_fifo, results_rr, results_sjn, results_srtn, results_pbs, data, nmb):

    #join all calenders into list
    results = [results_fifo, results_rr, results_sjn, results_srtn, results_pbs]

    #create figure
    plt.figure(figsize=(12,8))
    #data table
    ax0 = plt.subplot2grid((7, 5), (6, 0), colspan=5)
    #broken bar plots
    ax1 = plt.subplot2grid((7, 5), (0, 0), colspan=4)
    ax2 = plt.subplot2grid((7, 5), (1, 0), colspan=4)
    ax3 = plt.subplot2grid((7, 5), (2, 0), colspan=4)
    ax4 = plt.subplot2grid((7, 5), (3, 0), colspan=4)
    ax5 = plt.subplot2grid((7, 5), (4, 0), colspan=4)
    #vertical bar plots
    ax6 = plt.subplot2grid((7, 5), (1, 4), rowspan=1)
    ax7 = plt.subplot2grid((7, 5), (2, 4), rowspan=1)
    ax8 = plt.subplot2grid((7, 5), (3, 4), rowspan=1)
    ax9 = plt.subplot2grid((7, 5), (0, 4), rowspan=1)
    ax10 = plt.subplot2grid((7, 5), (4, 4), rowspan=1)

    #list of pyplot accepted colors
    colors = ['c','m','g','y','b','r']

    #x lables for subplots
    xl = []
    for i in range(nmb):
        xl.append("P"+str(i+1))

    #set calender subplot axis
    ax1.set_xlabel('Time', color='black')
    ax1.tick_params(axis='x', colors='black')
    ax1.set_yticks([1.5, 2.5, 3.5, 4.5, 5.5, 6.5])
    ax1.set_yticklabels(xl)
    ax1.tick_params(axis='y', colors='black')
    ax2.set_xlabel('Time', color='black')
    ax2.tick_params(axis='x', colors='black')
    ax2.set_yticks([1.5, 2.5, 3.5, 4.5, 5.5, 6.5])
    ax2.set_yticklabels(xl)
    ax2.tick_params(axis='y', colors='black')
    ax3.set_xlabel('Time', color='black')
    ax3.tick_params(axis='x', colors='black')
    ax3.set_yticks([1.5, 2.5, 3.5, 4.5, 5.5, 6.5])
    ax3.set_yticklabels(xl)
    ax3.tick_params(axis='y', colors='black')
    ax4.set_xlabel('Time', color='black')
    ax4.tick_params(axis='x', colors='black')
    ax4.set_yticks([1.5, 2.5, 3.5, 4.5, 5.5, 6.5])
    ax4.set_yticklabels(xl)
    ax4.tick_params(axis='y', colors='black')
    ax5.set_xlabel('Time', color='black')
    ax5.tick_params(axis='x', colors='black')
    ax5.set_yticks([1.5, 2.5, 3.5, 4.5, 5.5, 6.5])
    ax5.set_yticklabels(xl)
    ax5.tick_params(axis='y', colors='black')

    #prepare variables for bar plots
    fifo_completed, rr_completed, sjn_completed, srtn_completed, pbs_completed = [0]*nmb, [0]*nmb, [0]*nmb, [0]*nmb, [0]*nmb
    fifo_to_go, rr_to_go, sjn_to_go, srtn_to_go, pbs_to_go = [(list(x[2] for x in data)*5)[x:x+nmb] for x in range(0, len((list(x[2] for x in data)*5)),nmb)]

    #for purpose of ploting emptys in calender
    last1, last2, last3, last4, last5 = None, None, None, None, None

    # *** LOOP THAT PLOTS CALENDERS ***
    for i in range(len(results[0])):

        #set calender subplots labels
        ax1.set_ylabel('FIFO', weight = 'bold')
        ax2.set_ylabel('RR', weight = 'bold')
        ax3.set_ylabel('SJN', weight = 'bold')
        ax4.set_ylabel('SRTN', weight = 'bold')
        ax5.set_ylabel('PBS', weight = 'bold')
        
        #converts current time to appropriate broken bar plot
        if results[0][i][0] == None:
            ax1.broken_barh([(i,1)], (last1, 1), facecolors=('white'))
        else:
            ax1.broken_barh([(i,1)], (results[0][i][0], 1), facecolors=(colors[results[0][i][0]-1]), edgecolor="black")
            fifo_completed[results[0][i][0]-1]+=1
            fifo_to_go[results[0][i][0]-1]-=1
            last1 = results[0][i][0]
        if results[1][i][0] == None:
            ax2.broken_barh([(i,1)], (last2, 1), facecolors=('white'))
        else:
            ax2.broken_barh([(i,1)], (results[1][i][0], 1), facecolors=(colors[results[1][i][0]-1]), edgecolor="black")
            rr_completed[results[1][i][0]-1]+=1
            rr_to_go[results[1][i][0]-1]-=1
            last2 = results[1][i][0]
        if results[2][i][0] == None:
            ax3.broken_barh([(i,1)], (last3, 1), facecolors=('white'))
        else:
            ax3.broken_barh([(i,1)], (results[2][i][0], 1), facecolors=(colors[results[2][i][0]-1]), edgecolor="black")
            sjn_completed[results[2][i][0]-1]+=1
            sjn_to_go[results[2][i][0]-1]-=1
            last3 = results[2][i][0]
        if results[3][i][0] == None:
            ax4.broken_barh([(i,1)], (last4, 1), facecolors=('white'))
        else:
            ax4.broken_barh([(i,1)], (results[3][i][0], 1), facecolors=(colors[results[3][i][0]-1]), edgecolor="black")
            srtn_completed[results[3][i][0]-1]+=1
            srtn_to_go[results[3][i][0]-1]-=1
            last4 = results[3][i][0]
        if results[4][i][0] == None:
            ax5.broken_barh([(i,1)], (last4, 1), facecolors=('white'))
        else:
            ax5.broken_barh([(i,1)], (results[4][i][0], 1), facecolors=(colors[results[4][i][0]-1]), edgecolor="black")
            pbs_completed[results[4][i][0]-1]+=1
            pbs_to_go[results[4][i][0]-1]-=1
            last5 = results[4][i][0]
        
        #plot data table
        label=("Process ID", "Arrival Time", "Burst Time", "Priority")
        cellColors = [['c','c','c','c'],['m','m','m','m'],['g','g','g','g'],['y','y','y','y'],['b','b','b','b'],['r','r','r','r']][0:nmb]
        #clear previous data table to prevent full screen from distorting visual
        ax0.clear()
        ax0.table(cellText=np.array(data), cellColours=cellColors, colLabels=label, cellLoc='center', loc='center')
        ax0.set_yticklabels([])
        ax0.set_xticklabels([])
        ax0.axis('off')
        
        #turn off the y axis for the verticle bar plots
        ax6.axes.get_yaxis().set_visible(False)
        ax7.axes.get_yaxis().set_visible(False)
        ax8.axes.get_yaxis().set_visible(False)
        ax9.axes.get_yaxis().set_visible(False)
        ax10.axes.get_yaxis().set_visible(False)

        #width of bars in verticle bar plots
        width = 0.35
        
        #update verticle bar subplots
        ax6.clear()
        ax7.clear()
        ax8.clear()
        ax9.clear()
        ax6.bar(xl, rr_completed, width, color='g')
        ax6.bar(xl, rr_to_go, width, bottom=rr_completed, color='r')
        ax7.bar(xl, sjn_completed, width, color='g')
        ax7.bar(xl, sjn_to_go, width, bottom=sjn_completed, color='r')
        ax8.bar(xl, srtn_completed, width, color='g')
        ax8.bar(xl, srtn_to_go, width, bottom=srtn_completed, color='r')
        ax9.bar(xl, fifo_completed, width, color='g')
        ax9.bar(xl, fifo_to_go, width, bottom=fifo_completed, color='r')
        ax10.bar(xl, pbs_completed, width, color='g')
        ax10.bar(xl, pbs_to_go, width, bottom=pbs_completed, color='r')
        
        #prevents overlapping of sub plots
        plt.tight_layout()
        
        #pause for user to see
        plt.pause(1.0)

    #display plot indefinitly at end
    plt.show()


