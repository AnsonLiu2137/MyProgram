# finds the max increase between any two elements in a random list
# (not necessarily adjacent)
import random
import sys
import time

def main():
    # get the size of the list from the terminal and convert it from a 
    # to an int
    list_size = int(sys.argv[1])

    # make a random list of numbers
    max_num = 1_000_000
    numbers = [ ]
    print(f"Generating random list of {list_size} numbers.")
    for i in range(list_size):
        n = random.randint(0, max_num)
        numbers.append(n)

    print(f"Now searching for the max increase.")
    # uncomment this if you want to see the list generated:
    # print(numbers)
    start_time = time.time()
    max_increase(numbers)
    elapsed_time = time.time() - start_time
    print(f"it took {elapsed_time:.4f} seconds to find.")

def max_increase(a):
    index1 = -1
    index2 = -1
    max_increase = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if (a[j] - a[i] > max_increase):
                max_increase = a[j] - a[i]
                index1 = i
                index2 = j
    if (max_increase == 0):
        print("this data didn't increase ever")
    else:
        print(f"For a random list of size {len(a)}, the max increase",
              f"was {max_increase}, between indices {index1} and {index2}.")

main()
