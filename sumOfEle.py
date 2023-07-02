arr = []
n = int(input("Enter the no of elements in an array : "))

print("Enter the array elements one by one: ")
for i in range(0,n):
    print("arr[",i,"]: ",end=" ")
    arr.append(int(input()))
    
print("The given array elements are: ")
for i in range(0,n):
    print("arr[",i,"]: ",end=" ")
    print(arr[i])
    
sum = 0 
for i in range(0,n):
    sum = sum + arr[i]

print("The sum of the array elements are: ",sum)

    
    