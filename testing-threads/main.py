import threading

total = 0
# Function to calculate the sum
def tester(results, index):
    global total
    for i in range(1,100,1):
        print(i)
        total += i
        
    # Save the result in the shared list at the specified index
    results[index] = total

def main():
    # List to store the results of each thread
    results = [None] * 2

    # Create threads and pass the results list and index to each thread
    t1 = threading.Thread(target=tester, args=(results, 0))
    t2 = threading.Thread(target=tester, args=(results, 1))
    
    # Start the threads
    t1.start()
    
    t2.start()
    
    # Wait for both threads to finish
    t1.join()
    t2.join()

    print(total)
    # Display the result of each thread
    # print(f"Result from thread 1: {results[0]}")
    # print(f"Result from thread 2: {results[1]}")
    print("Done")

if __name__ == "__main__":
    main()
