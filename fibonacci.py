
import matplotlib.pyplot as plt
import time
import concurrent.futures as cf

def time_func(fun, n):
    startTime  = time.time()
    fun(n)
    endTime  = time.time()
    
    execTime = endTime - startTime
    return execTime

#O(2^n)
def trib(n):#presume n >= 1
    if n == 0:
        raise ValueError("n must be >= 1")
    elif n <= 2:#if n 1 or 2 then sequence is 1,1 -> n = 1
        return 1 #c2.5 = 1
    else: #(n-1)+n | 1,1 -> 1+1=2 -> 1,1,2...
        val = trib(n-1) + trib(n-2)    
    return val

def trib_steps(n):
    if n == 0:
        raise ValueError("n must be >= 1") 
    elif n <= 2:
        return 1
    else:
        steps = trib_steps(n-1) + trib_steps(n-2)
    return steps

#O(N)
def trib_for(n):
    if n == 0:
        raise ValueError("n must be >= 1")  
    fibSeqList = []
    
    for val in range (0, n):
        if(len(fibSeqList) > 1): 
            val = fibSeqList[val-1] + fibSeqList[val-2]
        else:
            val = 1
        fibSeqList.append(val)
    return fibSeqList

def trib_for_steps(n):
    return n

def timed_trib(n):
    return time_func(trib, n)

def timed_trib_for(n):
    return time_func(trib_for, n)


def execute_in_parallel(func, seq):
    with cf.ProcessPoolExecutor() as executor:
        results = list(executor.map(func, seq))
    return results


if __name__ == '__main__':
    stepsTrib = []
    stepsTribFor = []
    timedFor = []
    timedRec = []

    fibToGet = 37  # Adjust as needed
    fibSeqToGet = [n for n in range(1, fibToGet + 1)]
    startTime  = time.time()
        
    timedRec = execute_in_parallel(timed_trib, fibSeqToGet)
    timedFor = execute_in_parallel(timed_trib_for, fibSeqToGet)
    stepsTrib =  execute_in_parallel(trib_steps, fibSeqToGet)
    stepsTribFor =  execute_in_parallel(trib_for_steps, fibSeqToGet)
    
    endTime  = time.time()

    execTime = endTime - startTime

    print(execTime)
    plt.subplot()
    plt.scatter(fibSeqToGet, timedRec, color='red')
    plt.scatter(fibSeqToGet, timedFor, color='blue')
    plt.xlabel('Fibonacci value to calculate')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time vs. Fibonacci')

    plt.figure()
    plt.scatter(fibSeqToGet, stepsTrib, color='red')
    plt.scatter(fibSeqToGet, stepsTribFor, color='blue')
    plt.xlabel('Fibonacci value to calculate')
    plt.ylabel('Steps Taken')
    plt.title('Steps taken vs. Fibonacci')
    plt.show()

