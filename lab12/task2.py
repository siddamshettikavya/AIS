import time
import bisect

# Sample dataset
data = [
    {"title": "Machine Learning", "author": "Andrew Ng"},
    {"title": "Deep Learning", "author": "Yann LeCun"},
    {"title": "NLP Basics", "author": "Christopher Manning"},
    {"title": "Computer Vision", "author": "Fei-Fei Li"},
    {"title": "Reinforcement Learning", "author": "Richard Sutton"}
]

# -------- Linear Search --------
def linear_search(data, keyword):
    return [book for book in data if keyword.lower() in book["title"].lower() 
            or keyword.lower() in book["author"].lower()]

# -------- Binary Search --------
def binary_search(data, keyword):
    sorted_data = sorted(data, key=lambda x: x["title"].lower())
    titles = [book["title"].lower() for book in sorted_data]
    index = bisect.bisect_left(titles, keyword.lower())
    results = []
    while index < len(titles) and keyword.lower() in titles[index]:
        results.append(sorted_data[index])
        index += 1
    return results

# -------- Hash Search --------
def build_hash(data):
    return {book["title"].lower(): book for book in data} | \
           {book["author"].lower(): book for book in data}

def hash_search(table, keyword):
    return [table[keyword.lower()]] if keyword.lower() in table else []


# -------- Compare Searches --------
keyword = input("Enter keyword (title/author): ")

# Linear
start = time.time()
lin = linear_search(data, keyword)
print("Linear:", lin, "Time:", time.time()-start)

# Binary
start = time.time()
binr = binary_search(data, keyword)
print("Binary:", binr, "Time:", time.time()-start)

# Hash
hash_table = build_hash(data)
start = time.time()
hsh = hash_search(hash_table, keyword)
print("Hash:  ", hsh, "Time:", time.time()-start)
