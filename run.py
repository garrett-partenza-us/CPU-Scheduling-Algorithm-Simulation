#import needed packages
import copy
import random
import art
import random
from fifo import *
from rr import *
from sjn import *
from srtn import *
from pbs import *
from plot import *

def main():
    
    #show logo
    logo=art.text2art("CPU Scheduler Simulation")
    print(logo)
    print("\n"*2)
    
    #take user number of processes
    nmb = int(input("Enter the number of processes to schedule: "))
    
    #generate processes
    processes = [
    [None,0,4,None],
    [None,1,3,None],
    [None,5,7,None],
    [None,4,2,None],
    [None,3,3,None],
    [None,9,2,None],
    [None,5,3,None],
    [None,3,1,None],
    [None,2,7,None],
    [None,8,5,None],
    [None,0,1,None],
    ]
    processes = random.sample(processes, nmb)
    for i in range(len(processes)):
        if i == 0:
            processes[i][1]=0
        processes[i][0] = i+1
        processes[i][3] = random.randrange(1,10)

    #make deep copys of data for each function
    data1 = copy.deepcopy(processes)
    data2 = copy.deepcopy(data1)
    data3 = copy.deepcopy(data2)
    data4 = copy.deepcopy(data3)
    data5 = copy.deepcopy(data4)
    data6 = copy.deepcopy(data5)
    
    #get calenders
    display(FIFO(data1), RR(data2), SJN(data3), SRTN(data4), PBS(data5), data6, nmb)

if __name__ == '__main__':
    main()
