import random
import time
import heapq

# -------------------------------
# Simulate stock data
# -------------------------------
def generate_stocks(n):
    stocks = []
    for i in range(n):
        symbol = f"STK{i+1:03d}"  # Stock symbols: STK001, STK002...
        open_price = round(random.uniform(100, 500), 2)
        close_price = round(open_price * random.uniform(0.9, 1.1), 2)  # daily change ±10%
        stocks.append({
            "symbol": symbol,
            "open": open_price,
            "close": close_price,
            "change": round(((close_price - open_price)/open_price)*100, 2)
        })
    return stocks

# -------------------------------
# Heap Sort by percentage change
# -------------------------------
def heap_sort_stocks(stocks):
    heap = [(-s["change"], s) for s in stocks]  # max-heap using negative change
    heapq.heapify(heap)
    sorted_stocks = []
    while heap:
        sorted_stocks.append(heapq.heappop(heap)[1])
    return sorted_stocks

# -------------------------------
# Search with Hash Map
# -------------------------------
def create_stock_map(stocks):
    return {s["symbol"]: s for s in stocks}

def search_stock(stock_map, symbol):
    return stock_map.get(symbol, None)

# -------------------------------
# Main Program
# -------------------------------
if __name__ == "__main__":
    n = 20  # Number of stocks
    stocks = generate_stocks(n)

    print("Generated Stock Data:")
    for s in stocks:
        print(s)

    # -------------------------------
    # Sorting
    # -------------------------------
    start = time.time()
    sorted_stocks = heap_sort_stocks(stocks)
    end = time.time()
    print(f"\n✅ Stocks sorted by % change using Heap Sort (Time: {end-start:.6f} sec):")
    for s in sorted_stocks:
        print(s)

    # Compare with Python sorted()
    start = time.time()
    sorted_std = sorted(stocks, key=lambda x: x["change"], reverse=True)
    end = time.time()
    print(f"\n✅ Stocks sorted by % change using sorted() (Time: {end-start:.6f} sec):")
    for s in sorted_std:
        print(s)

    # -------------------------------
    # Searching
    # -------------------------------
    stock_map = create_stock_map(stocks)

    symbol_to_search = "STK005"
    start = time.time()
    result = search_stock(stock_map, symbol_to_search)
    end = time.time()
    print(f"\nSearch result for {symbol_to_search} using Hash Map (Time: {end-start:.6f} sec):")
    print(result)

    # Compare with linear search
    start = time.time()
    result_linear = next((s for s in stocks if s["symbol"] == symbol_to_search), None)
    end = time.time()
    print(f"\nSearch result for {symbol_to_search} using linear search (Time: {end-start:.6f} sec):")
    print(result_linear)
