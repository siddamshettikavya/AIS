def format_name(full_name):
    parts = full_name.strip().split()
    if len(parts) >= 2:
        first = parts[0]
        last = parts[-1]
        return f"{last}, {first}"
    return full_name
print(format_name("John Smith"))      
print(format_name("Alice Johnson"))   
print(format_name("Michael Jordan"))  
