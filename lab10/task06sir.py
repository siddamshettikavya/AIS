def grade(score):
    if score >= 90:
        return "A"
    else:
        if score >= 80:
            return "B"
        else:
            if score >= 70:
                return "C"
            else:
                if score >= 60:
                    return "D"
                else:
                    return "F"
scores = [95, 82, 67, 74, 58]
for s in scores:
    print(f"Score: {s}, Grade: {grade(s)}")


