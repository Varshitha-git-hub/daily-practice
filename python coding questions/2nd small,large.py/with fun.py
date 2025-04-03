def second_smallest_second_largest():
    arr = list(map(int, input("Enter the list of numbers separated by space: ").split()))#to convert the map object to a list is called list() function.
    arr = list(set(arr))#set(arr) removes duplicates & list() converts the result back into a list.
    if len(arr) < 2:#it can len(arr) is lessthan 2
        return -1, -1#it is condition checker <2 return -1,-1 & >2 return second smallesta dn largest numbers.
    arr.sort()#sort elements in ascending order.
    return arr[1], arr[-2]#2nd smallest index[1] & second largest index[-2]

second_smallest, second_largest = second_smallest_second_largest()
print("Second Smallest:", second_smallest)
print("Second Largest:", second_largest)
