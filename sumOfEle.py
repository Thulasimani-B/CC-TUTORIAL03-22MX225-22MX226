arr = []
n = int(input("Enter the no of elements in an array : "))

print("Enter the array elements one by one: ")
for i in range(n):
    print("arr[",i,"]: ",end=" ")
    arr.append(int(input()))
    
print("The given array elements are: ")
for i in range(n):
    print("arr[",i,"]: ",end=" ")
    print(arr[i])
    
sum = 0 
for i in range(n):
    sum = sum + arr[i]

print("The sum of the array elements are: ",sum)

# Edited by Sushma (22MX225), the second collaborator

arr2 = []
n2 = int(input('\nEnter the size of second array: '))

print('Enter the array elements (float values):')

for i in range(n2):
    arr2.append(float(input()))

sum2 = 0
for i in range(n2):
    sum2 += arr2[i]

print('Sum of second array elements: ', sum2)