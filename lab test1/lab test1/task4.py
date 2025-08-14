def generate_email(name):
    parts = name.strip().split()
    if len(parts) < 2:
        return None
    first_letter = parts[0][0].lower()
    last_name = parts[-1].lower()
    email = f"{first_letter}{last_name}@sru.edu.in"
    return email

# Few-shot prompting examples
examples = [
    "Anita Sharma",
    "Ravi Kumar",
    "Priya Singh",
    "Kavya shetti"  # Replace with your student name if needed
]
for name in examples:
    email = generate_email(name)
    print(f"Name: {name}")
    print(f"Email: {email}\n")