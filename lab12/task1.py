import time
import random

# -------------------------------
# Quick Sort
# -------------------------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x["cgpa"] >= pivot["cgpa"]]
    right = [x for x in arr[1:] if x["cgpa"] < pivot["cgpa"]]
    return quick_sort(left) + [pivot] + quick_sort(right)

# -------------------------------
# Merge Sort
# -------------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]["cgpa"] >= right[j]["cgpa"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# -------------------------------
# Display Top 10 Students
# -------------------------------
def display_top_10(students):
    print("\n🏆 Top 10 Students by CGPA:")
    print("-" * 40)
    print(f"{'Name':<15} {'Roll No':<12} {'CGPA':<5}")
    print("-" * 40)
    for s in students[:10]:
        print(f"{s['name']:<15} {s['roll']:<12} {s['cgpa']:<5}")

# -------------------------------
# Main Program
# -------------------------------
if __name__ == "__main__":
    students = []
    n = int(input("Enter the number of students: "))

    # Loop to generate student records automatically
    for i in range(n):
        name = f"Student{i+1}"
        roll = f"2403a51{i:02d}"  # e.g., 2403a5100, 2403a5101 ...
        cgpa = round(random.uniform(7.0, 10.0), 2)  # random CGPA between 7 and 10
        students.append({"name": name, "roll": roll, "cgpa": cgpa})

    print("\nChoose sorting algorithm:")
    print("1. Quick Sort")
    print("2. Merge Sort")
    choice = int(input("Enter choice (1/2): "))

    if choice == 1:
        start = time.time()
        sorted_students = quick_sort(students)
        end = time.time()
        print(f"\n✅ Records sorted using Quick Sort (Time: {end-start:.6f} sec)")
    else:
        start = time.time()
        sorted_students = merge_sort(students)
        end = time.time()
        print(f"\n✅ Records sorted using Merge Sort (Time: {end-start:.6f} sec)")

    print("\n📋 Sorted Student Records:")
    print("-" * 40)
    print(f"{'Name':<15} {'Roll No':<12} {'CGPA':<5}")
    print("-" * 40)
    for s in sorted_students:
        print(f"{s['name']:<15} {s['roll']:<12} {s['cgpa']:<5}")

    display_top_10(sorted_students)
