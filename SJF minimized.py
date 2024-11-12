class Process:
    def __init__(self, pid, arrival, burst):
        self.pid, self.arrival, self.burst = pid, arrival, burst
        self.completion = self.turnaround = self.waiting = self.remaining = burst

processes = [Process(1, 0, 8), Process(2, 1, 4), Process(3, 2, 9), Process(4, 3, 5)]
time = 0

while any(p.remaining > 0 for p in processes):
    available = [p for p in processes if p.arrival <= time and p.remaining > 0]
    if available:
        shortest = min(available, key=lambda p: p.remaining)
        shortest.remaining -= 1
        if shortest.remaining == 0:
            shortest.completion, shortest.turnaround = time + 1, time + 1 - shortest.arrival
            shortest.waiting = shortest.turnaround - shortest.burst
    time += 1
print(f"The SJF job is:")
print("PID  Arrival  Burst  Completion  Turnaround  Waiting")
for p in processes:
    print(f"{p.pid:<5}{p.arrival:<8}{p.burst:<7}{p.completion:<11}{p.turnaround:<11}{p.waiting}")
print(f"\nAverage Turnaround Time: {sum(p.turnaround for p in processes) / len(processes):.2f}")
print(f"Average Waiting Time: {sum(p.waiting for p in processes) / len(processes):.2f}")
