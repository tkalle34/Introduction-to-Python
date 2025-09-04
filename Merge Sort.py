
# I added a few other methods for fun

import random


def mergeSort(input:list):
    """
    Sorts a list using the Merge Sort algorithm.

    @param arr: list. The list of elements to sort.
    @return list. A new sorted list.
    """
    if len(input) <= 1:
        return input

    mid = len(input)//2
    left = mergeSort(input[:mid])
    right = mergeSort(input[mid:])

    return merge(left, right)

def merge(left: list, right: list):
    """
    Merges two sorted lists into one sorted list.

    @param left: list. First sorted sublist.
    @param right: list. Second sorted sublist.
    @return list. A merged and sorted list.
    """
    result= []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def quickSort(input): # For fun

    if len(input) <= 1:
        return input

    pivotIndex = len(input)//2
    pivot = input[pivotIndex]

    left = []
    middle = []
    right = []

    for i in range(len(input)):
        if input[i] < pivot:
            left.append(input[i])
        elif input[i] > pivot:
            right.append(input[i])
        else:
            middle.append(input[i])
    sortedLeft = quickSort(left)
    sortedRight = quickSort(right)

    return sortedLeft + middle + sortedRight

def binarySearch(arr, target, left, right):
    """
    Recursive binary search on a sorted (ascending) list.

    @param arr: list. Sorted list (ascending).
    @param target: Any. Value to search for.
    @return int. Index of target if found; otherwise "Not Found".
    """
    if left > right:
        return "Not Found"

    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binarySearch(arr, target, mid + 1, right)
    else:
        return binarySearch(arr, target, left, mid - 1)


def generateTestList(size=10, minVal=0, maxVal=100):
    """
    Generates a random list of integers for testing purposes.

    @param size: int. Number of elements in the list (default: 10).
    @param minVal: int. Minimum possible integer value (default: 0).
    @param maxVal: int. Maximum possible integer value (default: 100).
    @return list. A randomly generated list of integers.
    """
    return [random.randint(minVal, maxVal) for _ in range(size)]


if __name__ == "__main__":
    myList = generateTestList(20, 0, 100)
    print("Original: {0}".format(myList))
    sortedList = mergeSort(myList)
    print("Sorted: {0}".format(sortedList))
    sortedList2 = quickSort(myList)
    print("Sorted: {0}".format(sortedList2))
    num = random.randint(0,100)
    print("{0} was found in position: {1}".format(num,
                                                  binarySearch(sortedList,num,0,
                                                               len(sortedList)-1)))