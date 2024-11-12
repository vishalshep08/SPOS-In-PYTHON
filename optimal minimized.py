def optimal_page_replacement():
    pages = list(map(int, input("Enter the page numbers (space-separated): ").split()))
    capacity = int(input("Enter the capacity of frame: "))

    frame, hit, fault = [], 0, 0

    for i in range(len(pages)):
        if pages[i] in frame:
            hit += 1
        else:
            fault += 1
            if len(frame) < capacity:
                frame.append(pages[i])
            else:
                farthest = -1
                index_to_replace = 0
                for j in range(len(frame)):
                    if frame[j] not in pages[i+1:]:
                        index_to_replace = j
                        break
                    else:
                        next_use = pages[i+1:].index(frame[j]) + i + 1
                        if next_use > farthest:
                            farthest = next_use
                            index_to_replace = j
                frame[index_to_replace] = pages[i]

        print(f"{'H' if pages[i] in frame else 'F'}", end=" ")

    hit_ratio = (hit / len(pages)) * 100
    fault_ratio = (fault / len(pages)) * 100
    print(f"\nHits: {hit}, Faults: {fault}")
    print(f"Hit Ratio: {hit_ratio:.2f}%, Fault Ratio: {fault_ratio:.2f}%")

# Run the function
optimal_page_replacement()
