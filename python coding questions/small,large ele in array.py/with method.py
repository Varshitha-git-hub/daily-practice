#we cannot give int() because seperated by spaces so it can be consider as string.
numbers=input("enter numbers seperated by spaces:")#seperated by spaces can be used for user comfortability.
num_list=numbers.split()
#split can be used for to change the input string into a list of numbers.
smallest=num_list[0]
print(num_list)
for num in num_list:
    if int(num)<int(smallest):
        smallest=num
print("smallest number:",smallest)   




numbers = input("Enter numbers separated by spaces: ")
arr = numbers.split()
arr = [int(num) for num in arr]
#This line converts each string number in the list to an integer using a shortcut called "list comprehension".
arr.sort()
print("Smallest element:", arr[0])
# print("Largest element:", arr[-1])

