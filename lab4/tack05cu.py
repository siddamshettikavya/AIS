def count_lines(filename):
  """Reads a text file and prints its number of lines."""
  try:
    with open(filename, 'r') as f:
      lines = f.readlines()
      print(f"Number of lines in {filename}: {len(lines)}")
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

# Example usage:
# Create a dummy file for testing
with open("example.txt", "w") as f:
  f.write("hello world\n")
  f.write("hi hello\n")
  f.write("sru ai technology\n")


count_lines("example.txt")

# You can replace "example.txt" with the path to your file.