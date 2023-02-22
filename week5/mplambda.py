"""A multiprocessing benchmark that runs inside of AWS Lambda.

Calculate the sum of 10,000 numbers and print the result in 25 processes.
"""
import multiprocessing
import time

def sum_numbers():
    """Sum numbers."""
    numbers = []
    for i in range(10000):
        numbers.append(i)
    #print the sum and the id of the process
    print(f"Sum: {sum(numbers)} Process ID: {multiprocessing.current_process().pid}")

#write an aws lambda handler function
def lambda_handler(event, context):
    """Lambda handler function."""
    # Measure the time it takes to spawn the processes.
    start = time.time()
    # Create 100processes.
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
    # Print the results.
    print(f"Time to spawn processes: {end - start}")
    print(f"Time to complete processes: {end - start}")