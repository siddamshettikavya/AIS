def grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"
scores = [95, 82, 67, 74, 58]
for s in scores:
    print(f"Score: {s}, Grade: {grade(s)}")


