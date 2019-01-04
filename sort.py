from random import randint
import time

def bubbleSortAlgo(array):
    for x in range(0, len(array)):
        for y in range(0, len(array) -x - 1):
            if(array[y+1] < array[y]):
                next = array[y+1]
                current = array[y]
                array[y+1] = current
                array[y] = next
    return array
	
def randomArrayGenerator(min, max, length):
    array = []
    for x in range(0, length):
        array.append(randint(min, max))
    return array

def measureSortingTime(sort, array):
    start = time.clock()
    print(sort(array))
    ending = time.clock()
    elapsed = ending - start
    print(str(elapsed * 1000) + "ms")

def main():
    array = randomArrayGenerator(0, 300, 10)
    print(array)
    measureSortingTime(bubbleSortAlgo, array)

if __name__ == "__main__":
    main()