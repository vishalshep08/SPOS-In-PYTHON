def lru_page_replacement():
    pages = list(map(int, input("Enter the page numbers (space-separated): ").split()))
    capacity = int(input("Enter the frame capacity: "))

    frame = []
    hit = 0
    fault = 0

    print("\nPage Replacement Process:")
    for page in pages:
        if page in frame:
            hit += 1
            frame.remove(page)  # Remove to mark as recently used
            print(" H ", end="")
        else:
            fault += 1
            if len(frame) == capacity:
                frame.pop(0)  # Remove the least recently used page
            print(" F ", end="")
        frame.append(page)  # Add page as the most recently used

    # Calculate hit and fault ratios
    hit_ratio = (hit / len(pages)) * 100
    fault_ratio = (fault / len(pages)) * 100

    print(f"\n\nTotal Page Faults: {fault}")
    print(f"Total Page Hits: {hit}")
    print(f"Hit Ratio: {hit_ratio:.2f}%")
    print(f"Fault Ratio: {fault_ratio:.2f}%")

# Run the function
lru_page_replacement()