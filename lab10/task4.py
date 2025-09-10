def process_scores(scores):
    if not scores:
        print("Average:", 0)
        print("Highest:", None)
        print("Lowest:", None)
        return

    total = sum(scores)
    avg = total / len(scores)

    highest = max(scores)
    lowest = min(scores)

    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)

scores = [85, 90, 78, 92, 88]
process_scores(scores)