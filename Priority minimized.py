class Process:
    def __init__(self, pid, arrival, burst, priority):
        self.pid, self.arrival, self.burst, self.priority = pid, arrival, burst, priority
        self.completion = self.turnaround = self.waiting = 0

processes = [Process(1, 0, 8, 3), Process(2, 1, 4, 1), Process(3, 2, 9, 4), Process(4, 3, 5, 2)]
processes.sort(key=lambda p: (p.arrival, p.priority))
current_time = 0

for p in processes:
    current_time = max(current_time, p.arrival) + p.burst
    p.completion = current_time
    p.turnaround = p.completion - p.arrival
    p.waiting = p.turnaround - p.burst

print(f"Priority Scheduling(Non-Preemptive)")
print("PID  Arrival  Burst  Priority  Completion  Turnaround  Waiting")
for p in processes:
     print(f"{p.pid:<5}{p.arrival:<8}{p.burst:<7}{p.priority:<9}{p.completion:<11}{p.turnaround:<11}{p.waiting}")

avg_turnaround = sum(p.turnaround for p in processes) / len(processes)
avg_waiting = sum(p.waiting for p in processes) / len(processes)
print(f"\nAverage Turnaround Time: {avg_turnaround:.2f}")
print(f"Average Waiting Time: {avg_waiting:.2f}")
