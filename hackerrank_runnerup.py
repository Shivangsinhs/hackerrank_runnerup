

def second_largest(arr):
    # Find the largest number in the list
    largest = max(arr)
    
    # Remove the largest number from the list
    arr.remove(largest)
    
    # Find the second largest number by finding the new max of the modified list
    second_largest = max(arr)
    
    # Return the second largest number
    return second_largest

# Input the number of elements in the list
n = int(input())

# Input the elements of the list and convert them to integers
arr = list(map(int, input().split()))

# Call the second_largest function and print the result
print(second_largest(arr))
