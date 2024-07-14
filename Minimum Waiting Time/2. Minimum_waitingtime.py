# T-O(nlogn) | S-O(1)
def minimum_waiting_time(processes):
    processes.sort()
    total_waiting_time = 0
    for idx, time in enumerate(processes):
        total_waiting_time += time * (len(processes) - (idx + 1))

    return total_waiting_time


# print(f"minimum waiting time is {minimum_waiting_time(processes)}")
