def fifo_page_replacement(pages, capacity):
    frame = [-1] * capacity
    index = hit = fault = 0
    
    for page in pages:
        if page in frame:
            hit += 1
            print(" H ", end="")
        else:
            frame[index] = page
            fault += 1
            print(" F ", end="")
            index = (index + 1) % capacity
    
    print(f"\nPage Faults: {fault}  Page Hits: {hit}")
    print(f"Hit Ratio: {hit / len(pages) * 100:.2f}%  Fault Ratio: {fault / len(pages) * 100:.2f}%")

# Input
pages = list(map(int, input("Enter the pages (space-separated): ").split()))
capacity = int(input("Enter the frame capacity: "))

# Run simulation
fifo_page_replacement(pages, capacity)
