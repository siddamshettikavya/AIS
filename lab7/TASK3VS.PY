# code1
with open("example.txt", "w") as f:
    f.write("Hello,world!")

# code2
f1 = open("data1.txt", "w")
f2 = open("data2.txt", "w")
f1.write("First file content\n")
f2.write("Second file content\n")
f1.close()
f2.close()
print("files written successfully")

# code3
data = open("input.txt", "r").readlines()
output = open("output.txt", "w")
for line in data:
    output.write(line.upper())
output.close()
print("processing done")

# code4 (fixed)
# write some numbers first
f = open("numbers.txt", "w")
f.write("1\n2\n3\n4\n5\n")
f.close()

# now read the numbers
f = open("numbers.txt", "r")
nums = f.readlines()
f.close()

squares = []
for n in nums:
    n = n.strip()
    if n.isdigit():
        squares.append(int(n) * int(n))

f2 = open("squares.txt", "w")
for sq in squares:
    f2.write(str(sq) + "\n")
f2.close()
print("squares written")
