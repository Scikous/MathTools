
import matplotlib.pyplot as plt
import time
import concurrent.futures as cf

def time_func(fun, fib_val):
    start_time  = time.time()
    val = fun(fib_val)
    end_time  = time.time()
    exec_time = end_time - start_time
    return exec_time, val

#O(2^N)
def trib_slowest(fib_val):#presume fib_val >= 1
    if fib_val < 0:
        raise ValueError("fib_val must be >= 0")
    elif fib_val == 0:
        return 0
    elif fib_val == 1:
        return 1
    else: #(fib_val-1)+(fib_val-2) -> 1,1 -> 1+1=2 -> 1,1,2...
        return trib_slowest(fib_val-1) + trib_slowest(fib_val-2)  
      
#O(2^N)
def trib_steps_slowest(fib_val, steps=0):
    if fib_val == 0 or fib_val == 1:
        return steps+1
    else:
        steps_left = trib_steps_slowest(fib_val - 1, steps)
        steps_right = trib_steps_slowest(fib_val - 2, steps)
        return steps_left + steps_right + 1
    
#O(2^(N-1))
def trib_slow(fib_val):#presume fib_val >= 1
    if fib_val <= 0:
        raise ValueError("fib_val must be >= 1")
    elif fib_val == 1 or fib_val == 2:#if fib_val 1 or 2 then sequence is 1,1 -> fib_val = 1
        return 1
    else: #(fib_val-1)+fib_val | 1,1 -> 1+1=2 -> 1,1,2...
        return trib_slow(fib_val-1) + trib_slow(fib_val-2) 

#O(2^(N-1))
def trib_steps_slow(fib_val, steps=0):
    if fib_val == 1 or fib_val == 2:
        return steps+1
    else:
        steps_left = trib_steps_slow(fib_val - 1, steps)
        steps_right = trib_steps_slow(fib_val - 2, steps)
        return steps_left + steps_right + 1

#O(N)
def trib(fib_val, traversed=None):#presume fib_val >= 1
    if traversed is None:
        traversed = {}
    if fib_val <= 0:
        raise ValueError("fib_val must be >= 1")
    elif fib_val <= 2:#if fib_val 1 or 2 then sequence is 1,1 -> fib_val = 1
        return 1
    elif fib_val not in traversed: #(fib_val-1)+fib_val | 1,1 -> 1+1=2 -> 1,1,2...
        traversed[fib_val] = trib(fib_val-1, traversed) + trib(fib_val-2,traversed)
    return traversed[fib_val]

#O(N)
def trib_steps_fast(fib_val, traversed=None, steps=0):
    if traversed is None:
        traversed = []
    if fib_val <= 0:
        raise ValueError("fib_val must be >= 1")
    elif fib_val <= 2:
        return steps+1
    elif fib_val not in traversed:
        traversed.append(fib_val)
        steps = trib_steps_fast(fib_val-1, traversed, steps)
        steps = trib_steps_fast(fib_val-2, traversed, steps)
    return steps+1

#O(N)
def trib_for(fib_val):
    if fib_val <= 0:
        raise ValueError("fib_val must be >= 1")  
    fib_seq_list = []
    for val in range(0, fib_val):
        if(val > 1): 
            val = fib_seq_list[val-1] + fib_seq_list[val-2]
        else:
            val = 1
        fib_seq_list.append(val)
    return fib_seq_list[-1]

def trib_for_steps(fib_val):
    return fib_val



def timed_trib_recursive_slowest(fib_val):
    return time_func(trib_slowest, fib_val)

def timed_trib_recursive_slow(fib_val):
    return time_func(trib_slow, fib_val)

def timed_trib_recursive_fast(fib_val):
    return time_func(trib, fib_val)

def timed_trib_for(fib_val):
    return time_func(trib_for, fib_val)


def execute_fib_in_parallel(func, seq: list):
    with cf.ProcessPoolExecutor() as executor:
        results = list(executor.map(func, seq))
    return results

if __name__ == '__main__':
    fib_get_values = 37  # Adjust as needed
    fib_seq_to_get = [fib_val for fib_val in range(1, fib_get_values + 1)]
    #get Fibonacci sequence values and their execution times
    timed_recursive_slowest, fib_vals_recursive_slowest = zip(*execute_fib_in_parallel(timed_trib_recursive_slowest, fib_seq_to_get))
    timed_recursive_slow, fib_vals_recursive_slow = zip(*execute_fib_in_parallel(timed_trib_recursive_slow, fib_seq_to_get))
    timed_recursive_fast, fib_vals_recursive_fast = zip(*execute_fib_in_parallel(timed_trib_recursive_fast, fib_seq_to_get))
    timed_for, fib_vals_for = zip(*execute_fib_in_parallel(timed_trib_for, fib_seq_to_get))

    #get Fibonacci sequence execution steps
    steps_trib_recursive_slowest =  execute_fib_in_parallel(trib_steps_slowest, fib_seq_to_get)
    steps_trib_recursive_slow =  execute_fib_in_parallel(trib_steps_slow, fib_seq_to_get)
    steps_trib_recursive_fast =  execute_fib_in_parallel(trib_steps_fast, fib_seq_to_get)
    steps_trib_for =  execute_fib_in_parallel(trib_for_steps, fib_seq_to_get)
    
    print(f"Recursive O(2^N) fib vals: {fib_vals_recursive_slowest}\fib_val\nRecursive O(2^(N-1)) fib vals: {fib_vals_recursive_slow}\fib_val\nRecursive O(N) fib vals: {fib_vals_recursive_fast}\fib_val\nFor loop O(N) fib vals: {fib_vals_for}\fib_val")
    print("--------------------------------")
    print(f"Recursive O(2^N) fib times: {timed_recursive_slowest}\fib_val\nRecursive O(2^(N-1)) fib times: {timed_recursive_slow}\fib_val\nRecursive O(N) fib times: {timed_recursive_fast}\fib_val\nFor loop O(N) fib times: {timed_for}\fib_val")
    print("--------------------------------")
    print(f"Recursive O(2^N) fib steps: {steps_trib_recursive_slowest}\fib_val\nRecursive O(2^(N-1)) fib steps: {steps_trib_recursive_slow}\fib_val\nRecursive O(N) fib steps: {steps_trib_recursive_fast}\fib_val\nFor loop O(N) fib steps: {steps_trib_for}")


    plt.subplot()
    plt.scatter(fib_seq_to_get, timed_recursive_slowest, color='orange', label='Recursive 2^N')
    plt.scatter(fib_seq_to_get, timed_recursive_slow, color='red', label='Recursive 2^(N-1)')
    plt.scatter(fib_seq_to_get, timed_recursive_fast, color='green', label='Recursive N')
    plt.scatter(fib_seq_to_get, timed_for, color='blue', label='Using For Loop')
    plt.xlabel('Fibonacci value to calculate')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time (Fibonacci)')
    plt.legend()

    #recursive_fast and For loop values are too similar, and cannot be distinguished from one another unless zoomed in
    plt.figure()
    plt.scatter(fib_seq_to_get, steps_trib_recursive_slowest, color='orange', label='Recursive 2^N')
    plt.scatter(fib_seq_to_get, steps_trib_recursive_slow, color='red', label='Recursive 2^(N-1)')
    plt.scatter(fib_seq_to_get, steps_trib_recursive_fast, color='green', label='Recursive N')
    plt.scatter(fib_seq_to_get, steps_trib_for, color='blue', label='Using For Loop')
    plt.xlabel('Fibonacci value to calculate')
    plt.ylabel('Steps Taken')
    plt.title('Steps taken (Fibonacci)')
    plt.legend()

    plt.figure()
    plt.scatter(fib_seq_to_get, steps_trib_recursive_fast, color='green', label='Recursive N')
    plt.scatter(fib_seq_to_get, steps_trib_for, color='blue', label='Using For Loop')
    plt.xlabel('Fibonacci value to calculate')
    plt.ylabel('Steps Taken')
    plt.title('Steps taken (Fibonacci)')
    plt.legend()
    
    plt.show()
