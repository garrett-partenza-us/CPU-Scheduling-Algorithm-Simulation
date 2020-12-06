#SRTN simulator
def RR(data):
    #set needed variables, where data is the original data source and copy is a deep copy of data
    data, time, results = data, 0, []
    #loop until all processes are complete
    while True:
        #create ready queue
        ready = list(x[0] for x in data if x[1]<=time)
        #if there are no processes to run and ready queue is empty
        if not ready:
            results.append([None,None])
            time+=1
        #otherwise, iterate through all ready processes and run the FIFO algorithm
        else:
            rq = []
            for i, process in enumerate(data):
                if data[i][0] in ready:
                    rq.append(data[i])
            for process in rq:
                for x, d in enumerate(data):
                    if data[x][0] == process[0]:
                        data[x][2]-=1
                        results.append([data[x][0], data[x][2]])
                        time+=1
                    
        #get rid of completed processes
        data = list(x for x in data if x[2]>0)
        #break while of all processes are complete
        if not data:
            break
        # print(results)
            
    return results
