# T-O(nlogn) | S-O(1)
def minimum_waiting_time(processes):
    processes.sort()
    min_waiting_time = 0
    cur_sum = processes[0]
    for i in range(1, len(processes) - 1):
        processes[i] += cur_sum
        cur_sum = processes[i]
    for val in processes:
        min_waiting_time += val

    return min_waiting_time - processes[len(processes) - 1]


# print(f"minimum waiting time is {minimum_waiting_time(processes)}")
