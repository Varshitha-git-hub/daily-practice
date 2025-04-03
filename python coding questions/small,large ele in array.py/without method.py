
numbers = input("Enter numbers separated by spaces: ")
arr = []
num = ""

for char in numbers:
  if char != " ":
    num += char
  else:
    arr.append(int(num))
    num = ""
arr.append(int(num))

for i in range(len(arr)):
  for j in range(len(arr) - 1):
    if arr[j] > arr[j + 1]:
      arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Smallest element:", arr[0])
print("Largest element:", arr[-1])
