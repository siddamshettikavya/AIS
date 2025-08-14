# Few-shot prompt for Copilot:
# "Generate all prime numbers between start and end (inclusive).\nStart: 5\nEnd: 11\nOutput: [5, 7, 11]\nStart: 10\nEnd: 20\nOutput: [11, 13, 17, 19]\nStart: {start}\nEnd: {end}\nOutput:"

def generate_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes
    return primes

if __name__ == "__main__":
    start = int(input("Enter start: "))
    end = int(input("Enter end: "))
    print(generate_primes(start, end))