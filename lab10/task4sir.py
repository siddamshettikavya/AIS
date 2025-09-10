def process_scores(scores):
    total = sum(scores)
    avg = total / len(scores)

    highest = scores[0]
    lowest = scores[0]

    for s in scores:
        if s > highest:
            highest = s
        if s < lowest:
            lowest = s

    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)

scores = [85, 90, 78, 92, 88]
process_scores(scores)