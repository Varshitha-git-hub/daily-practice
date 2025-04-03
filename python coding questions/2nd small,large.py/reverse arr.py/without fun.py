N = int(input("Enter the array size: "))
arr = list(map(int, input("Enter the array elements separated by space: ").split()))
print(arr)
arr = arr[::-1]
print("Reversed Array:",arr)