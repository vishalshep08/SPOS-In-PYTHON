class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = self.turnaround_time = self.waiting_time = 0

def round_robin(processes, quantum):
    time, completed = 0, 0
    queue = []
    while completed < len(processes):
        for p in processes:
            if p.arrival_time <= time and p not in queue: queue.append(p)
        if queue:
            p = queue.pop(0)
            exec_time = min(p.remaining_time, quantum)
            time += exec_time
            p.remaining_time -= exec_time
            if p.remaining_time == 0:
                p.completion_time = time
                p.turnaround_time = p.completion_time - p.arrival_time
                p.waiting_time = p.turnaround_time - p.burst_time
                completed += 1
            else:
                queue.append(p)
        else:
            time += 1
    return processes

def display_results(processes, algorithm_name):
    print(f"\n{algorithm_name}:")
    print(f"{'PID':<10}{'Arrival':<10}{'Burst':<10}{'Completion':<15}{'Turnaround':<15}{'Waiting':<10}")
    for p in processes:
        print(f"{p.pid:<10}{p.arrival_time:<10}{p.burst_time:<10}{p.completion_time:<15}{p.turnaround_time:<15}{p.waiting_time:<10}")
    avg_turnaround = sum(p.turnaround_time for p in processes) / len(processes)
    avg_waiting = sum(p.waiting_time for p in processes) / len(processes)
    print(f"\nAverage Turnaround Time: {avg_turnaround:.2f}")
    print(f"Average Waiting Time: {avg_waiting:.2f}")

if __name__ == "__main__":
    processes = [Process(1, 0, 8), Process(2, 1, 4), Process(3, 2, 9), Process(4, 3, 5)]
    round_robin(processes, 2)
    display_results(processes, "Round Robin (Time Quantum = 2)")
