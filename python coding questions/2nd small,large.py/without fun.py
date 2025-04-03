
arr = list(map(int, input("Enter the array elements separated by space: ").split()))
if len(arr) < 2:
    print("-1, -1")
else:
    arr.sort()
    print("Second Smallest:", arr[1])
    print("Second Largest:", arr[-2])
