class Process:
    def __init__(self, pid, arrival, burst):
        self.pid, self.arrival, self.burst = pid, arrival, burst
        self.completion = self.turnaround = self.waiting = 0

processes = [Process(1, 0, 8), Process(2, 1, 4), Process(3, 2, 9), Process(4, 3, 5)]
processes.sort(key=lambda p: p.arrival)

time = 0
for p in processes:
    time = max(time, p.arrival) + p.burst
    p.completion, p.turnaround, p.waiting = time, time - p.arrival, time - p.arrival - p.burst
print(f"The FCFS job is:")
print("PID  Arrival  Burst  Completion  Turnaround  Waiting")
for p in processes:
    print(f"{p.pid:<5}{p.arrival:<8}{p.burst:<7}{p.completion:<11}{p.turnaround:<11}{p.waiting}")

avg_turn = sum(p.turnaround for p in processes) / len(processes)
avg_waiting = sum(p.waiting for p in processes) / len(processes)
print(f"\nAverage Turnaround Time: {avg_turn:.2f}")
print(f"Average Waiting Time: {avg_waiting:.2f}")