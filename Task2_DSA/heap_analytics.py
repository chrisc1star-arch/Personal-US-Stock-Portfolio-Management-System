"""
heap_analytics.py
Demonstrates the use of a Max-Heap data structure and Heap Sort algorithm
for analyzing financial data (e.g., ranking stock returns).
"""

def heapify(arr: list, n: int, i: int):
    """
    Maintains the Max-Heap property.
    Parameters:
        arr: The list containing tuples of (Ticker, Return_Percentage).
        n: The size of the heap.
        i: The index of the current root node of the subtree.
    """
    largest = i          # Initialize largest as root
    left = 2 * i + 1     # Left child index
    right = 2 * i + 2    # Right child index

    # Compare left child with root based on the return percentage (index 1 of tuple)
    if left < n and arr[left][1] > arr[largest][1]:
        largest = left

    # Compare right child with the currently determined largest
    if right < n and arr[right][1] > arr[largest][1]:
        largest = right

    # If the largest is not the root, swap and continue to heapify down the tree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr: list):
    """
    Implements the Heap Sort algorithm.
    Time Complexity: O(n log n).
    """
    n = len(arr)

    # Step 1: Build a Max-Heap from the unsorted array
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        # Move current root (maximum element) to the end of the array
        arr[i], arr[0] = arr[0], arr[i]
        # Call max heapify on the reduced heap
        heapify(arr, i, 0)

def main():
    print("\n" + "=" * 50)
    print("Stock Performance Ranker (Heap Sort)".center(50))
    print("=" * 50)
    
    # Allow user to input custom data
    print("Let's build a watchlist to sort by daily returns.")
    print("You can type 'done' when you finish adding stocks.\n")
    
    stock_data = []
    while True:
        ticker = input("Enter stock ticker (or 'done' to finish): ").upper()
        if ticker == 'DONE':
            break
            
        try:
            pct_return = float(input(f"Enter today's return % for {ticker} (e.g., 2.5 or -1.2): "))
            stock_data.append((ticker, pct_return))
            print(f"Added {ticker}: {pct_return}%")
        except ValueError:
            print("Invalid input. Please enter a numerical value for the return.\n")

    # Fallback to default data if user skipped input
    if not stock_data:
        print("\nNo data entered. Using default market data...")
        stock_data = [("AAPL", 1.5), ("TSLA", -2.3), ("MSFT", 0.8), ("NVDA", 4.2), ("AMZN", 1.1)]

    print("\n--- Processing Data ---")
    print(f"Original Unsorted Data: {stock_data}")
    
    # Execute O(n log n) sorting
    heap_sort(stock_data)
    
    print("\n" + "-" * 40)
    print("Top Performing Stocks (Worst to Best)")
    print("-" * 40)
    
    # Since Max-Heap sort places the largest items at the end, 
    # reading it left-to-right gives ascending order.
    rank = 1
    for ticker, pct_return in stock_data:
        sign = "+" if pct_return > 0 else ""
        print(f"Rank {rank}: {ticker:<5} | Return: {sign}{pct_return:.2f}%")
        rank += 1
        
    print("-" * 40)

if __name__ == "__main__":
    main()
