#!/usr/bin/env python3
"""Process benchmarking script.
The goal of this script is to benchmark the performance of the Python process and the memory overhead of the process.
This script does the following:

1. Spawns 100 processes using the multiprocessing module.
2. Each process will run the following code: calculate the fibonacci number of 1000.
3. The script will measure the time it takes to spawn all the processes and the time it takes to complete all the processes.
4. The script will measure the memory usage of the process before and after the processes are spawned and completed.
5. The script will print the results to the console.

"""
import time
import multiprocessing
import psutil
import resource

# A function that creates 10,000 numbers in a list and then sums them up
def sum_numbers():
    """Sum numbers."""
    numbers = []
    for i in range(10000):
        numbers.append(i)
    #print the sum and the id of the process
    print(f"Sum: {sum(numbers)} Process ID: {multiprocessing.current_process().pid}")
    #print the memory usage of the process in human readable format
    process = psutil.Process()
    print(f"Memory usage: {psutil._common.bytes2human(process.memory_info().rss)}")

def main():
    """Main function."""
    # Measure the memory usage of the process before spawning the processes.
    process = psutil.Process()
    mem_before = process.memory_info().rss / 1024 / 1024

    peak_mem_before = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 / 1024
    #print the peak memory usage of the process in human readable format
    print(f"Peak memory usage: {psutil._common.bytes2human(peak_mem_before)}")

    # Measure the time it takes to spawn the processes.
    start = time.time()
    # Create 100 processes.
    processes = []
    for i in range(100):
        processes.append(multiprocessing.Process(target=sum_numbers))
    # Start the processes.
    

    for p in processes:
        p.start()
    # Wait for the processes to complete.
    for p in processes:
        p.join()
    end = time.time()

    # Measure the memory usage of the process after the processes are completed.
    mem_after = process.memory_info().rss / 1024 / 1024
    peak_mem_after = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 / 1024
    #print the peak memory usage of the process in human readable format
    print(f"Peak memory usage: {psutil._common.bytes2human(peak_mem_after)}")

    # Print the results.
    print(f"Time to spawn processes: {end - start}")
    print(f"Time to complete processes: {end - start}")
    print(f"Memory usage before spawning processes: {mem_before} MB")
    print(f"Memory usage after spawning processes: {mem_after} MB")

if __name__ == "__main__":
    main()

