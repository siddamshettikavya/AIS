def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Error: File not found."
    except IOError:
        return "Error: Unable to read the file."
    except Exception as e:
        return f"Unexpected error: {e}"

# 🧪 Test block with output
if __name__ == "__main__":
    content = read_file("example.txt")
    print("File Content:\n", content)